import json

def load_ontology():
    with open("core/ontology.json") as f:
        return json.load(f)
