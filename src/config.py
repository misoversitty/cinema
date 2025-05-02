from pathlib import Path

from configparser import ConfigParser
from configparser import ExtendedInterpolation

conf = ConfigParser(interpolation=ExtendedInterpolation())
config_path = Path(__file__).parent.parent.resolve()
conf.read([config_path / "config", config_path / "secrets"])

host_address = conf["Main"]["host"]
host_port = int(conf["Main"]["port"])


ROOT_PATH = Path(conf["Paths"]["ROOT_PATH"])
SOURCES_PATH = Path(conf["Paths"]["SOURCES_PATH"])
SPECIFICATION_PATH = Path(conf["Paths"]["SPECIFICATION_PATH"])
SECRETS_PATH = Path(conf["Paths"]["SECRETS_PATH"])

secrets_section = conf["secrets"]
__db_schema = secrets_section["DB_SCHEMA"]
__db_name = secrets_section["DB_NAME"]
__db_username = secrets_section["DB_USERNAME"]
__db_password = secrets_section["DB_PASSWORD"]
__db_uri = secrets_section["DB_URI"]

if conf["Main"]["Mode"] == "Database.Development":
    from development_engine import engine_factory
    engine = engine_factory(__db_schema, __db_name, __db_username, __db_password, __db_uri)
elif conf["Main"]["Mode"] == "Database.Test":
    from test_engine import engine_factory
    engine = engine_factory()
