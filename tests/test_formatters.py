from gendiff.gendiff import generate_diff


def test_generate_diff():
    output = generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert output.startswith('{')
