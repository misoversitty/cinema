from connexion import FlaskApp
from connexion.resolver import MethodResolver

from config import *

app = FlaskApp(__name__, specification_dir=SPECIFICATION_PATH)
app.add_api("core.yaml", resolver=MethodResolver('controllers'))