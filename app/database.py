from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_SERVER_ADDRESS = os.getenv('DB_SERVER_ADDRESS')

# Replace with your own PostgreSQL instance
DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER_ADDRESS}/{DB_NAME}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)