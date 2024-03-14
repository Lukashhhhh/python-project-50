from gendiff.read_file import get_file_data
from gendiff.diff_tree import build_diff_tree
from gendiff.formatters.format_selection import get_formated_data


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data_file1 = get_file_data(file_path1)
    data_file2 = get_file_data(file_path2)
    sorted_diff = build_diff_tree(data_file1, data_file2)
    formated_data = get_formated_data(format_name, sorted_diff)
    return formated_data
