from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy import func

from app.core.config import settings
import databases
import sqlalchemy

DATABASE_URL = settings.get_database_url

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, unique=True),
    sqlalchemy.Column("password", sqlalchemy.String),
)

engine = create_engine(DATABASE_URL, echo=True)

metadata.create_all(engine)

sync_session_maker = sessionmaker(engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db() -> Session:
    session = sync_session_maker()
    try:
        yield session
    finally:
        session.close()
