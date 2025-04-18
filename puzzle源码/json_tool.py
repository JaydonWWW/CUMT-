import json


def read_json(path):
    '''
    读取json文件
    :param path:
    :return:
    '''
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()
            return data
    except:
        print("error", path)
        exit()


def save_json(data, path, debug=False):
    '''
    读取json文件
    :param data:
    :param path:
    :param debug
    :return:
    '''
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
        f.close()
    if debug:
        print(f"save to {path}!")
