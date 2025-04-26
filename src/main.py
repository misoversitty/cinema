from connexion import FlaskApp
from connexion.resolver import MethodResolver

from config import *
from core_views.views import sub_app


app = FlaskApp(__name__, specification_dir=SPECIFICATION_PATH)
app.add_api("core.yaml", resolver=MethodResolver('controllers'))

app.app.register_blueprint(sub_app)


def main():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
