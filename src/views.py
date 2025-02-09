import requests
from connexion import FlaskApp
from flask import render_template
from flask import request


def registryViews(app: FlaskApp):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/customers")
    def show_customers():
        customers = requests.get("http://localhost:8000/api/customers").json()
        return render_template("customers.html", customers=customers)

    @app.route("/customers/<int:id>")
    def show_customer(id):
        if request.method == "GET":
            customer = requests.get(f"http://localhost:8000/api/customers/{id}").json()
            return render_template("customer.html", customer=customer)
        elif request.method == "POST":
            pass

    @app.route("/orders")
    def show_orders():
        orders = requests.get("http://localhost:8000/api/orders").json()
        return render_template("orders.html", orders=orders)

    @app.route("/orders/<int:id>")
    def show_order(id):
        if request.method == "GET":
            order = requests.get(f"http://localhost:8000/api/orders/{id}").json()
            return render_template("order.html", order=order)
        elif request.method == "POST":
            pass

    @app.route("/filmsessions")
    def show_filmsessions():
        sessions = requests.get("http://localhost:8000/api/filmsessions").json()
        return render_template("filmsessions.html", sessions=sessions)

    @app.route("/filmsessions/<int:id>")
    def show_filmsession(id):
        if request.method == "GET":
            session = requests.get(f"http://localhost:8000/api/filmsessions/{id}").json()
            return render_template("filmsession.html", session=session)
        elif request.method == "POST":
            pass

    @app.route("/films")
    def show_films():
        films = requests.get("http://localhost:8000/api/films").json()
        return render_template("films.html", films=films)
    