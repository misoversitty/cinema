from sqlalchemy.orm import Session
from sqlalchemy import select

from models import *
from modelSchemas import *
from config import engine


class FilmsController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(Film)
            films = session.execute(stmt).scalars()
            return films_schema.dump(films)


class FilmSessionsController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(FilmSession)
            filmSessions = session.execute(stmt).scalars()
            return filmSessions_schema.dump(filmSessions)


class OrdersController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(Order)
            orders = session.execute(stmt).scalars()
            return orders_schema.dump(orders)