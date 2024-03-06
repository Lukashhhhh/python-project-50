import os
import json
import yaml


def get_file_expansion(file_path):
    _, expansion = os.path.splitext(file_path)
    return expansion


def get_file_data(file_path):
    expansion = get_file_expansion(file_path)
    with open(file_path) as path:
        match expansion:
            case '.json':
                return json.load(path)
            case '.yml' | '.yaml':
                return yaml.safe_load(path)
