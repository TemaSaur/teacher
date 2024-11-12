from fastapi import Request, APIRouter, UploadFile, Form
from config import server
from models.file import File
from models.material import Material

router = APIRouter()


@router.get("/study-materials")
def materials(request: Request):
	context = {
		"materials": ["1", "2", "3"]
	}
	return server.jinja.TemplateResponse(
		request=request,
		name="materials.html",
		context=context
	)


@router.post("/study-materials")
async def create(file: UploadFile,
		title: str = Form(),
		clas: int = Form(),
		quarter: int = Form()):
	f = await File.read(file)
	f.upload(server.conn)
	material = Material()
	material.title = title
	material.file_id = f.id
	material.link_url = None
	material.clas = clas
	material.quarter = quarter
	material.create(server.conn)
	return material

