from gendiff.read_file import get_file_data
from gendiff.parser import get_sorted_data
from gendiff.format.json import get_formated_json
from gendiff.format.stylish import get_formated_stylish
from gendiff.format.plain import get_formated_plain


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data_file1 = get_file_data(file_path1)
    data_file2 = get_file_data(file_path2)
    sorted_diff = get_sorted_data(data_file1, data_file2)
    match format_name:
        case 'stylish':
            formated_data = get_formated_stylish(sorted_diff)
        case 'plain':
            formated_data = get_formated_plain(sorted_diff)
        case 'json':
            formated_data = get_formated_json(sorted_diff)
    return formated_data
