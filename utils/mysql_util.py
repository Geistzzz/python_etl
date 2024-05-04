import pymysql
import config.project_config as config
from utils.logging_util import init_logger

logger = init_logger()


class MysqlUtil:
    def __init__(self,
                 host=config.metadata_host,
                 port=config.metadata_port,  # 一定是整型
                 user=config.metadata_user,
                 password=config.metadata_password,
                 charset=config.mysql_charset,
                 database=config.metadata_database  # 当前处理的是元数据
                 ):
        """
         创建MySql的连接
        """
        self.conn = pymysql.connect(
            host=host,
            port=port,  # 一定是整型
            user=user,
            password=password,
            charset=charset,
            database=database,  # 当前处理的是元数据
            autocommit=False
        )
        if self.conn:
            logger.info(
                f"构建完成到{config.metadata_host}：{config.metadata_port}的数据库「{config.metadata_database}」连接成功...")
            pass

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        if self.conn:
            self.conn.close()
            self.conn = None

    def query(self, sql):
        """
        :param sql:需要执行查询的语句
        :return:
        """
        # 获取游标
        cursor = self.conn.cursor()
        # 执行查询sql语句
        cursor.execute(sql)
        # 获取查询的结果
        result = cursor.fetchall()
        # 关闭游标
        cursor.close()
        logger.info(result)
        # 返回结果
        return result

    def select_db(self, db_name):
        """
        切换数据库
        :param db_name:
        :return:
        """
        self.conn.select_db(db_name)

    def execute_with_commit(self, sql):
        """
        直接执行一条SQL语句，不处理返回值
        确保执行的SQL语句提交到数据库
        :param sql:
        :return:
        """
        # 获取游标
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql)
        # 确保提交到数据库
        if not self.conn.get_autocommit():
            self.conn.commit()

        # 关闭游标
        self.conn.close()

    def execute_without_commit(self, sql):
        # 获取游标
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql)
        logger.debug(f"执行了一条SQL:{sql}")

        # 关闭游标
        self.conn.close()

    def check_table_exist(self, db_name, table_name):
        """
        :param db_name:
        :param table_name:
        :return:
        """
        # 切换数据库
        self.select_db(db_name)
        # 查询所有表
        results = self.query('show tables')
        # 判断查询的表是否在结果中
        return (table_name,) in results

    def creat_table(self, db_name, table_name, create_cols):
        """
        检查表是否存在
        :param db_name:
        :param table_name:
        :param create_cols:
        :return:
        """
        # if not self.check_table_exist(db_name, table_name):
        sql = f"create table {table_name}({create_cols})"
        # 执行建表语句
        self.select_db(db_name)
        self.execute_with_commit(sql)
        logger.info(f"在数据库中：{db_name}中创建了表：{table_name}完成。建表语句是{create_cols}")
        #     pass
        # else:
        #     logger.info(f"在数据库中：{db_name}中：表{table_name}已经存在，创建表的操作跳过")

        # pass


def get_processed_files(db_util,
                        db_name=config.target_database,
                        table_name=config.metadata_file_monitor_table_name,
                        create_cols=config.metadata_file_monitor_creat_cols):
    """
    获取处理过的文件名
    :param db_util:
    :param db_name:
    :param table_name: file_monitor
    :param create_cols: 建表语句中的列名和类型
    :return: 处理过的文件路径组成的列表
    """
    db_util.select_db(db_name)

    if not db_util.check_table_exist(db_name, table_name):
        db_util.create_table(db_name, table_name, create_cols)
    else:
        logger.debug(f"{table_name}存在，跳过建表语句")
    results = db_util.query(f"select file_name from {table_name}")
    file_names = []
    for result in results:
        file_names.append(result[0])

    return file_names


if __name__ == '__main__':
    # 连接到原数据库
    mysql_util = MysqlUtil()
    # mysql_util.query('select * from test;')
    # mysql_util.select_db('retail')
    mysql_util.query('SELECT database();')
    # mysql_util.close()

    # 连接到目的地数据库
    # target_mysql_util = MysqlUtil(
    #     host=config.target_host,
    #     port=config.target_port,
    #     user=config.target_user,
    #     password=config.target_password,
    #     database=config.target_database)
    if not mysql_util.check_table_exist('metadata', 'test5'):
        mysql_util.creat_table('metadata', 'test5', 'name varchar(255),age int')

    # mysql_util.close()
