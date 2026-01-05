from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost/escola"

engine = createEngine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()