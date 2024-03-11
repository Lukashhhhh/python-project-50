NUMBER_OF_INDENTS = 4 * ' '
OFFSET_TO_THE_LEFT = 2 * ' '
CURRENT_DEPTH = 0
OPERATOR = {'added': '+', 'deleted': '-', 'unchanged': ' '}


def get_formated_data(data):
    format_ = {
        bool: str(data).lower(),
        type(None): 'null'
    }
    if type(data) in format_:
        return format_[type(data)]
    return data


def get_formated_stylish(data):
    def iner_(current_value, depth=CURRENT_DEPTH):
        if not isinstance(current_value, dict):
            # current_value = get_formated_data(current_value)
            return f'{get_formated_data(current_value)}'
        result = '{'
        gen_indent = depth * NUMBER_OF_INDENTS + OFFSET_TO_THE_LEFT
        for key, value in current_value.items():
            if isinstance(value, dict) and 'status' in value:
                match value['status']:
                    case 'nested' | 'unchanged':
                        result += (f'\n{gen_indent}'
                                   f'{OPERATOR["unchanged"]} {key}: ')
                    case 'added':
                        result += f'\n{gen_indent}{OPERATOR["added"]} {key}: '
                    case 'deleted':
                        result += f'\n{gen_indent}{OPERATOR["deleted"]} {key}: '
                    case 'changed':
                        # child1 and child2 - keys indicating the difference
                        # with a common primary key
                        child1, child2 = value["child1"], value["child2"]
                        result += (
                            f'\n{gen_indent}{OPERATOR["deleted"]} {key}: '
                            f'{iner_(child1, depth + 1)}\n'
                            f'{gen_indent}{OPERATOR["added"]} {key}: '
                            f'{iner_(child2, depth + 1)}')
                        continue
                children = value['children']
                result += iner_(children, depth + 1)
            else:
                result += (f'\n{gen_indent}{OPERATOR["unchanged"]} {key}: '
                           f'{iner_(value, depth + 1)}')
        return result + ('\n' + depth * NUMBER_OF_INDENTS + '}')
    return iner_(data)
