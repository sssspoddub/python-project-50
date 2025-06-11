from gendiff.diff import build_diff
from gendiff.formatters.stylish import stylish


def test_stylish_format():
    diff = build_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    result = stylish(diff)
    assert 'common' in result
    assert 'group1' in result
    assert 'added' not in result
    assert isinstance(result, str)
