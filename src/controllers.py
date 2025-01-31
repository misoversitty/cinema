from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Film
from modelSchemas import film_schema
from modelSchemas import films_schema
from config import engine


class FilmsController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(Film)
            films = session.execute(stmt).scalars()
            return films_schema.dump(films)
