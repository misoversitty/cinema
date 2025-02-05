import requests
from connexion import FlaskApp
from connexion.resolver import MethodResolver
from flask import render_template

from config import *


app = FlaskApp(__name__, specification_dir=SPECIFICATION_PATH)
app.add_api("swagger.yml", resolver=MethodResolver('controllers'))


def main():
    app.run(host="0.0.0.0", port=8000)


@app.route("/customers")
def show_customers():
    request = requests.get("http://localhost:8000/api/customers")
    customers = request.json()
    return render_template("customers.html", customers=customers)


if __name__ == "__main__":
    main()
