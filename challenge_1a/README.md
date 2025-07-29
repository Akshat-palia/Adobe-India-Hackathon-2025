# Adobe India Hackathon 2025 – Challenge 1a  
## 📄 PDF Outline Extraction (Structured JSON Output)

This project automatically extracts structured outlines (headings with levels and page numbers) from multiple PDF documents and generates corresponding JSON outputs following a specified schema.

---

## 🛠️ Tech Stack & Tools
- **Language:** Python 3.9+
- **Libraries:** PyMuPDF (`fitz`), `jsonschema`, `os`, `re`
- **Containerization:** Docker (CPU-only)
- **Platform:** Linux (amd64), Mac (tested on ARM64 via x86 image)
- **Open-source only:** ✅

---

## 📁 Folder Structure

challenge_1a_final/
├── Dockerfile
├── process_pdfs.py
├── validate_output.py
├── requirements.txt
├── sample_dataset/
│ ├── pdfs/
│ │ ├── sample1.pdf
│ │ ├── test_50_page.pdf
│ │ └── complex_layout.pdf
│ ├── outputs/
│ │ ├── sample1.json
│ │ ├── test_50_page.json
│ │ ├── complex_layout.json
│ └── schema/
│ └── output_schema.json


---

## 🚀 How to Run (Using Docker)

### 1. Build the Docker image:
```bash
docker build -t pdf-processor .


 2. Run the processor:

docker run --rm \
  -v "$(pwd)/sample_dataset/pdfs:/app/sample_dataset/pdfs:ro" \
  -v "$(pwd)/sample_dataset/outputs:/app/sample_dataset/outputs" \
  pdf-processor

### 3. Validate the outputs (on host):
python validate_output.py

✅ Features & Highlights

🔍 Automatically scans all .pdf files inside /app/sample_dataset/pdfs/
🧠 Extracts hierarchical headings (H1, H2...) with corresponding page numbers
📤 Outputs JSON per PDF file: filename.json → /app/sample_dataset/outputs
🔐 Validates all outputs using output_schema.json
⏱️ Designed for ≤10s execution for 50-page PDFs
💡 Lightweight: No models >200MB, CPU-only, zero internet requirement

📋 Assumptions & Notes

Only headings with clearly distinguishable font sizes/styles are extracted
Multi-column PDFs are partially supported depending on layout clarity
Files like .DS_Store are ignored automatically
Text styles (e.g., bold, font size) are used heuristically for heading levels


👨‍🔬 Tested On

✅ Simple structured PDF (sample1.pdf)
✅ Complex multi-layout PDF (complex_layout.pdf)
✅ 50-page performance test PDF (test_50_page.pdf)

### 📄 Schema (Key Structure)

Each JSON output follows:

{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Section Title",
      "page": 2
    },
    ...
  ]
}

###
To create a .tar.gz for submission:

tar -czvf challenge_1a_final.tar.gz \
    Dockerfile \
    process_pdfs.py \
    validate_output.py \
    requirements.txt \
    sample_dataset/


## Author

Made with ❤️ by **Akshat Palia**

- 💼 [LinkedIn](https://www.linkedin.com/in/akshatpalia/)
- 💻 [GitHub](https://github.com/Akshat-palia)

Submission for Adobe India Hackathon 2025 – Challenge 1a
