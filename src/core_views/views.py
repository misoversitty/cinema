import requests
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

from flask import Blueprint

from core.urls import make_url

sub_app = Blueprint("core_views", __name__,
                    static_folder="static",
                    static_url_path="/core_views/static",
                    template_folder="./templates")

@sub_app.route("/")
def index():
    return render_template("index.html")

@sub_app.route("/customers")
def show_customers():
    url = make_url("/api/customers")
    customers = requests.get(url).json()
    return render_template("customers.html", customers=customers)

@sub_app.route("/customers/<int:id>", methods=["POST", "GET"])
def show_customer(id):
    url = make_url(f"/api/customers{id}")
    if request.method == "GET":
        customer = requests.get(url).json()
        return render_template("customer.html", customer=customer)
    elif request.method == "POST":
        last_name = request.form.get("last_name")
        first_name = request.form.get("first_name")
        middle_name = request.form.get("middle_name")
        data = {"last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name}
        res = requests.post(url, json=data)
        return "", 201

@sub_app.route("/customers/add_new", methods=["POST", "GET"])
def add_customer():
    url = make_url("/api/customers")
    if request.method == "POST":
        last_name = request.form.get("last_name")
        first_name = request.form.get("first_name")
        middle_name = request.form.get("middle_name")
        data = {"last_name": last_name,
                "first_name": first_name,
                "middle_name": middle_name}
        res = requests.post(url, json=data)
        if res.status_code == 201:
            return redirect(url_for("customer_created"))
    return render_template("customer.html", customer=None)

@sub_app.route("/customers/add_new/success")
def customer_created():
    return render_template("customer_created.html")

@sub_app.route("/orders")
def show_orders():
    url = make_url("/api/orders")
    orders = requests.get(url).json()
    return render_template("orders.html", orders=orders)

@sub_app.route("/orders/<int:id>")
def show_order(id):
    url = make_url(f"/api/orders/{id}")
    if request.method == "GET":
        order = requests.get(url).json()
        return render_template("order.html", order=order)
    elif request.method == "POST":
        pass

@sub_app.route("/orders/add_new", methods=["POST", "GET"])
def add_order():
    if request.method == "POST":
        pass
    return render_template("order.html", order=None)

@sub_app.route("/filmsessions")
def show_filmsessions():
    url = make_url("/api/filmsessions")
    sessions = requests.get(url).json()
    return render_template("filmsessions.html", sessions=sessions)

@sub_app.route("/filmsessions/<int:id>")
def show_filmsession(id):
    url = make_url(f"/api/filmsessions/{id}")
    if request.method == "GET":
        session = requests.get(url).json()
        return render_template("filmsession.html", session=session)
    elif request.method == "POST":
        pass

@sub_app.route("/filmsessions/add_new", methods=["POST", "GET"])
def add_filmsession():
    url = make_url(f"/api/filmsessions")
    if request.method == "POST":
        return redirect(url_for("filmsession_created"))
    return render_template("filmsession.html", customer=None)

@sub_app.route("/films")
def show_films():
    url = make_url("/api/films")
    films = requests.get(url).json()
    return render_template("films.html", films=films)

@sub_app.route("/films/<int:id>")
def show_film(id):
    url = make_url(f"/api/films/{id}")
    if request.method == "GET":
        film = requests.get(url).json()
        return render_template("film.html", film=film)
    elif request.method == "POST":
        pass

@sub_app.route("/films/add_new", methods=["POST", "GET"])
def add_film():
    url = make_url("/api/films")
    if request.method == "POST":
        name = request.form.get("name")
        data = {"name": name}
        res = requests.post(url, json=data)
        if res.status_code == 201:
            return redirect(url_for("film_created"))
    return render_template("film.html", film=None)

@sub_app.route("/film/add_new/success")
def film_created():
    return render_template("film_created.html")
