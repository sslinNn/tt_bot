from models.user import get_db
from models.user import User

def add_user_to_db(telegram_id: int, name: str):
    db = next(get_db())

    # Проверка, существует ли пользователь
    existing_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if existing_user:
        return f"Пользователь {name} уже зарегистрирован."

    # Создание нового пользователя
    new_user = User(telegram_id=telegram_id, name=name)
    db.add(new_user)
    db.commit()
    return f"Пользователь {name} успешно добавлен."