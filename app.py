import gradio as gr
from resumeanalyzer import ResumeAnalyzer
analyzer = ResumeAnalyzer()
def analyze_resume(resume_file, job_desc):
    file_name = resume_file.name
    if file_name.endswith(".pdf"):
        resume_text = analyzer.load_pdf_text(resume_file.name)
    elif file_name.endswith(".txt"):
        resume_text = resume_file.read().decode("utf-8")
    else:
        return "Unsupported file type.", "", "0%"
    matched, missing = analyzer.compare_keywords(resume_text, job_desc)
    job_keywords = analyzer.extract_keywords(job_desc)
    match_score = round(len(matched) / len(job_keywords) * 100) if job_keywords else 0
    matched_str = "\n".join(f" {kw}" for kw in matched)
    missing_str = "\n".join(f" {kw}" for kw in missing)
    return matched_str, missing_str, f"{match_score}%"
custom_css = """
body, .gr-block, .gr-button, .gr-textbox textarea, .gr-textbox label, .gr-label, .gr-file, .gr-input, .gr-output {
    font-family: Georgia, serif !important;
    color: #FFFFFF !important;
}
body {
    background-color: #87CEEB;
}
.gr-button {
    background-color: #000000 !important;
    color: #FFFFFF !important;
    border: none;
    font-weight: bold;
}
.gr-textbox, .gr-file {
    background-color: #000000 !important;
    border: none;
}
"""
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("<h1 style='text-align: center; color: white;'> Resume Keyword Analyzer</h1>")
    with gr.Row():
        resume_input = gr.File(label="Upload Resume (.txt or .pdf)")
        job_input = gr.Textbox(label="Paste Job Description", lines=10, placeholder="Paste job description here...")
    analyze_btn = gr.Button(" Analyze Resume")
    matched_output = gr.Textbox(label=" Matched Keywords", lines=10)
    missing_output = gr.Textbox(label=" Missing Keywords", lines=10)
    score_output = gr.Textbox(label=" Match Score")
    analyze_btn.click(
        fn=analyze_resume,
        inputs=[resume_input, job_input],
        outputs=[matched_output, missing_output, score_output]
    )
demo.launch()