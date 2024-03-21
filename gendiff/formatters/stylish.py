NUMBER_OF_INDENTS = 4 * ' '
OFFSET_TO_THE_LEFT = 2 * ' '
START_DEPTH = 0
SIGN = {'added': '+ ', 'deleted': '- ', 'unchanged': '  '}


def dict_to_str(dict_value: dict, depth):
    result = []
    close_indent = depth * NUMBER_OF_INDENTS + '}'
    str_indent = depth * NUMBER_OF_INDENTS + OFFSET_TO_THE_LEFT
    for key, value in dict_value.items():
        if isinstance(value, dict):
            result.append(f'{str_indent}{SIGN["unchanged"]}{key}: {dict_to_str(value, depth + 1)}')
        else:
            result.append(f'{str_indent}{SIGN["unchanged"]}{key}: {value}')
    return '{\n' + '\n'.join(result) + f'\n{close_indent}'


def transform_to_str(value, depth=START_DEPTH):
    if isinstance(value, dict):
        return dict_to_str(value, depth)
    format_ = {bool: str(value).lower(),
               type(None): 'null',
              }
    str_value = format_.get(type(value))
    if str_value:
        return str_value
    return str(value)


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
                    children = value['children']
                    result.append(f'{str_indent}{SIGN["added"]}{key}: '
                                  f'{transform_to_str(children, depth + 1)}')
                case 'deleted':
                    children = value['children']
                    result.append(f'{str_indent}{SIGN["deleted"]}{key}: '
                                  f'{transform_to_str(children, depth + 1)}')
                case 'changed':
                    child1, child2 = value["child1"], value["child2"]
                    result.append(f'{str_indent}{SIGN["deleted"]}{key}: '
                                  f'{transform_to_str(child1, depth + 1)}\n'
                                  f'{str_indent}{SIGN["added"]}{key}: '
                                  f'{transform_to_str(child2, depth + 1)}')
                case 'unchanged':
                    children = value['children']
                    result.append(f'{str_indent}{SIGN["unchanged"]}{key}: '
                                   f'{transform_to_str(children, depth + 1)}')
    return '{\n' + '\n'.join(result) + f'\n{close_indent}'
