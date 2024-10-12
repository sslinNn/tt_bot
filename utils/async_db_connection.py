from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.users_locations import Base
import os
from dotenv import load_dotenv


load_dotenv()

# Создание асинхронного движка

user_ = os.getenv('POSTGRESQL_USER')
passwd_ = os.getenv('POSTGRESQL_PASSWORD')
host_ = os.getenv('POSTGRESQL_HOST')
dbname_ = os.getenv('POSTGRESQL_DBNAME')

engine = create_async_engine(f'postgresql+asyncpg://{user_}:{passwd_}@{host_}/{dbname_}', echo=True)

# Создание фабрики сессий
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Асинхронное создание таблиц
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)