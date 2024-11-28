from fastapi import APIRouter, Request, Form, Cookie
from fastapi.responses import RedirectResponse
from config import server
# from models.user import User
from models.user_test_result import UserTestResult
from auth.helpers import jwt


router = APIRouter(tags=["Admin"])


@router.get("/admin/login")
async def login_page(request: Request, error: str | None = None):
	context = {}
	if error == 'wrongpassword':
		context['error'] = 'Неверный пароль'
	return server.jinja.TemplateResponse(
		request=request,
		name="admin_login.html",
		context=context
	)


@router.post("/admin/login")
async def login(request: Request,
		email: str = Form(),
		password: str = Form()):
	if email != "admin" or password != "12345678":
		return RedirectResponse("/admin/login?error=wrongpassword", status_code=303)
	token = jwt.issue(email)
	response = RedirectResponse("/admin", status_code=303)
	response.set_cookie(key="token", value=token, expires=jwt.TTL)
	return response


@router.get("/admin")
async def admin(request: Request, token: str | None = Cookie()):
	if (validate := jwt.validate(token)) and validate['sub'] != "admin":
		return RedirectResponse("/", status_code=303)

	test_results = UserTestResult.get_all(server.conn)

	return server.jinja.TemplateResponse(
		request=request,
		name="admin.html",
		context={"results": test_results}
	)

