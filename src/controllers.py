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
            return films_schema.dump(films), 200

    @staticmethod
    def read_one(film_id: int):
        with Session(engine) as session:
            stmt = select(Film).where(Film.film_id == film_id)
            film = session.execute(stmt).scalar()
            return film_schema.dump(film), 200


class FilmSessionsController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(FilmSession)
            filmSessions = session.execute(stmt).scalars()
            return filmSessions_schema.dump(filmSessions), 200

    @staticmethod
    def read_one(filmsession_id: int):
        with Session(engine) as session:
            stmt = select(FilmSession).where(FilmSession.session_id == filmsession_id)
            filmsession = session.execute(stmt).scalar()
            return filmSession_schema.dump(filmsession), 200


class OrdersController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(Order)
            orders = session.execute(stmt).scalars()
            return orders_schema.dump(orders), 200

    @staticmethod
    def read_one(order_id: int):
        with Session(engine) as session:
            stmt = select(Order).where(Order.order_id == order_id)
            order = session.execute(stmt).scalar()
            return order_schema.dump(order), 200

    @staticmethod
    def create(*args, **kwargs):
        data = kwargs.get("body")
        order_args = order_schema.load(data)
        customer_id = order_args.get("customer_id")
        tickets_args = order_args.get("tickets")

        with Session(engine) as session:
            new_order = Order(customer_id=customer_id)
            for ticket_args in tickets_args:
                ticket_id = ticket_args.get("ticket_id")
                stmt = select(Ticket).where(Ticket.ticket_id == ticket_id)
                ticket = session.execute(stmt).scalar()
                new_order.tickets.append(ticket)
            session.add(new_order)
            session.commit()
        return "", 201


class CustomersController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(Customer)
            customers = session.execute(stmt).scalars()
            return customers_schema.dump(customers), 200

    @staticmethod
    def read_one(customer_id: int):
        with Session(engine) as session:
            stmt = select(Customer).where(Customer.customer_id == customer_id)
            customer = session.execute(stmt).scalar()
            return customer_schema.dump(customer), 200

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

class TicketsController:
    @staticmethod
    def read_all():
        with Session(engine) as session:
            stmt = select(Ticket)
            tickets = session.execute(stmt).scalars()
            return tickets_schema.dump(tickets), 200

    @staticmethod
    def read_one(ticket_id: int):
        with Session(engine) as session:
            stmt = select(Ticket).where(Ticket.ticket_id == ticket_id)
            ticket = session.execute(stmt).scalar()
            return ticket_schema.dump(ticket), 200
