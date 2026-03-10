from resumeanalyzer import ResumeAnalyzer
analyzer = ResumeAnalyzer()
resume_path = input("Enter your resume file name (with .txt or .pdf): ").strip()
if resume_path.endswith(".pdf"):
    resume_text = analyzer.load_pdf_text(resume_path)
elif resume_path.endswith(".txt"):
    resume_text = analyzer.load_text(resume_path)
else:
    raise ValueError("Unsupported resume file format. Use .txt or .pdf")
job_text = analyzer.load_text("jobdescription.txt")
matched, missing = analyzer.compare_keywords(resume_text, job_text)
job_keywords = analyzer.extract_keywords(job_text)
match_score = round(len(matched) / len(job_keywords) * 100) if job_keywords else 0
print(f"\n Match Score: {match_score}%")
print("\n Matched Keywords: ")
for keyword in matched: 
    print(f" - {keyword}")
print("\n Missing Keywords: ")
for keyword in missing: 
    print(f" - {keyword}")
with open("report.txt", "w") as f:
    f.write(f"Match Score: {match_score}%\n\n")
    f.write("Matched Keywords:\n")
    for keyword in matched:
        f.write(f" - {keyword}\n")
    f.write("Missing Keywords:\n")
    for keyword in missing:
        f.write(f" - {keyword}\n")
