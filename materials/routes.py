from typing import Annotated
from fastapi import Request, APIRouter, UploadFile, Form, Query
from config import server
from models.file import File
from models.material import Material
from models.material_file import MaterialFile

router = APIRouter()


@router.get("/study-materials")
def materials(request: Request,
		clas: Annotated[str | None, Query(alias="class")] = None,
		quarter: Annotated[str | None, Query(alias="quarter")] = None):
	materials = None
	if clas is not None and quarter is not None:
		materials = MaterialFile.get_filtered(server.conn, clas, quarter)
	# materials = MaterialFile.get_all(server.conn)
	context = {
		"materials": materials,
		"class": clas,
		"quarter": quarter,
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

