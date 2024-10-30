# from sqlalchemy import create_engine
#
# engine = create_engine('sqlite:///blog.db')


# # database.py
# from databases import Database
# import os
# from dotenv import load_dotenv
#
# load_dotenv()  # Automatically loads .env file
#
# # Set up database URL
# DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
# POSTGRES_DB = os.getenv("POSTGRES_DB", "testlogic")
# POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
# POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
#
# DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}/{POSTGRES_DB}"
# database = Database(DATABASE_URL)

# 3333333333333333333

# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Construct the database URL
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('POSTGRES_DB')}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
