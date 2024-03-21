NUMBER_OF_INDENTS = 4 * ' '
OFFSET_TO_THE_LEFT = 2 * ' '
START_DEPTH = 0
SIGN = {'added': '+ ', 'deleted': '- ', 'unchanged': '  '}


def transform_to_str(changeable_value, depth=START_DEPTH):
    if isinstance(changeable_value, dict):
        result = []
        close_indent = depth * NUMBER_OF_INDENTS + '}'
        str_indent = depth * NUMBER_OF_INDENTS + OFFSET_TO_THE_LEFT
        for key, value in changeable_value.items():
            if isinstance(value, dict):
                result.append(f'{str_indent}{SIGN["unchanged"]}{key}: '
                              f'{transform_to_str(value, depth + 1)}')
            else:
                result.append(f'{str_indent}{SIGN["unchanged"]}{key}: {value}')
        return '{\n' + '\n'.join(result) + f'\n{close_indent}'
    dict_changes = {
        bool: str(changeable_value).lower(),
        type(None): 'null',
    }
    return dict_changes.get(type(changeable_value), str(changeable_value))


def get_format_stylish(current_value, depth=START_DEPTH):
    result = []
    close_indent = depth * NUMBER_OF_INDENTS + '}'
    str_indent = depth * NUMBER_OF_INDENTS + OFFSET_TO_THE_LEFT
    for key, value in current_value.items():
        if isinstance(value, dict) and 'status' in value:
            match value['status']:
                case 'nested':
                    children = value['children']
                    result.append(f'{str_indent}{SIGN["unchanged"]}{key}: '
                                  f'{get_format_stylish(children, depth + 1)}')
                case 'added':
                    add_value = value["value"]
                    result.append(f'{str_indent}{SIGN["added"]}{key}: '
                                  f'{transform_to_str(add_value, depth + 1)}')
                case 'deleted':
                    del_value = value["value"]
                    result.append(f'{str_indent}{SIGN["deleted"]}{key}: '
                                  f'{transform_to_str(del_value, depth + 1)}')
                case 'changed':
                    old_value = value["old_value"]
                    new_value = value["new_value"]
                    result.append(f'{str_indent}{SIGN["deleted"]}{key}: '
                                  f'{transform_to_str(old_value, depth + 1)}\n'
                                  f'{str_indent}{SIGN["added"]}{key}: '
                                  f'{transform_to_str(new_value, depth + 1)}')
                case 'unchanged':
                    unch_value = value["value"]
                    result.append(f'{str_indent}{SIGN["unchanged"]}{key}: '
                                  f'{transform_to_str(unch_value, depth + 1)}')
    return '{\n' + '\n'.join(result) + f'\n{close_indent}'
