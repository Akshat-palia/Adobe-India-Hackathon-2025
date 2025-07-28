import os
from input_parser import parse_input
from pdf_loader import load_pdfs
from relevance_extractor import extract_relevant_sections
from output_writer import write_output

def main():
    base_path = os.getcwd()  # current working directory
    collections = [d for d in os.listdir(base_path) if d.startswith("collection_") and os.path.isdir(d)]

    if not collections:
        print("No collection folders found.")
        return

    for collection in collections:
        collection_path = os.path.join(base_path, collection)
        input_path = os.path.join(collection_path, "input.json")
        pdf_dir = os.path.join(collection_path, "PDFs")
        output_path = os.path.join(collection_path, "challenge1b_output.json")

        print(f"\n--- Processing {collection} ---")
        print(f"Looking for input.json at: {input_path}")
        print(f"Looking for PDFs at: {pdf_dir}")

        # Ensure input.json exists
        if not os.path.exists(input_path):
            print(f"❌ Skipping {collection}: input.json not found at {input_path}")
            continue

        # Ensure PDFs directory exists
        if not os.path.exists(pdf_dir):
            print(f"❌ Skipping {collection}: PDFs folder not found at {pdf_dir}")
            continue

        try:
            persona, job = parse_input(input_path)
            documents = load_pdfs(pdf_dir)
            results = extract_relevant_sections(documents, persona, job)
            write_output(results, output_path)
            print(f"✅ Done: Output written to {output_path}")
        except Exception as e:
            print(f"❌ Error processing {collection}: {e}")

if __name__ == "__main__":
    main()
