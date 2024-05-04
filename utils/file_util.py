import os


def get_file_list(path, recursive=False):
    """
    获取指定路径下所有的文件名(绝对路径)
    :param path:指定的路径
    :param recursive:是否递归
    :return:获取到的文件列表
    """
    dir_names = os.listdir(path)
    file_list = []
    for dir_name in dir_names:
        absolute_path = f'{path}/{dir_name}'
        if not os.path.isdir(absolute_path):
            file_list.append(absolute_path)
        else:
            if recursive:
                file_list += get_file_list(absolute_path, recursive=recursive)
    return file_list


def get_bew_by_compare_list(a_list, b_list):
    """
    差集
    :param a_list:
    :param b_list:
    :return:
    """
    return list(set(a_list) - set(b_list))
