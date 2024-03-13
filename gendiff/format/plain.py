def get_formated_data(data):
    format_ = {
        bool: str(data).lower(),
        type(None): 'null',
    }
    if type(data) in format_:
        return format_[type(data)]
    return f"'{data}'"


def get_formated_plain(data):
    def iner_(current_value, path=[]):
        if not isinstance(current_value, dict):
            return get_formated_data(current_value)
        result = []
        for key, value in current_value.items():
            if isinstance(current_value, dict) and 'status' in value:
                path.append(key)
                current_path = '.'.join(path)
                match value['status']:
                    case 'added':
                        children = value['children']
                        result.append(
                            f"Property '{current_path}' was added with "
                            f"value: {iner_(children, path)}"
                        )
                        path.pop()
                    case 'deleted':
                        result.append(f"Property '{current_path}' was removed")
                        path.pop()
                    case 'changed':
                        child1, child2 = value['child1'], value['child2']
                        result.append(
                            f"Property '{current_path}' was updated. "
                            f"From {iner_(child1)} to {iner_(child2)}"
                        )
                        path.pop()
                    case 'nested':
                        children = value['children']
                        result.append(iner_(children, path))
                        path.pop()
                    case 'unchanged':
                        path.pop()
                        continue
            else:
                return '[complex value]'
        return '\n'.join(result)
    return iner_(data)
