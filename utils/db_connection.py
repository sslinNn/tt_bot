import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def get_connetion_with_db():
    user_ = os.getenv('POSTGRESQL_USER')
    passwd_ = os.getenv('POSTGRESQL_PASSWORD')
    host_ = os.getenv('POSTGRESQL_HOST')
    dbname_ = os.getenv('POSTGRESQL_DBNAME')
    try:
        engine = create_engine(
            f'postgresql+psycopg2://{user_}:{passwd_}@{host_}/{dbname_}',
            pool_size=10,
            max_overflow=20
        )
        return engine
    except Exception as ex:
        return ex




if __name__ == '__main__':
    print(get_connetion_with_db())