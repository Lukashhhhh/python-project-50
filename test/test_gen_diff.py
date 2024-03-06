import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file_path1, file_path2", [
    ('test/fixtures/file1.json', 'test/fixtures/file2.json')
])
def test_generate_diff(file_path1, file_path2):
    result_file_path = 'test/fixtures/result_file.txt'
    with open(result_file_path) as result:
        assert generate_diff(file_path1, file_path2) == result.read()
