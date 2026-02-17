import json

with open("data/taxonomy.json", "r") as f:
    taxonomy = json.load(f)


def get_suggested_action(label):
    return taxonomy[label]["suggested_action"]

