import requests
from connexion import FlaskApp
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for


def registryViews(app: FlaskApp):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/customers")
    def show_customers():
        customers = requests.get("http://localhost:8000/api/customers").json()
        return render_template("customers.html", customers=customers)

    @app.route("/customers/<int:id>", methods=["POST", "GET"])
    def show_customer(id):
        if request.method == "GET":
            customer = requests.get(f"http://localhost:8000/api/customers/{id}").json()
            return render_template("customer.html", customer=customer)
        elif request.method == "POST":
            last_name = request.form.get("last_name")
            first_name = request.form.get("first_name")
            middle_name = request.form.get("middle_name")
            data = {"last_name": last_name,
                    "first_name": first_name,
                    "middle_name": middle_name}
            res = requests.post(f"http://localhost:8000/api/customers/{id}", json=data)
            return "", 201

    @app.route("/customers/add_new", methods=["POST", "GET"])
    def add_customer():
        if request.method == "POST":
            last_name = request.form.get("last_name")
            first_name = request.form.get("first_name")
            middle_name = request.form.get("middle_name")
            data = {"last_name": last_name,
                    "first_name": first_name,
                    "middle_name": middle_name}
            res = requests.post(f"http://localhost:8000/api/customers", json=data)
            if res.status_code == 201:
                return redirect(url_for("customer_created"))
        return render_template("customer.html", customer=None)

    @app.route("/customers/add_new/success")
    def customer_created():
        return render_template("customer_created.html")

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

    @app.route("/films/<int:id>")
    def show_film(id):
        if request.method == "GET":
            film = requests.get(f"http://localhost:8000/api/films/{id}").json()
            return render_template("film.html", film=film)
        elif request.method == "POST":
            pass
