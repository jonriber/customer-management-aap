from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from tenacity import retry, stop_after_attempt, wait_fixed

DATABASE_URL = os.getenv("DATABASE_URL")

@retry(stop=stop_after_attempt(10), wait=wait_fixed(2))
def connect_to_database():
  return create_engine(DATABASE_URL)

engine = connect_to_database()
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

