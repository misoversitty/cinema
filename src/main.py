from core import app
from core_views.views import sub_app
from config import host_address
from config import host_port


app.app.register_blueprint(sub_app)


def main():
    app.run(host=host_address, port=host_port)


if __name__ == "__main__":
    main()
