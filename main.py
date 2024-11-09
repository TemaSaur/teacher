from sqlalchemy import create_engine
from fastapi import FastAPI
from dotenv import load_dotenv
from repository.user import Querier
import os


load_dotenv(".env")

engine = create_engine(os.getenv("DATABASE_URL")
                       .replace("mysql://", "mysql+pymysql://"))

app = FastAPI()

@app.get("/")
def index():
    return "hello"


@app.get("/data")
def data():
    with engine.connect() as conn:
        result = Querier(conn).get_all()
        return list(result)

