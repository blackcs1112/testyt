import datetime
import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Test(SqlAlchemyBase):
    __tablename__ = 'test'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)# ид игрока
    name_test = sqlalchemy.Column(sqlalchemy.String, nullable=True)# по какому предмету
    number = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)# номер среди своих типо история(name_test) вариация 2(number)
    questions = orm.relation("Question", back_populates='tes')