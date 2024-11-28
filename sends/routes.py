from fastapi import APIRouter, Request, UploadFile, Form, Cookie
from models.file import File
from models.work import Work
from models.user import User
from config import server
from auth.helpers import jwt

router = APIRouter(tags=["Student Works"])

@router.post("/send")
async def send(
	request: Request,
	file: UploadFile = File(),
	comment: str = Form(),
	token: str = Cookie()
):
	f = await File.read(file)
	f.upload(server.conn)

	if (validate := jwt.validate(token)) and (email := validate['sub']):
		user = User.get_by_email(server.conn, email).__dict__

		work = Work(
			file_id=f.id,
			user_id=user["id"],
			sent_detail=comment
		)
		work.send(server.conn)

	return server.jinja.TemplateResponse(
		request=request,
		name="sent.html",
	)

