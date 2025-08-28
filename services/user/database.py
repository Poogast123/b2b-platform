from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get the complete connection string from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Fallback if DATABASE_URL is not set (for local development)
if not DATABASE_URL:
    DB_USER = os.getenv("POSTGRES_USER", "postgres")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("POSTGRES_DB", "b2b_db")

    from urllib.parse import quote_plus

    DB_PASSWORD_ENCODED = quote_plus(DB_PASSWORD)
    DATABASE_URL = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD_ENCODED}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# If DATABASE_URL exists but doesn't specify pg8000, modify it
else:
    if DATABASE_URL.startswith('postgresql://'):
        DATABASE_URL = DATABASE_URL.replace('postgresql://', 'postgresql+pg8000://')
    elif DATABASE_URL.startswith('postgresql+psycopg2://'):
        DATABASE_URL = DATABASE_URL.replace('postgresql+psycopg2://', 'postgresql+pg8000://')

print(f"Connecting to: {DATABASE_URL}")

# Create SQLAlchemy engine with pg8000

engine = create_engine(DATABASE_URL, echo=True, future=True)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print(f"PostgreSQL version: {result.scalar()}")
except Exception as e:
    raise RuntimeError(f"PostgreSQL connection failed: {e}")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")