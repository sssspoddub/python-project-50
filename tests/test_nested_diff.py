from pathlib import Path

from gendiff import generate_diff_from_data
from gendiff.scripts.parser import parse_file

FIXTURES_PATH = Path(__file__).parent / 'test_data'


def read_file(path):
    with open(path, 'r') as f:
        return f.read()


def test_gendiff_json_nested():
    data1 = parse_file(FIXTURES_PATH / 'file1.json')
    data2 = parse_file(FIXTURES_PATH / 'file2.json')

    result = generate_diff_from_data(data1, data2)
    expected = read_file(FIXTURES_PATH / 'expected_result_stylish.txt').strip()
    assert result.strip() == expected
