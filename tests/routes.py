from fastapi import Request, APIRouter, Form, Query, HTTPException
from typing import Annotated
from collections import defaultdict as dd
import json
from config import server
from models.test import Test
from tests.helpers import test_json as json_helper


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
	if not json_helper.is_valid_test(test_data):
		return HTTPException(status_code=422, detail="invalid test json")

	test = Test(
		name=name,
		clas=clas,
		quarter=quarter,
		topic=topic,
		test_data=test_data
	)

	return test.create(server.conn)

@router.get("/test/{id}")
def get_one(id: int):
	test = json.loads(Test.get_one(server.conn, id).test_data)
	return test
