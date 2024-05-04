"""
json文件处理
"""
from utils.logging_util import init_logger
from utils.file_util import get_file_list, get_bew_by_compare_list
from utils.mysql_util import MysqlUtil, get_processed_files
import config.project_config as config

logger = init_logger()
logger.info("读取JSON数据处理，程序开始执行了......")
# 1 获取所有文件名
file_list = get_file_list(path=config.json_data_root_path, recursive=False)
logger.info(f"判断json文件夹，发现有如下文件: {file_list}")
# 2 获取已经处理的
## 2.1 实例化MySQLUtil对象
db_util = MysqlUtil()
## 2.2获取处理过的
processed_files = get_processed_files(db_util)
# 3 获取等待处理的
need_to_process_files = get_bew_by_compare_list(file_list, processed_files)
