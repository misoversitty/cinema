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

    @staticmethod
    def read_one(order_id: int):
        with Session(engine) as session:
            stmt = select(Order).where(Order.order_id == order_id)
            order = session.execute(stmt).scalar()
            return order_schema.dump(order)


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
