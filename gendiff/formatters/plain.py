def transform_to_str(value):
    dict_changes = {
        bool: str(value).lower(),
        type(None): 'null',
        str: f"'{value}'",
        dict: '[complex value]'
    }
    return dict_changes.get(type(value), str(value))


def get_format_plain(current_value, path=''):
    result = []
    for key, value in current_value.items():
        match value['status']:
            case 'added':
                added_value = value["value"]
                result.append(f"Property '{path}{key}' was added with "
                              f"value: {transform_to_str(added_value)}")
            case 'deleted':
                result.append(f"Property '{path}{key}' was removed")
            case 'changed':
                old_value = value["old_value"]
                new_value = value["new_value"]
                result.append(f"Property '{path}{key}' was updated. "
                              f"From {transform_to_str(old_value)} to "
                              f"{transform_to_str(new_value)}")
            case 'nested':
                children = value['children']
                result.append(get_format_plain(children, f'{path}{key}.'))
    return '\n'.join(result)
