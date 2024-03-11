from gendiff.read_file import get_file_data
from gendiff.parser import get_sorted_data
from gendiff.stylish import get_formated_diff 


def generate_diff(file_path1, file_path2):
    data_file1 = get_file_data(file_path1)
    data_file2 = get_file_data(file_path2)
    sorted_diff = get_sorted_data(data_file1, data_file2)
    formated_data = get_formated_diff(sorted_diff)
    return formated_data