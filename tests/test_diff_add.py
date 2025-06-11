from gendiff.diff import build_diff


def test_build_diff_add():
    diff = build_diff('tests/fixtures/add1.json', 'tests/fixtures/add2.json')
    expected = [
        {'key': 'key1', 'status': 'unchanged', 'value': 'val1'},
        {'key': 'key2', 'status': 'added', 'value': 'val2'}
    ]
    assert diff == expected
