import os

from gendiff.diff import generate_diff


def test_generate_diff_yaml():
    base_path = os.path.join(os.path.dirname(__file__), 'test_data')
    file1 = os.path.join(base_path, 'file1.yml')
    file2 = os.path.join(base_path, 'file2.yml')
    expected_path = os.path.join(base_path, 'expected_diff.txt')

    with open(expected_path) as f:
        expected = f.read()

    diff = generate_diff(file1, file2)
    assert diff.strip() == expected.strip()


def test_generate_diff_json():
    base_path = os.path.join(os.path.dirname(__file__), 'test_data')
    file1 = os.path.join(base_path, 'file1.json')
    file2 = os.path.join(base_path, 'file2.json')
    expected_path = os.path.join(base_path, 'expected_diff.txt')

    with open(expected_path) as f:
        expected = f.read()

    diff = generate_diff(file1, file2)
    assert diff.strip() == expected.strip()
