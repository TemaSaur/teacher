from fastapi import Request, APIRouter
from config import server

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
def create():
	pass

