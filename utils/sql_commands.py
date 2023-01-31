from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, desc

from utils.datbase import session
from utils.schemas import User


def register_user(tg_id: int, first_name: str, second_name: str):
    session.connection()
    user = User(
        tg_id=tg_id,
        first_name=first_name,
        second_name=second_name
    )
    session.add(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()


def delete_user(tg_id):
    user = session.query(User).filter(User.tg_id == tg_id).one()
    session.delete(user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()


def select_users():
    users = session.query(User).all()
    return users
