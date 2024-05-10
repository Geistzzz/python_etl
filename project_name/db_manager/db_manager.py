import functools

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker


class DbManager:
    __config = None
    __instance = None
    __engine = None

    def __new__(cls, config, *args, **kwargs):
        if not cls.__instance:
            cls.__config = config
            cls.__instance = object.__new__(cls)
        return cls.__instance

    @staticmethod
    def db_session(user=None, password=None, db=None, host=None, port=None):
        def method(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                e = DbManager.gen_engine(user, password, db, host, port)
                s = DbManager.session()
                m = DbManager.meta()
                print(f"Function <{func.__name__}> use Mysql:{e}")
                res = func(session=s, meta=m, *args, **kwargs)
                s.commit()
                s.close()
                DbManager.gen_engine().dispose()
                return res

            return wrapper

        return method()

    @staticmethod
    def gen_engine(user=None, password=None, db=None, host=None, port=None):
        if (not DbManager.__engine) or all(map(lambda x: x is not None, [user, password, db, host, port])):
            engine = create_engine(f"""mysql+pymysql://{user}:{password}@{host}:{port}/{db}""", pool_pre_ping=True,
                                   max_overflow=10, pool_size=20, pool_recycle=600)
            DbManager.__engine = engine
        return DbManager.__engine

    @staticmethod
    def session(user=None, password=None, db=None, host=None, port=None) -> Session:
        s = sessionmaker(bind=DbManager.gen_engine(user, password, db, host, port))
        return s()

    @staticmethod
    def meta(user=None, password=None, db=None, host=None, port=None) -> MetaData:
        m = MetaData()
        m.reflect(bind=DbManager.gen_engine(user, password, db, host, port))
        return m
