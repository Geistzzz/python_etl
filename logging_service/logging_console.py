import logging

# 构造logger对象
logger = logging.getLogger()

# 构造stream_handler
stream_handler = logging.StreamHandler()

# 设置logger输出格式
fmt = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
)
stream_handler.setFormatter(fmt)
# 组合
logger.addHandler(stream_handler)
