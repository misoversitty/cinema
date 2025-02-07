from marshmallow import Schema, fields


class CustomerSchema(Schema):
    customer_id = fields.Int()
    first_name = fields.String()
    last_name = fields.String()
    middle_name = fields.String()
    orders = fields.List(fields.Nested("OrderSchema"))
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


class FilmSchema(Schema):
    film_id = fields.Int()
    name = fields.String()
    sessions = fields.List(fields.Nested("FilmSessionSchema", exclude=["film"]))
film_schema = FilmSchema()
films_schema = FilmSchema(many=True)


class OrderSchema(Schema):
    order_id = fields.Int()
    customer_id = fields.Integer()
    customer = fields.Nested("CustomerSchema", exclude=["first_name", "last_name", "middle_name", "orders"])
    tickets = fields.List(fields.Nested("OrderTicketAssociationSchema"))
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


class FilmSessionSchema(Schema):
    session_id = fields.Int()
    film = fields.Nested("FilmSchema", exclude=["sessions"])
    date = fields.String()
    include_relationships = True
filmSession_schema = FilmSessionSchema()
filmSessions_schema = FilmSessionSchema(many=True)


class TicketSchema(Schema):
    ticket_id = fields.Int()
    session_id = fields.Int()
    cost_rub = fields.Int()
ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

class OrderTicketAssociationSchema(Schema):
    ticket_id = fields.Int()
