from ..formatters.json import format_json
from ..formatters.plain import format_plain
from ..formatters.stylish import format_stylish
from ..scripts.diff_builder import build_diff_tree
from ..scripts.parser import parse_file

FORMATTERS = {
    'stylish': lambda diff: format_stylish(diff, depth=1),
    'plain': format_plain,
    'json': format_json,
}


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff_tree = build_diff_tree(data1, data2)

    if format_name not in FORMATTERS:
        raise ValueError(f'Unsupported format: {format_name}')

    formatter = FORMATTERS[format_name]
    result = formatter(diff_tree)

    if format_name == 'stylish':
        return '{\n' + result + '\n}'
    else:
        return result


def generate_diff_from_data(data1, data2, format_name='stylish'):
    diff_tree = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        inner = format_stylish(diff_tree, 1)
        return '{\n' + inner + '\n}'
    if format_name == 'plain':
        return format_plain(diff_tree)
    if format_name == 'json':
        return format_json(diff_tree)
    else:
        raise ValueError(f'Unsupported format: {format_name}')
