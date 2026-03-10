import spacy
import fitz
class ResumeAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
    def load_text(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    def extract_keywords(self, text):
        doc = self.nlp(text)
        return set(chunk.text.lower().strip() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 1)
    def compare_keywords(self, resume_text, job_text):
        resume_keywords = self.extract_keywords(resume_text)
        job_keywords = self.extract_keywords(job_text)
        matched = sorted(job_keywords & resume_keywords)
        missing = sorted(job_keywords - resume_keywords)
        return matched, missing
    def load_pdf_text(self, filepath):
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        return text