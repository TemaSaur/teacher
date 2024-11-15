from fastapi import FastAPI, Request, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from models.user import User
from models.file import File
from config import server
import pymysql

import materials.routes


load_dotenv(".env")

conn = pymysql.connect(
	host=os.getenv("DATABASE_HOST"),
	user=os.getenv("DATABASE_USER"),
	password=os.getenv("DATABASE_PASSWORD"),
	database=os.getenv("DATABASE_DATABASE"),
	autocommit=True,
)

server.conn = conn

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


app.include_router(materials.routes.router)


@app.get("/tests")
def tests(request: Request):
	return server.jinja.TemplateResponse(
		request=request,
		name="tests.html"
	)


@app.get("/account")
def account(request: Request):
	return server.jinja.TemplateResponse(
		request=request,
		name="account.html"
	)


@app.get("/data")
def data():
	return User.get_all(conn)


@app.post("/upload")
async def upload(file: UploadFile):
	f = await File.read(file)
	f.upload(conn)
	conn.commit()
	return f.id
