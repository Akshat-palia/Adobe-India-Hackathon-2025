import os
import json

from jsonschema import validate, ValidationError

# Load the schema
with open("sample_dataset/schema/output_schema.json") as f:
    schema = json.load(f)

output_dir = "./sample_dataset/outputs"

all_valid = True
for json_file in os.listdir(output_dir):
    if not json_file.endswith(".json"):
        continue

    file_path = os.path.join(output_dir, json_file)
    with open(file_path) as f:
        try:
            data = json.load(f)
            validate(instance=data, schema=schema)
            print(f"[✓] {json_file} is valid ✅")
        except (ValidationError, json.JSONDecodeError) as e:
            all_valid = False
            print(f"[!] {json_file} is INVALID ❌")
            print("    Reason:", str(e))

if all_valid:
    print("\n🎉 All JSON outputs are valid as per schema!")
else:
    print("\n⚠️ Some files are invalid. Please fix the issues above.")
