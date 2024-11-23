from fastapi import Request, APIRouter, Form, Query
from typing import Annotated
from collections import defaultdict as dd
from config import server
from models.test import Test


router = APIRouter()


@router.get("/tests")
def tests(request: Request,
		clas: Annotated[str | None, Query(alias="class")] = None,
		quarter: Annotated[str | None, Query(alias="quarter")] = None):
	tests = None
	if clas is not None and quarter is not None:
		tests_db = Test.get_filtered(server.conn, clas, quarter)
		tests = dd(list)
		for test in tests_db:
			tests[test.topic].append(test)

	context = {
		"results": tests,
		"class": clas,
		"quarter": quarter,
	}
	return server.jinja.TemplateResponse(
		request=request,
		name="tests.html",
		context=context
	)


@router.post("/tests")
def create(
	name: str = Form(),
	clas: int = Form(),
	quarter: int = Form(),
	topic: str = Form(),
	test_data: str = Form()
):
	test = Test(
		name=name,
		clas=clas,
		quarter=quarter,
		topic=topic,
		test_data=test_data
	)

	return test.create(server.conn)
