from logging.config import fileConfig

from alembic import context

from app.database import Base, database_url, engine
from app.models import Supplier  # Register the supplier table with Base


config = context.config

# Use Alembic's logging configuration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Give Alembic our table definitions
target_metadata = Base.metadata


def run_migrations_offline():
    # Generate SQL without connecting to PostgreSQL
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    # Connect to PostgreSQL to apply database changes
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()