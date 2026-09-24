import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Load environment variables
load_dotenv()

# Get database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Create database engine & session 
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)