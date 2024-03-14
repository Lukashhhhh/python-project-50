from gendiff.formatters.json import get_format_json
from gendiff.formatters.stylish import get_format_stylish
from gendiff.formatters.plain import get_format_plain

def get_formated_data(format, data):
    match format:
        case 'stylish':
            return get_format_stylish(data)
        case 'plain':
            return get_format_plain(data)
        case 'json':
            return get_format_json(data)
