from gendiff.diff import build_diff


def test_build_diff():
    diff = build_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert isinstance(diff, list)
    keys = [item['key'] for item in diff]
    assert 'common' in keys
    assert 'group1' in keys
