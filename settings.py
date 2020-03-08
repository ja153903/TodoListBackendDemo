from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path('.')
load_dotenv(dotenv_path=env_path)

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB = os.getenv("DB_NAME")
