from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"
    customer_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    middle_name: Mapped[str] = mapped_column(String)

    orders: Mapped[List["Order"]] = relationship(back_populates="customer")


class Film(Base):
    __tablename__ = "films"
    film_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    sessions: Mapped[List["FilmSession"]] = relationship(back_populates="film")


orders_sessions_link = Table(
    "orders_list",
    Base.metadata,
    Column("order_id", ForeignKey("orders.order_id"), primary_key=True),
    Column("session_id", ForeignKey("sessions.session_id"), primary_key=True))


class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"))
    customer: Mapped["Customer"] = relationship(back_populates="orders")
    sessions: Mapped[List["FilmSession"]] = relationship(secondary=orders_sessions_link, back_populates="orders")


class FilmSession(Base):
    __tablename__ = "sessions"
    session_id: Mapped[int] = mapped_column(primary_key=True)
    film_id: Mapped[int] = mapped_column(ForeignKey("films.film_id"))
    film: Mapped["Film"] = relationship(back_populates="sessions")
    orders: Mapped[List["Order"]] = relationship(secondary=orders_sessions_link, back_populates="sessions")
