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


if __name__ == "__main__":
    main()
