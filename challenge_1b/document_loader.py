import os
import PyPDF2

def load_documents(folder_path, parsed_input):
    docs = []
    for doc in parsed_input.get("documents", []):
        path = os.path.join(folder_path, doc["path"])
        title = doc.get("title", os.path.basename(path))

        if not os.path.exists(path):
            print(f"⚠️ File not found: {path}")
            continue

        try:
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
        except Exception as e:
            print(f"❌ Error reading {path}: {e}")
            continue

        sections = [{
            "title": "Full Document",
            "text": text[:5000]  # Take only first 5000 characters for demo
        }]

        docs.append({
            "title": title,
            "path": doc["path"],
            "sections": sections
        })

    return docs
