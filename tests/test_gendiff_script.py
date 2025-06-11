import sys

from gendiff.scripts.gendiff import generate_diff, main


def test_generate_diff_call(monkeypatch):
    result = generate_diff(
        'tests/test_data/file1.yml', 'tests/test_data/file2.yml')
    assert isinstance(result, str)
    assert 'host' in result


def test_main_prints(monkeypatch, capsys):
    testargs = ['gendiff', 'tests/test_data/file1.yml',
                'tests/test_data/file2.yml']
    monkeypatch.setattr(sys, 'argv', testargs)
    main()
    captured = capsys.readouterr()
    assert 'host' in captured.out
