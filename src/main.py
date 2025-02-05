from connexion import FlaskApp
from connexion.resolver import MethodResolver

from config import *


connexion_app = FlaskApp(__name__, specification_dir=SPECIFICATION_PATH)
connexion_app.add_api("swagger.yml", resolver=MethodResolver('controllers'))
app = connexion_app.app


def main():
    connexion_app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
