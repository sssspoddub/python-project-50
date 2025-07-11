def format_stylish(diff_tree, depth=0):
    indent = '    ' * depth
    unchanged_indent = '    '
    removed_indent = '  - '
    added_indent = '  + '

    lines = []

    for node in diff_tree:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children_lines = format_stylish(node['children'], depth)
            lines.append(f"{indent}{key}: {{")
            if '\n' in children_lines:
                indent_children = '\n'.join(
                    f"{'    ' * depth}{line}"
                    for line in children_lines.split('\n')
                )
                lines.append(indent_children)
            else:
                lines.append(f"{'    ' * (depth + 1)}{children_lines}")
            lines.append(f"{indent}}}")

        elif node_type == 'changed':
            old_val = format_value(node['old_value'], depth + 1)
            new_val = format_value(node['new_value'], depth + 1)
            if old_val == new_val:
                lines.append(f'{unchanged_indent}{key}: {old_val}')
                lines.append(f"{unchanged_indent}{key}: {new_val}")
            else:
                lines.append(f"{removed_indent}{key}: {old_val}")
                lines.append(f"{added_indent}{key}: {new_val}")

        elif node_type == 'added':
            val = format_value(node['value'], depth + 1)
            lines.append(f"{added_indent}{key}: {val}")

        elif node_type == 'removed':
            val = format_value(node['value'], depth + 1)
            lines.append(f"{removed_indent}{key}: {val}")

        elif node_type == 'unchanged':
            val = format_value(node['value'], depth + 1)
            lines.append(f"{unchanged_indent}{key}: {val}")

    return '\n'.join(lines)


def format_value(value, depth=0):
    if isinstance(value, dict):
        lines = []

        for k, v in sorted(value.items()):
            formatted_v = format_value(v, depth + 1)
            lines.append(f"{'    ' * depth}{k}: {formatted_v}")

        if not lines:
            return '{}'

        content = '\n'.join(lines)
        indent = '    ' * (depth - 1)
        return f"{{\n{content}\n{indent}}}"

    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif value == '':
        return ''
    else:
        return str(value)
