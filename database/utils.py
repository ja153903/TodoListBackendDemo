import sqlalchemy as db

from settings import DATABASE_USER, DATABASE_PASSWORD, HOST, DB, PORT
from models.base import Base


DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOST}:{PORT}/{DB}"

def get_engine():
    engine = db.create_engine(DATABASE_URL)

    Base.metadata.create_all(engine)

    return engine


def get_session():
    Session = db.orm.sessionmaker()
    Session.configure(bind=get_engine())

    return Session()
