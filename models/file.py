import uuid
from pymysql import Connection
from fastapi import UploadFile
from .model import Model

"""
CREATE TABLE files (
	id CHAR(36) NOT NULL,
	fname VARCHAR(255),
	fsize INT,
	fdata LONGBLOB,

	PRIMARY KEY(id)
);
"""

class File(Model):
	id: uuid.UUID
	fname: str
	fsize: int
	fdata: bytes

	def __init__(self, fetched: tuple | None = None):
		if fetched is None:
			return

		self.id = fetched[0]
		self.fname = fetched[1]
		self.fsize = fetched[2]
		self.fdata = fetched[3]

	@staticmethod
	async def read(file: UploadFile):
		self = File()
		self.fname = file.filename
		self.fsize = file.size
		self.fdata = await file.read()
		return self

	def upload(self, conn: Connection):
		sql = """
		INSERT INTO files (id, fname, fsize, fdata)
		VALUES (%s, %s, %s, %s);
		"""
		uid = uuid.uuid4()
		with conn.cursor() as cur:
			cur.execute(sql, (str(uid), self.fname, self.fsize, self.fdata))
			self.id = uid
			return self

