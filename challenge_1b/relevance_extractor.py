def extract_relevant_sections(documents, persona, job_to_be_done):
    extracted = []

    for doc in documents:
        sections = []
        for section in doc["sections"]:
            score = 0
            text = section["text"].lower()

            if "methodology" in text:
                score += 2
            if "dataset" in text:
                score += 2
            if "benchmark" in text:
                score += 2
            if "performance" in text:
                score += 1
            if any(keyword in text for keyword in ["evaluation", "comparison", "metrics"]):
                score += 1

            if score >= 2:
                sections.append({
                    "subsection_title": section["title"],
                    "subsection_text": section["text"],
                    "relevance_score": score
                })

        if sections:
            extracted.append({
                "document_title": doc["title"],
                "document_path": doc["path"],
                "importance_rank": 1,  # Simplified ranking
                "sections": sections
            })

    return extracted
