def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain(diff, path=''):
    lines = []

    for node in diff:
        key = node['key']
        status = node['status']
        property_path = f"{path}.{key}" if path else key

        if status == 'nested':
            lines.append(plain(node['children'], property_path))
        elif status == 'added':
            val = to_str(node['value'])
            lines.append(
                f"Property '{property_path}' was added with value: {val}"
            )
        elif status == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif status == 'changed':
            old_val = to_str(node['old_value'])
            new_val = to_str(node['new_value'])
            lines.append(
                f"Property '{property_path}' was updated. "
                f"From {old_val} to {new_val}"
            )

    return '\n'.join(lines)
