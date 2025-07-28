import json
import os

def write_output(folder_path, persona, job_to_be_done, extracted_sections, output_path):
    output = {
        "metadata": {
            "collection_name": os.path.basename(folder_path),
            "persona": persona,
            "job_to_be_done": job_to_be_done
        },
        "extracted_sections": extracted_sections
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=4)
