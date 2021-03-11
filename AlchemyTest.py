from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DATABASE = {
    #    Тут можно использовать MySQL или другой драйвер
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'two',
    'password': '123',
    'database': 'my'
}

engine = create_engine(URL(**DATABASE))
DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = 'two_table'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)

    def __repr__(self):
        return "".format(self.code)
