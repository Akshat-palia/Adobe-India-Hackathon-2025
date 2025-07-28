from document_loader import load_documents
from input_parser import parse_input

import os

def test_loader(collection_folder):
    input_path = os.path.join(collection_folder, 'input.json')
    print(f"\n--- Testing {collection_folder} ---")
    
    parsed_input = parse_input(input_path)
    docs = load_documents(collection_folder, parsed_input)


    for doc in docs:
        print(f"Title: {doc['title']}")
        print(f"Content (first 200 chars): {doc['content'][:200]}...\n")

if __name__ == "__main__":
    test_loader("collection_1")
    test_loader("collection_2")
    test_loader("collection_3")

