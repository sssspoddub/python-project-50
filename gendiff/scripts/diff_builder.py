ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
NESTED = 'nested'


def build_diff_tree(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key not in data1:
            diff.append({
                'type': ADDED,
                'key': key,
                'value': val2
            })
        elif key not in data2:
            diff.append({
                'type': REMOVED,
                'key': key,
                'value': val1
            })
        elif isinstance(val1, dict) and isinstance(val2, dict):
            diff.append({
                'type': NESTED,
                'key': key,
                'children': build_diff_tree(val1, val2)
            })
        elif val1 != val2:
            diff.append({
                'type': CHANGED,
                'key': key,
                'old_value': val1,
                'new_value': val2
            })
        else:
            diff.append({
                'type': UNCHANGED,
                'key': key,
                'value': val1
            })

    return diff
