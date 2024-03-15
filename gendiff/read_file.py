import os
import json
import yaml


def get_file_data(file_path: str):
    _, expansion = os.path.splitext(file_path)
    return extract_data_from_file(file_path, expansion)


def extract_data_from_file(file_path: str, expansion: str):
    match expansion:
        case '.json':
            return json.load(open(file_path))
        case '.yml' | '.yaml':
            return yaml.safe_load(open(file_path))
