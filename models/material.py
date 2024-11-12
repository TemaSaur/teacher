import uuid
from pymysql import Connection
from pydantic import Field
from .model import Model

# CREATE TABLE study_materials (
# 	id INT NOT NULL AUTO_INCREMENT,
# 	title VARCHAR(255) NOT NULL,
# 	file_id CHAR(36),
# 	link_url TEXT,
# 	class TINYINT NOT NULL,
# 	quarter TINYINT NOT NULL,

# 	PRIMARY KEY(id),
# 	FOREIGN KEY(file_id) REFERENCES files(id)
# );

class Material(Model):
	id: int
	title: str
	file_id: uuid.UUID | None
	link_url: str | None
	clas: int = Field(alias="class")
	quarter: int

	def __init__(self, fetched: tuple | None = None):
		if fetched is None:
			return
		self.id = fetched[0]
		self.title = fetched[1]
		self.file_id = fetched[2]
		self.link_url = fetched[3]
		self.clas = fetched[4]
		self.quarter = fetched[5]

	def create(self, conn: Connection):
		sql = """
		INSERT INTO study_materials (title, file_id, link_url, class, quarter)
		VALUES (%s, %s, %s, %s, %s);
		"""
		with conn.cursor() as cur:
			cur.execute(
				sql,
				(self.title, self.file_id, self.link_url, self.clas, self.quarter)
			)
			self.id = cur.lastrowid
			return self

