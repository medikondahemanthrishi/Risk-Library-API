import json
from jsonschema import validate

with open("schema.json", "r") as file:
    schema = json.load(file)


def validate_scores(scores):
    """
    Validates the input scores using JSON Schema.
    Raises an exception if validation fails.
    """
    validate(instance=scores, schema=schema)