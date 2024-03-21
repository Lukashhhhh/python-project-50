def build_diff_tree(data1, data2):
    result = {}
    keys = data1.keys() | data2.keys()
    for key in keys:
        if key not in data1:
            result[key] = {
                'status': 'added',
                'value': data2[key]}
        elif key not in data2:
            result[key] = {
                'status': 'deleted',
                'value': data1[key]}
        elif data1[key] == data2[key]:
            result[key] = {
                'status': 'unchanged',
                'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'status': 'nested',
                'children': build_diff_tree(data1[key], data2[key])}
        else:
            result[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
    sorted_diff = dict(sorted(result.items()))
    return sorted_diff
