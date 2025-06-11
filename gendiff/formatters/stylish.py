def to_str(value, depth):
    indent = '    ' * depth
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f'{indent}    {k}: {to_str(v, depth + 1)}')
        return '{\n' + '\n'.join(lines) + f'\n{indent}}}'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def stylish(diff, depth=0):
    indent = '    ' * depth
    lines = []

    for item in diff:
        key = item['key']
        status = item['status']

        if status == 'added':
            lines.append(
                f'{indent}  + {key}: {to_str(item["value"], depth + 1)}')
        elif status == 'removed':
            lines.append(
                f'{indent}  - {key}: {to_str(item["value"], depth + 1)}')
        elif status == 'unchanged':
            lines.append(
                f'{indent}    {key}: {to_str(item["value"], depth + 1)}')
        elif status == 'changed':
            lines.append(
                f'{indent}  - {key}: {to_str(item["old_value"], depth + 1)}')
            lines.append(
                f'{indent}  + {key}: {to_str(item["new_value"], depth + 1)}')
        elif status == 'nested':
            children_str = stylish(item['children'], depth + 1)
            lines.append(f'{indent}    {key}: {children_str}')
    return '{\n' + '\n'.join(lines) + f'\n{indent}}}'
