from db import get_session
from models import User

def add_to_user(name: str, email: str) -> User:
    """
    Добавляет запись в таблицу User
    Возвращает объект User
    """
    with get_session() as session:
        try:
            user = User(name=name, email=email)
            session.add(user)
            session.commit()
            session.refresh(user)  # Чтобы получить id после создания
            print(f"Пользователь {name} ({email}) добавлен в БД")
            return user
        except Exception as e:
            session.rollback()
            print(f"Ошибка добавления пользователя: {e}")
            raise

def get_user_by_id(user_id: int) -> User:
    """
    Поиск записи в таблице User по атрибуту id
    Возвращает объект User
    """
    with get_session() as session:
        try:
            user = session.get(User, user_id)
            if user:
                print(f"Найден пользователь: {user.name} (ID: {user.id})")
                return user
            else:
                print(f"Пользователь с ID {user_id} не найден")
                return None
        except Exception as e:
            print(f"Ошибка получения пользователя: {e}")
            return None

def get_all_users() -> list[User]:
    """
    Возвращает список всех пользователей
    """
    with get_session() as session:
        try:
            users = session.query(User).all()
            print(f"Найдено {len(users)} пользователей")
            return users
        except Exception as e:
            print(f"Ошибка получения списка пользователей: {e}")
            return []

def update_user(user_id: int, name: str = None, email: str = None) -> bool:
    """
    Обновляет данные пользователя
    """
    with get_session() as session:
        try:
            user = session.get(User, user_id)
            if not user:
                print(f"Пользователь с ID {user_id} не найден")
                return False

            if name is not None:
                user.name = name
            if email is not None:
                user.email = email

            session.commit()
            print(f"Пользователь {user_id} обновлен")
            return True
        except Exception as e:
            session.rollback()
            print(f"Ошибка обновления пользователя: {e}")
            return False

def delete_user(user_id: int) -> bool:
    """
    Удаляет пользователя из таблицы User
    Возвращает True если удалено, False если ошибка
    """
    with get_session() as session:
        try:
            user = session.get(User, user_id)
            if not user:
                print(f"Пользователь с ID {user_id} не найден")
                return False

            session.delete(user)
            session.commit()

            print(f"Пользователь {user_id} удален")
            return True
        except Exception as e:
            session.rollback()
            print(f"Ошибка удаления пользователя: {e}")
            return False