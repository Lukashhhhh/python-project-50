import json


def get_diff(data1, data2):
    result = '{\n'
    keys_list = sorted(data1.keys() | data2.keys())
    for key in keys_list:
        if data1.get(key) == data2.get(key):
            result += f'    {key}: {data1.get(key)}\n'
        elif data1.get(key) is None:
            result += f'  + {key}: {data2.get(key)}\n'
        elif data2.get(key) is None:
            result += f'  - {key}: {data1.get(key)}\n'
        else:
            result += (
                f'  - {key}: {data1.get(key)}\n'
                f'  + {key}: {data2.get(key)}\n'
                )
    result += '}'
    return result


def generate_diff(file_path1, file_path2):
    with open(file_path1) as data1, open(file_path2) as data2:
        file1 = json.load(data1)
        file2 = json.load(data2)
    return get_diff(file1, file2)
