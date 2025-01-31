from connexion import FlaskApp

from config import *


connexion_app = FlaskApp(__name__, specification_dir="./")
app = connexion_app.app


def main():
    connexion_app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()