from gendiff.read_file import get_file_data


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
    data_file1 = get_file_data(file_path1)
    data_file2 = get_file_data(file_path2)
    return get_diff(data_file1, data_file2)
