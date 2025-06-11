from gendiff.diff import build_diff
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def generate_diff(filepath1, filepath2, format_name='stylish'):
    diff = build_diff(filepath1, filepath2)

    if format_name == 'stylish':
        return stylish(diff)
    if format_name == 'plain':
        return plain(diff)
    raise ValueError(f"Unsupported format: {format_name}")
