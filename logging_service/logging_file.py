import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(r"test.log")

# 设置logger输出格式
fmt = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
)
file_handler.setFormatter(fmt)
# 组合
logger.addHandler(file_handler)