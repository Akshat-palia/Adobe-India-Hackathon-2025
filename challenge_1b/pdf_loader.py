import os
import fitz  # PyMuPDF

def load_pdfs(pdf_folder):
    pdf_texts = {}
    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith('.pdf'):
            path = os.path.join(pdf_folder, filename)
            doc = fitz.open(path)
            text = ""
            for page in doc:
                text += page.get_text()
            pdf_texts[filename] = text
    return pdf_texts
