# Resume Keyword Analyzer

This project analyzes how well a resume matches a job description by extracting and comparing important keywords using natural language processing.

The tool identifies keywords from the job description and checks whether they appear in the resume. It then calculates a match score and shows which keywords are present and which are missing.

The project includes both a command-line interface and a web interface built with Gradio.

## Features

- Resume analysis against job descriptions
- Automatic keyword extraction using NLP
- Match score calculation
- Identification of missing keywords
- Support for `.txt` and `.pdf` resumes
- Interactive web interface using Gradio

## How It Works

1. The user uploads a resume or provides a text file.
2. A job description is provided as input.
3. The system extracts keywords from both the resume and job description.
4. The keywords are compared to identify:
   - matched keywords
   - missing keywords
5. A match score is calculated based on keyword overlap.

## Requirements

- Python 3
- spaCy
- PyMuPDF
- Gradio
