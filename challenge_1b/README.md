# Adobe India Hackathon 2025 – Challenge 1B: Persona-Driven Document Intelligence

## 📌 Problem Statement

Build a **persona-driven document intelligence system** that extracts and prioritizes relevant content from a collection of PDF documents based on a given persona and their job-to-be-done (JTBD). The system must:

- Ingest 3–10 PDFs and an associated `input.json`
- Extract meaningful sections/subsections from the documents
- Rank them based on importance to the persona's task
- Output a structured `output.json` for each collection

---

## 📂 Folder Structure

challenge_1b/
├── main.py
├── process_collection.py
├── utils/
│ ├── document_parser.py
│ ├── persona_ranker.py
│ ├── section_extractor.py
│ └── ...
├── collections/
│ ├── collection_1/
│ │ ├── input.json
│ │ └── PDFs/
│ │ └── ...
│ ├── collection_2/
│ │ └── ...
│ └── collection_3/
│ └── ...
└── outputs/
├── collection_1/
│ └── output.json
├── collection_2/
└── collection_3/


---

## ⚙️ How It Works

1. **Input Files:**
   - Each `collection_X/` contains:
     - `input.json` – describes the persona, job, and document metadata
     - `PDFs/` – folder containing all source PDFs

2. **Processing Pipeline:**
   - Load persona + JTBD from `input.json`
   - Parse and chunk PDF content
   - Extract headings and body sections
   - Rank sections based on persona-task relevance
   - Output the most relevant sections in a structured JSON format

3. **Output File:**
   - For each collection, an `output.json` is generated under `outputs/collection_X/`
   - Follows the Adobe-defined schema with `metadata`, `extracted_sections`, and `sub_section_analysis`

---

## 🚀 Running the Solution

```bash
# Navigate to root directory
cd challenge_1b

# Run main processing script
python main.py
{
  "metadata": {
    "challenge_id": "round_1b_001",
    "test_case_name": "kpi_financials"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "section_title": "Key Performance Metrics",
      "page_number": 4,
      "importance_rank": 1,
      "content": "Revenue grew 25% YoY in Q1..."
    },
    ...
  ],
  "sub_section_analysis": [
    {
      "section_title": "Revenue Trends",
      "summary": "Discusses year-on-year revenue change and key drivers.",
      "relevance_score": 0.93
    }
  ]
}

---


