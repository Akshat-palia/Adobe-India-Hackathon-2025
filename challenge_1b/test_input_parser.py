from input_parser import parse_input
import os

collections = ["Collection_1", "Collection_2", "Collection_3"]

for collection in collections:
    input_path = os.path.join(collection, "input.json")
    print(f"\n--- Parsing {collection} ---")
    
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        continue

    parsed_data = parse_input(input_path)
    print("Parsed Input:\n", parsed_data)
