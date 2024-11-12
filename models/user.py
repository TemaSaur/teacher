from pymysql import Connection
from .model import Model

"""
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
);
"""

class User(Model):
	id: int
	first_name: str
	last_name: str

	def __init__(self, fetched):
		self.id = fetched[0]
		self.first_name = fetched[1]
		self.last_name = fetched[2]

	@staticmethod
	def get_all(conn: Connection):
		sql = """SELECT id, first_name, last_name FROM users;"""
		with conn.cursor() as cur:
			cur.execute(sql)
			return [User(x) for x in cur.fetchmany()]

