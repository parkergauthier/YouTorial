import os
import toml
from dotenv import load_dotenv
from sqlalchemy import create_engine
import psycopg2

load_dotenv()

toml_data = toml.load(".streamlit/secrets.toml")

# DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
# DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
# DATABASE_HOST = os.environ["DATABASE_HOST"]
# DATABASE_PORT = os.environ["DATABASE_PORT"]
# DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]

DATABASE_USERNAME = toml_data["DATABASE_USERNAME"]
DATABASE_PASSWORD = toml_data["DATABASE_PASSWORD"]
DATABASE_HOST = toml_data["DATABASE_HOST"]
DATABASE_PORT = toml_data["DATABASE_PORT"]
DATABASE_DATABASE = toml_data["DATABASE_DATABASE"]
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

conn_query = psycopg2.connect(
    dbname=DATABASE_DATABASE,
    user=DATABASE_USERNAME,
    host=DATABASE_HOST,
    password=DATABASE_PASSWORD,
)
