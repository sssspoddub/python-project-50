from .parser import parse_file


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = ['{']
    for key in keys:
        if key not in data1:
            lines.append(f"  + {key}: {to_str(data2[key])}")
        elif key not in data2:
            lines.append(f"  - {key}: {to_str(data1[key])}")
        elif data1[key] != data2[key]:
            lines.append(f"  - {key}: {to_str(data1[key])}")
            lines.append(f"  + {key}: {to_str(data2[key])}")
        else:
            lines.append(f"    {key}: {to_str(data1[key])}")
    lines.append('}')
    return '\n'.join(lines)
