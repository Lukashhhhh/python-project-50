NUMBER_OF_INDENTS = 4 * ' '
OFFSET_TO_THE_LEFT = 2 * ' '
CURRENT_DEPTH = 0
SIGN = {'added': '+', 'deleted': '-', 'unchanged': ' '}


def transform_to_str(value):
    format_ = {bool: str(value).lower(), type(None): 'null'}
    if type(value) in format_:
        return format_[type(value)]
    return str(value)


def get_format_stylish(current_value, depth=CURRENT_DEPTH):
    if not isinstance(current_value, dict):
        return f'{transform_to_str(current_value)}'
    result = []
    indent = depth * NUMBER_OF_INDENTS + '}'
    gen_indent = depth * NUMBER_OF_INDENTS + OFFSET_TO_THE_LEFT
    for key, value in current_value.items():
        if isinstance(value, dict) and 'status' in value:
            match value['status']:
                case 'nested' | 'unchanged':
                    children = value['children']
                    result.append(f'{gen_indent}{SIGN["unchanged"]} {key}: '
                                  f'{get_format_stylish(children, depth + 1)}')
                case 'added':
                    children = value['children']
                    result.append(f'{gen_indent}{SIGN["added"]} {key}: '
                                  f'{get_format_stylish(children, depth + 1)}')
                case 'deleted':
                    children = value['children']
                    result.append(f'{gen_indent}{SIGN["deleted"]} {key}: '
                                  f'{get_format_stylish(children, depth + 1)}')
                case 'changed':
                    child1, child2 = value["child1"], value["child2"]
                    result.append(f'{gen_indent}{SIGN["deleted"]} {key}: '
                                  f'{get_format_stylish(child1, depth + 1)}\n'
                                  f'{gen_indent}{SIGN["added"]} {key}: '
                                  f'{get_format_stylish(child2, depth + 1)}')
        else:
            result.append(f'{gen_indent}{SIGN["unchanged"]} {key}: '
                          f'{get_format_stylish(value, depth + 1)}')
    return '{\n' + '\n'.join(result) + f'\n{indent}'
