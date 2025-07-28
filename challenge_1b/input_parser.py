# input_parser.py

import json
import os

def parse_input(collection_path):
    input_file = os.path.join(collection_path, "input.json")
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"input.json not found in {collection_path}")
    
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return {
        "persona": data.get("persona"),
        "job_to_be_done": data.get("job_to_be_done")
    }

# Example usage:
if __name__ == "__main__":
    sample_input = parse_input("collection_1")
    print(sample_input)
