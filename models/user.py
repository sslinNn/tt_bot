from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from utils.db_connection import get_connetion_with_db

# Создание базового класса
Base = declarative_base()

# Определение ORM-класса User, который будет соответствовать таблице в базе данных
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    name = Column(String)
    location = Column(String)


    def __repr__(self):
        return (
            f"<User(telegram_id={self.telegram_id}, "
            f"name={self.name}, "
        )

Base.metadata.create_all(get_connetion_with_db())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_connetion_with_db())

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()