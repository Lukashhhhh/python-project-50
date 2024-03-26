import os
import json
import yaml


def get_file_data(file_path: str):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as content:
        return parse(content, extension[1:])


def parse(content, format: str):
    match format:
        case 'json':
            return json.load(content)
        case 'yml' | 'yaml':
            return yaml.safe_load(content)
        case _:
            raise ValueError('Invalid file format')
