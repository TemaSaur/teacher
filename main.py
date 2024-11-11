from sqlalchemy import create_engine
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from repository.users import Querier
from config import server


env = load_dotenv(".env")

engine = create_engine(os.getenv("DATABASE_URL")
		.replace("mysql://", "mysql+pymysql://"))

server.jinja = Jinja2Templates(directory="templates/")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index(request: Request, name: str | None = None):
	context = {
		"name": name or "Default"
	}
	return server.jinja.TemplateResponse(
		request=request,
		name="index.html",
		context=context)


@app.get("/study-materials")
def materials(request: Request):
	return server.jinja.TemplateResponse(
		request=request,
		name="materials.html"
	)


@app.get("/tests")
def materials(request: Request):
	return server.jinja.TemplateResponse(
		request=request,
		name="tests.html"
	)

@app.get("/account")
def materials(request: Request):
	return server.jinja.TemplateResponse(
		request=request,
		name="account.html"
	)


@app.get("/data")
def data():
	with engine.connect() as conn:
		result = Querier(conn).get_all()
		return list(result)

