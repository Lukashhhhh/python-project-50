import json


def get_formated_json(data):
    return json.dumps(data, indent=2)
