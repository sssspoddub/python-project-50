from gendiff.diff import build_diff
from gendiff.formatters.stylish import stylish


def generate_diff(filepath1, filepath2, format_name='stylish'):
    diff = build_diff(filepath1, filepath2)
    if format_name == 'stylish':
        return stylish(diff)
    return stylish(diff)
