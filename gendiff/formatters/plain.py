def transform_to_str(value):
    dict_changes = {
        bool: str(value).lower(),
        type(None): 'null',
        str: f"'{value}'",
        dict: '[complex value]'
    }
    return dict_changes.get(type(value), str(value))


def get_format_plain(current_value, path=None):
    result = []
    for key, value in current_value.items():
        # Не знаю насколько корректно и читаемо писать такие условия
        # Здесь вроде читаемо, но можно расписать если нужно
        # Еще как вариант сделать функцию, но не знаю нужно ли
        path = path + f'.{key}' if path else key
        if isinstance(current_value, dict) and 'status' in value:
            match value['status']:
                case 'added':
                    added_value = value["value"]
                    result.append(f"Property '{path}' was added with "
                                  f"value: {transform_to_str(added_value)}")
                case 'deleted':
                    result.append(f"Property '{path}' was removed")
                case 'changed':
                    old_value = value["old_value"]
                    new_value = value["new_value"]
                    result.append(f"Property '{path}' was updated. "
                                  f"From {transform_to_str(old_value)} to "
                                  f"{transform_to_str(new_value)}")
                case 'nested':
                    children = value['children']
                    result.append(get_format_plain(children, path))
            # Здесь аналогично, но читаемость хуже
            path = path.replace(f'{key}', '') if path == key else path.replace(
                f'.{key}', '')
        else:
            return transform_to_str(current_value)
    return '\n'.join(result)
