from gendiff import generate_diff
import pytest


@pytest.mark.parametrize("file_path1, file_path2", [
    ('test/fixtures/file1.json', 'test/fixtures/file2.json'),
    ('test/fixtures/file1.yml','test/fixtures/file2.yml'),
])
def test_generate_diff(file_path1, file_path2):
    result_file_path = 'test/fixtures/result_file.txt'
    with open(result_file_path) as result:
        assert generate_diff(file_path1, file_path2, format='stylish') == result.read()
