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

    @staticmethod
    def read_one(film_id: int):
        with Session(engine) as session:
            stmt = select(Film).where(Film.film_id == film_id)
            film = session.execute(stmt).scalar()
            return film_schema.dump(film)


class FilmSessionsController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(FilmSession)
            filmSessions = session.execute(stmt).scalars()
            return filmSessions_schema.dump(filmSessions)

    @staticmethod
    def read_one(filmsession_id: int):
        with Session(engine) as session:
            stmt = select(FilmSession).where(FilmSession.session_id == filmsession_id)
            filmsession = session.execute(stmt).scalar()
            return filmSession_schema.dump(filmsession)


class OrdersController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(Order)
            orders = session.execute(stmt).scalars()
            return orders_schema.dump(orders)

    @staticmethod
    def read_one(order_id: int):
        with Session(engine) as session:
            stmt = select(Order).where(Order.order_id == order_id)
            order = session.execute(stmt).scalar()
            return order_schema.dump(order)

    @staticmethod
    def create(*args, **kwargs):
        order = kwargs.get("body")
        data = order_schema.load(order)
        customer_id = data.get("customer_id")
        sessions_args = data.get("sessions")

        with Session(engine) as session:
            new_order = Order(customer_id=customer_id)
            for filmsession_args in sessions_args:
                session_id = filmsession_args.get("session").get("session_id")
                count = filmsession_args.get("count")
                association = OrderSessionAssociation(count=count)
                stmt = select(FilmSession).where(FilmSession.session_id == session_id)
                association.session = session.execute(stmt).scalar()
                new_order.sessions.append(association)
            session.add(new_order)
            session.commit()


class CustomersController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(Customer)
            customers = session.execute(stmt).scalars()
            return customers_schema.dump(customers)

    @staticmethod
    def read_one(customer_id: int):
        with Session(engine) as session:
            stmt = select(Customer).where(Customer.customer_id == customer_id)
            customer = session.execute(stmt).scalar()
            return customer_schema.dump(customer)

    @staticmethod
    def create(*args, **kwargs):
        customer = kwargs.get("body")
        data = customer_schema.load(customer)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        middle_name = data.get("middle_name")
        with Session(engine) as session:
            new_customer = Customer(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name)
            session.add(new_customer)
            session.commit()
        return "", 201
