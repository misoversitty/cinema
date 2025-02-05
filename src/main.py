import requests
from connexion import FlaskApp
from connexion.resolver import MethodResolver
from flask import render_template, request

from config import *


app = FlaskApp(__name__, specification_dir=SPECIFICATION_PATH)
app.add_api("swagger.yml", resolver=MethodResolver('controllers'))


def main():
    app.run(host="0.0.0.0", port=8000)


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


@app.route("/filmsessions")
def show_filmsessions():
    sessions = requests.get("http://localhost:8000/api/filmsessions").json()
    return render_template("filmsessions.html", sessions=sessions)


if __name__ == "__main__":
    main()
