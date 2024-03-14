from gendiff import generate_diff
import pytest


@pytest.mark.parametrize("file_path1, file_path2", [
    ('test/fixtures/file1.json', 'test/fixtures/file2.json'),
    ('test/fixtures/file1.yml', 'test/fixtures/file2.yml'),
])
def test_generate_diff_stylish_plain(file_path1, file_path2):
    result_stylish_path = 'test/fixtures/result_file_stylish.txt'
    result_plain_path = 'test/fixtures/result_file_plain.txt'
    with open(result_stylish_path) as stylish_result, open(
            result_plain_path) as plain_result:
        assert generate_diff(file_path1, file_path2) == stylish_result.read()
        assert generate_diff(file_path1, file_path2, 'plain') == plain_result.read()


@pytest.mark.parametrize("file_path1, file_path2", [
    ('test/fixtures/file1.json', 'test/fixtures/file2.json'),
    ('test/fixtures/file1.yml', 'test/fixtures/file2.yml'),
])
def test_generate_diff_json(file_path1, file_path2):
    assert isinstance(generate_diff(file_path1, file_path2, 'json'), str)
