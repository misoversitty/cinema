from sqlalchemy import create_engine

def engine_factory(db_schema, db_name, db_username, db_password, db_uri):
    connection_string = f"postgresql+psycopg2://{db_username}:{db_password}@{db_uri}/{db_name}"
    engine = create_engine(connection_string,
                           connect_args={'options': f'-csearch_path={db_schema}'},
                           client_encoding='utf8')
    return engine