import os
import fitz  # PyMuPDF
import json

INPUT_DIR = "sample_dataset/pdfs"
OUTPUT_DIR = "sample_dataset/outputs"

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" not in b:
                continue
            for line in b["lines"]:
                text = "".join([span["text"] for span in line["spans"]]).strip()
                font_size = max([span["size"] for span in line["spans"]])
                if font_size >= 16:
                    level = "H1"
                elif font_size >= 13:
                    level = "H2"
                elif font_size >= 11:
                    level = "H3"
                else:
                    continue
                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_number + 1
                })
    return outline

def process_all_pdfs():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(OUTPUT_DIR, f"{base_name}.json")

            print(f"Processing: {filename}")
            outline = extract_headings(input_path)
            json_output = {
                "title": base_name,
                "outline": outline
            }

            with open(output_path, "w") as f:
                json.dump(json_output, f, indent=2)

            print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    process_all_pdfs()
