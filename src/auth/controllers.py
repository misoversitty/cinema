from sqlalchemy.orm import Session
from sqlalchemy import select

from models import *
from config import engine

from utils import hash_password


class AuthenticationController:
    @staticmethod
    def authenticate(username: str, password: str):
        with Session(engine) as session:
            user = session.scalar(select(User)
                                  .where(User.username == username,
                                         User.password_hash == hash_password(password)))
            if user is not None:
                return {"sub": user.user_id}