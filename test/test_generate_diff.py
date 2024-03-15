from gendiff import generate_diff
import pytest


@pytest.mark.parametrize("file_path1, file_path2, format_name", [
    ('test/fixtures/file1.json', 'test/fixtures/file2.json', 'stylish'),
    ('test/fixtures/file1.yml', 'test/fixtures/file2.yml', 'stylish'),
    ('test/fixtures/file1.json', 'test/fixtures/file2.json', 'plain'),
    ('test/fixtures/file1.yml', 'test/fixtures/file2.yml', 'plain'),
])
def test_generate_diff_stylish_plain(file_path1, file_path2, format_name):
    result_stylish_path = 'test/fixtures/result_file_stylish.txt'
    result_plain_path = 'test/fixtures/result_file_plain.txt'
    match format_name:
        case 'stylish':
            with open(result_stylish_path) as stylish_result:
                result = stylish_result.read()
        case 'plain':
            with open(result_plain_path) as plain_result:
                result = plain_result.read()
    assert generate_diff(file_path1, file_path2, format_name) == result


@pytest.mark.parametrize("file_path1, file_path2", [
    ('test/fixtures/file1.json', 'test/fixtures/file2.json'),
    ('test/fixtures/file1.yml', 'test/fixtures/file2.yml'),
])
def test_generate_diff_json(file_path1, file_path2):
    assert isinstance(generate_diff(file_path1, file_path2, 'json'), str)
