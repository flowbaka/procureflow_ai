from sqlalchemy import URL, create_engine, text

from app.config import settings
from sqlalchemy.orm import DeclarativeBase


# Shared parent class for all database models
class Base(DeclarativeBase):
    pass


# Build the database connection address
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD.get_secret_value(),
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)

# Configure the connection manager
engine = create_engine(
    database_url,
    pool_pre_ping=True,
)


def test_connection():
    # Open a connection and run a simple query
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful:", result.scalar_one())


# Run this test only when executing this module directly
if __name__ == "__main__":
    test_connection()