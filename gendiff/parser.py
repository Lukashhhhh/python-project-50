def get_sorted_diff(data1, data2):
    result = {}
    keys = data1.keys() | data2.keys()
    for key in keys:
        if key not in data1:
            result[key] = {
                'status': 'added',
                'children': data2[key]}
        elif key not in data2:
            result[key] = {
                'status': 'deleted',
                'children': data1[key]}
        elif data1[key] == data2[key]:
            result[key] = {
                'status': 'unchanged',
                'children': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'status': 'nested',
                'children': get_sorted_diff(data1[key], data2[key])}
        else:
            result[key] = {
                'status': 'changed',
                'child1': data1[key],
                'child2': data2[key]
            }
    sorted_diff = dict(sorted(result.items()))
    return sorted_diff
