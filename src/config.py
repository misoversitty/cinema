from pathlib import Path
import yaml
from sqlalchemy import create_engine


ROOT_PATH = Path(__file__).parent.parent.resolve()
SOURCES_PATH = ROOT_PATH / "src"
SPECIFICATION_PATH = SOURCES_PATH
SECRETS_PATH = ROOT_PATH


with open(SECRETS_PATH / "secrets.yaml", 'r') as file_buffer:
    s = yaml.load(file_buffer, Loader=yaml.Loader)
    __db_schema = s.get("DB_SCHEMA")
    __db_name = s.get("DB_NAME")
    __db_username = s.get("DB_USERNAME")
    __db_password = s.get("DB_PASSWORD")
    __db_uri = s.get("DB_URI")

engine = create_engine(f"postgresql+psycopg2://{__db_username}:{__db_password}@{__db_uri}/{__db_name}",
                       connect_args={'options': '-csearch_path={}'.format(__db_schema)})
