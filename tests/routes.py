from fastapi import Request, APIRouter
from config import server


router = APIRouter()


@router.get("/tests")
def tests(request: Request):
	return server.jinja.TemplateResponse(
		request=request,
		name="tests.html"
	)
