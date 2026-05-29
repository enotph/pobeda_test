import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

load_dotenv()

# Путь к файлу базы данных SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///pobeda.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Для SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    """Создает таблицы в БД"""
    Base.metadata.create_all(bind=engine)

def drop_tables():
    """Удаляет таблицы в БД"""
    Base.metadata.drop_all(bind=engine)

def get_session():
    """Создание сессии"""
    db = SessionLocal()
    return db