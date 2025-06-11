def stylish(diff, depth=0):
    indent = '    ' * depth
    lines = ['{']
    for item in diff:
        key = item['key']
        status = item['status']

        if status == 'nested':
            children_str = stylish(item['children'], depth + 1)
            lines.append(f"{indent}    {key}: {children_str}")
        elif status == 'added':
            lines.append(f"{indent}  + {key}: {repr(item['value'])}")
        elif status == 'removed':
            lines.append(f"{indent}  - {key}: {repr(item['value'])}")
        elif status == 'unchanged':
            lines.append(f"{indent}    {key}: {repr(item['value'])}")
        elif status == 'changed':
            lines.append(f"{indent}  - {key}: {repr(item['old_value'])}")
            lines.append(f"{indent}  + {key}: {repr(item['new_value'])}")
    lines.append(f"{indent}}}")
    return '\n'.join(lines)
