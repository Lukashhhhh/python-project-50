def transform_to_str(value):
    format_ = {bool: str(value).lower(), type(None): 'null', str: f"'{value}'"}
    if type(value) in format_:
        return format_[type(value)]
    return str(value)


def get_format_plain(current_value, path=[]):
    if not isinstance(current_value, dict):
        return transform_to_str(current_value)
    result = []
    for key, value in current_value.items():
        if isinstance(current_value, dict) and 'status' in value:
            path.append(key)
            current_path = '.'.join(path)
            match value['status']:
                case 'added':
                    children = value['children']
                    result.append(f"Property '{current_path}' was added with "
                                  f"value: {get_format_plain(children, path)}")
                case 'deleted':
                    result.append(f"Property '{current_path}' was removed")
                case 'changed':
                    child1, child2 = value['child1'], value['child2']
                    result.append(f"Property '{current_path}' was updated. "
                                  f"From {get_format_plain(child1)} to "
                                  f"{get_format_plain(child2)}")
                case 'nested':
                    children = value['children']
                    result.append(get_format_plain(children, path))
            path.pop()
        else:
            return '[complex value]'
    return '\n'.join(result)
