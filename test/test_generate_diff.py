from gendiff import generate_diff
import pytest


def get_builder_path(file_name):
    return 'test/fixtures/' + file_name


@pytest.mark.parametrize(
    "file1, file2",
    [('file1.json', 'file2.json'), ('file1.yml', 'file2.yml'),
     pytest.param('file1.txt', 'file2.txt', marks=pytest.mark.xfail)])
@pytest.mark.parametrize(
    "format, result",
    [('stylish', 'result_file_stylish.txt'),
     ('plain', 'result_file_plain.txt'), ('json', 'result_file_json.txt'),
     pytest.param('txt', 'result_file_stylish.txt', marks=pytest.mark.xfail)])
def test_generate_diff_stylish_plain(file1, file2, format, result):
    file_path1, file_path2, result_path = map(get_builder_path,
                                              (file1, file2, result))
    with open(result_path) as result:
        assert generate_diff(file_path1, file_path2, format) == result.read()
