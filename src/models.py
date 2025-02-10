from datetime import datetime
from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"
    customer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    middle_name: Mapped[str] = mapped_column(String)

    orders: Mapped[List["Order"]] = relationship(back_populates="customer")


class Film(Base):
    __tablename__ = "films"
    film_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    sessions: Mapped[List["FilmSession"]] = relationship(back_populates="film")


class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("customers.customer_id"))
    customer: Mapped["Customer"] = relationship(back_populates="orders")
    tickets: Mapped[List["Ticket"]] = relationship(back_populates="order")


class FilmSession(Base):
    __tablename__ = "sessions"
    session_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    film_id: Mapped[int] = mapped_column(Integer, ForeignKey("films.film_id"))
    film: Mapped["Film"] = relationship(back_populates="sessions")
    date: Mapped[datetime] = mapped_column(DateTime)


class Ticket(Base):
    __tablename__ = "tickets"
    ticket_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(Integer, ForeignKey("sessions.session_id"))
    session: Mapped["FilmSession"] = relationship()
    cost_rub: Mapped[int] = mapped_column(Integer)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.order_id"))
    order: Mapped["Order"] = relationship(back_populates="tickets")


class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)
    password_hash: Mapped[str] = mapped_column(String)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id
