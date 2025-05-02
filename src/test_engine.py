from sqlalchemy import create_engine


from core.models import Base


def engine_factory():
    engine = create_engine("sqlite://", echo=True)
    Base.metadata.create_all(engine)
    return engine