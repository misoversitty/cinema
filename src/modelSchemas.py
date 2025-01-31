from marshmallow import Schema, fields


class CustomerSchema(Schema):
    customer_id = fields.Int()
    orders = fields.List(fields.Nested("OrderSchema"))
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


class FilmSchema(Schema):
    film_id = fields.Int()
    name = fields.String()
    sessions = fields.List(fields.Nested("FilmSessionSchema"))


class OrderSchema(Schema):
    order_id = fields.Int()