from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "postgresql+psycopg2://task_user:password@localhost:5432/task_manager"

Base = declarative_base()

try:
    engine = create_engine(DATABASE_URL, echo=True, future=True)
    # Проверяем соединение корректно через text()
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
except SQLAlchemyError as e:
    print("Ошибка подключения к базе данных:", e)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
