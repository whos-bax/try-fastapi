from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from core.settings import settings


# base metadata
class Base(DeclarativeBase):
    pass


# (1) db connection
engine = create_engine(settings.db_url)

# (2) session
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# (3) get_db
def get_db() -> Generator[Session, None, None]:
    db = session()
    try:
        yield db
    finally:
        db.close()


def get_cli_session():
    DB_URL = settings.db_url
    CLI_DB_URL = DB_URL.replace("tensorcube-pg", "0.0.0.0")
    engine = create_engine(CLI_DB_URL)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_for_cli():
    db = get_cli_session()
    try:
        yield db()
    finally:
        db().close()