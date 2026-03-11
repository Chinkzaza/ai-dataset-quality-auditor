import json

def audit_dataset(file_path):
    with open(file_path) as f:
        data = json.load(f)

    total = len(data)
    missing_labels = 0

    for item in data:
        if "label" not in item or item["label"] == "":
            missing_labels += 1

    print("Total entries:", total)
    print("Missing labels:", missing_labels)

audit_dataset("dataset.json")
