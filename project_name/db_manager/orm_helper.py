import pandas as pd
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import Session, Query

from project_name.db_manager.db_manager import DbManager
from project_name.utils import *


def multi_filter(table: Table, **kwargs) -> Query:
    """

    :param table:
    :param kwargs:
    :return:
    """
    if table is None:
        print(f"Error: Table is None!")
    session: Session = DbManager.session()
    tb_session: Query = session.query(table)
    for arg in kwargs:
        if not kwargs.get(arg, False):
            continue
        if arg.lower() in table.columns:
            tb_session = tb_session.filter(table.columns.get(arg.lower()) == kwargs.get(arg))
        elif arg.upper() in table.columns:
            tb_session = tb_session.filter(table.columns.get(arg.upper()) == kwargs.get(arg))
        else:
            pass

    return tb_session


def multi_groupBy(tb_session: Query, table: Table, constants: list):
    """
    :param tb_session:
    :param table:
    :param constants:
    :return:
    """
    for arg in constants:
        if arg.lower() in table.columns:
            tb_session = tb_session.group_by(table.columns.get(arg.lower()))
        elif arg.upper() in table.columns:
            tb_session = tb_session.group_by(table.columns.get(arg.upper()))
        else:
            pass
    return tb_session
