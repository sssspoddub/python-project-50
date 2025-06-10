def build_diff_dict(data1: dict, data2: dict) -> str:
    def to_str(value):
        if isinstance(value, bool):
            return str(value).lower()
        return value

    keys = sorted(data1.keys() | data2.keys())
    lines = ['{']
    for key in keys:
        if key in data1 and key not in data2:
            lines.append(f'  - {key}: {to_str(data1[key])}')
        elif key not in data1 and key in data2:
            lines.append(f'  + {key}: {to_str(data2[key])}')
        else:
            if data1[key] == data2[key]:
                lines.append(f'    {key}: {to_str(data1[key])}')
            else:
                lines.append(f'  - {key}: {to_str(data1[key])}')
                lines.append(f'  + {key}: {to_str(data2[key])}')
    lines.append('}')
    return '\n'.join(lines) + '\n'
