def format_plain(diff_tree):
    lines = []

    def walk(node, path=""):
        node_type = node.get('type')
        key = node.get('key')

        current_path = f'{path}.{key}' if path else key

        if node_type == 'nested':
            for child in node.get("children", []):
                walk(child, current_path)

        elif node_type == 'unchanged':
            pass

        elif node_type == 'changed':
            old_val = format_value(node["old_value"])
            new_val = format_value(node["new_value"])
            lines.append(f"Property '{current_path}' was updated."
                         f" From {old_val} to {new_val}")

        elif node_type == 'added':
            value = format_value(node["value"])
            lines.append(f"Property '{current_path}'"
                         f" was added with value: {value}")

        elif node_type == 'removed':
            value = format_value(node["value"])
            lines.append(f"Property '{current_path}' was removed")

    for node in diff_tree:
        walk(node)

    return "\n".join(lines)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)
