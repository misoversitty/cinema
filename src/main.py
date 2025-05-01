from core import app
from core_views.views import sub_app


app.app.register_blueprint(sub_app)


def main():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
