from gendiff.diff import build_diff


def test_build_diff_empty_dicts():
    diff = build_diff('tests/fixtures/empty1.json', 'tests/fixtures/empty2.json')
    assert diff == []
