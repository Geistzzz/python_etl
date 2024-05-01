import logging
from config.project_config import log_name


class Logging:
    def __init__(self, level):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)


def init_logger():
    logger = Logging(20).logger

    # 构造handler
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(
        filename=log_name,
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
