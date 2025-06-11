import os

import pytest

from gendiff.parser import parse_file


def test_parse_yaml():
    filepath = os.path.join(os.path.dirname(__file__),
                            'test_data', 'file1.yml')
    data = parse_file(filepath)
    assert isinstance(data, dict)
    assert data.get('host') == 'hexlet.io'


def test_parse_json():
    filepath = os.path.join(os.path.dirname(__file__),
                            'test_data', 'file1.json')
    data = parse_file(filepath)
    assert isinstance(data, dict)
    assert data.get('host') == 'hexlet.io'


def test_unsupported_extension():
    filepath = os.path.join(os.path.dirname(__file__),
                            'test_data', 'file.unsupported')
    with pytest.raises(ValueError):
        parse_file(filepath)
