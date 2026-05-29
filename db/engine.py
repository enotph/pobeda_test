import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import Config

DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)

def drop_tables():
    Base.metadata.drop_all(bind=engine)

def get_session():
    db = SessionLocal()
    return db