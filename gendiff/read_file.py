import os
import json
import yaml


def get_file_data(file_path: str):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as file:
        return extract_data_from_file(file, extension)


def extract_data_from_file(file, extension: str):
    match extension:
        case '.json':
            return json.load(file)
        case '.yml' | '.yaml':
            return yaml.safe_load(file)
