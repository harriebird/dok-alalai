from sqlmodel import Session, create_engine

from app.core import config

from app.models.client import *

engine = create_engine(config.DB_URL)

def get_session():
    with Session(engine) as session:
        yield session
