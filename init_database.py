#!/usr/bin/env python3
"""
Скрипт для инициализации БД
Звпускать после установки зависимостей и настройки .env
"""

import sys
from db.engine import create_tables, engine

def check_db_connection():
    try:
        with engine.connect() as conn:
            print("База данных подключена успешно!")
            return True
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")
        return False

if __name__ == "__main__":
    print("Инициализация базы данных...")

    if check_db_connection():
        try:
            create_tables()
            print("Таблицы успешно созданы!")
            print("Создана таблица: users")
        except Exception as e:
            print(f"Ошибка при создании таблиц: {e}")
            sys.exit(1)
    else:
        print("Не удалось подключиться к базе данных.")
        sys.exit(1)