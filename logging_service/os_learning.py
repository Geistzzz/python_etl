import os

files_ = os.listdir("/Users/mac/Documents/data/pyetl_data_logs/JSON/")


# 当前代码是可以直接读取指定目录下的文件
# 如果当前目录下有别的文件夹，这个代码是无法满足的

# print(files)


def read_dir(dir_):
    result = []
    files = os.listdir(dir_)
    for file in files:
        f = dir_ + '/' + file
        if os.path.isdir(f):  # 判断指定的路径是文件还是目录
            # 当前的file名是目录
            result += read_dir(f)
        else:
            result.append(f)
    return result


print(read_dir("/Users/mac/Documents/data/pyetl_data_logs/JSON"))

# 目前使用的os库里面的函数
os.listdir()
os.path.isdir()
os.getcwd()
os.path.dirname()  # 获取指定路径的上一级目录
os.path.basename()  # 获取指定路径对应的文件名（相对路径）
os.mkdir()

