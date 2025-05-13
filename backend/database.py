from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
from pathlib import Path

# Carregando o .env em outra pasta
dotenv_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path)

POSTGRES_DATABASE_URL = os.getenv("DATABASE_URL")  #"postgresql://user:password@postgres/mydatabase"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() #ORM do SQLalchemy

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()