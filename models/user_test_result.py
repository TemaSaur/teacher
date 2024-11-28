from models.model import Model
from models.test_result import TestResult
from models.user import User

from pymysql import Connection


class UserTestResult(Model):
	test_result: TestResult
	user: User

	@staticmethod
	def get_all(conn: Connection):
		sql = """
		SELECT
			TR.id
			, TR.test_id
			, TR.user_id
			, TR.score
			, TR.max_score
			, TR.sent_at,
			, U.id,
			, U.first_name,
			, U.last_name,
			, U.email,
			, U.id,
		FROM test_results AS TR
			LEFT JOIN users AS U ON TR.user_id = U.id
		"""
		with conn.cursor() as cur:
			cur.execute(sql)
			return [
				{
					"test_result": TestResult(*x[:6]),
					"user": User(*x[6:])
				}
				for x in cur.fetchall()
			]

