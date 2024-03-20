def transform_to_str(value):
    format_ = {bool: str(value).lower(), type(None): 'null',
               str: f"'{value}'", dict: '[complex value]'}
    str_value = format_.get(type(value))
    if str_value:
        return str_value
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
                                  f"value: {transform_to_str(children)}")
                case 'deleted':
                    result.append(f"Property '{current_path}' was removed")
                case 'changed':
                    child1, child2 = value['child1'], value['child2']
                    result.append(f"Property '{current_path}' was updated. "
                                  f"From {transform_to_str(child1)} to "
                                  f"{transform_to_str(child2)}")
                case 'nested':
                    children = value['children']
                    result.append(get_format_plain(children, path))
            path.pop()
        else:
            return transform_to_str(current_value)
    return '\n'.join(result)
