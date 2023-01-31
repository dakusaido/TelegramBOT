from sqlalchemy import Column, Integer, String, Float

from utils.datbase import Base


class User(Base):
    __tablename__ = '__users__'

    id = Column(Integer, primary_key=True, unique=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    second_name = Column(String(12), nullable=False)
    first_name = Column(String(12), nullable=False)
