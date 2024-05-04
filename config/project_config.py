import time

log_root_path = "/Users/mac/Documents/Pythonproject/python_etl/"
log_filename = f'pyetl-{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}.log'

level = 10

############ MySQLUtil 配置 #####################
mysql_charset = "utf8"

################## 源数据库配置 ################
metadata_host = "localhost"
metadata_user = "root"
metadata_password = "Zc.1319119251"
metadata_port = 3306
metadata_database = "metadata"

################## 目标数据库配置 ################
target_host = "localhost"
target_user = "root"
target_password = "Zc.1319119251"
target_port = 3306
target_database = "retail"

#########################################################
# 文件监控表名称，存储哪些文件被处理过
metadata_file_monitor_table_name = "file_monitor"
# 文件监控表，建表语句的列信息
metadata_file_monitor_creat_cols = """
    id INT PRIMARY KEY AUTO_INCREMENT,
    file_name VARCHAR(255) UNIQUE NOT NULL COMMENT "被处理的文件名称",
    process_lines INT COMMENT '本文件中有多少条数据被处理,
    proces_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '处理时间'
"""
######################json相关文件配置################
json_data_root_path = "D:\\retail\\retail\\"
