from gendiff import generate_diff
import pytest

@pytest.mark.parametrize("file_path1, file_path2", [
    ('test/fixtures/file1.json', 'test/fixtures/file2.json'),
    ('test/fixtures/file1.yml', 'test/fixtures/file2.yml'),
    pytest.param('test/fixtures/file1.txt', 'test/fixtures/file2.txt', marks=pytest.mark.xfail)
])
@pytest.mark.parametrize("format, result_path", [
    ('stylish', 'test/fixtures/result_file_stylish.txt'),
    ('plain', 'test/fixtures/result_file_plain.txt'),
    ('json', 'test/fixtures/result_file_json.txt'),
    pytest.param('txt', 'test/fixtures/result_file_stylish.txt', marks=pytest.mark.xfail)
])
def test_generate_diff_stylish_plain(file_path1, file_path2, format, result_path):
    with open(result_path) as result:
        assert generate_diff(file_path1, file_path2, format) == result.read()
