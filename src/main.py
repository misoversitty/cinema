from connexion import FlaskApp
from connexion.resolver import MethodResolver

from config import *


app = FlaskApp(__name__, specification_dir=SPECIFICATION_PATH)
app.add_api("swagger.yml", resolver=MethodResolver('controllers'))


def main():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
