import logging
from config.project_config import log_root_path, log_filename, level


class Logging:
    def __init__(self, level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)


def init_logger():
    logger = Logging(level).logger

    # 避免重复输出日志
    if logger.handlers:
        return logger

    # 构造handler
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(
        filename=log_root_path + log_filename,
        mode="a",
        encoding="UTF-8"
    )
    # 设置一个format输出格式
    fmt = logging.Formatter("%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s")
    # 将格式设置到文件的handler中
    file_handler.setFormatter(fmt)
    stream_handler.setFormatter(fmt)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger
