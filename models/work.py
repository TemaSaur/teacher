from pymysql import Connection
from models.model import Model
import uuid

"""
CREATE TABLE students_works (
	id           INT      NOT NULL AUTO_INCREMENT,
	file_id      CHAR(36) NOT NULL,
	user_id      INT      NOT NULL,
	score        TINYINT  NOT NULL,
	max_score    TINYINT  NOT NULL,
	sent_at      INT      NOT NULL,
	score_detail TEXT,
	sent_detail  TEXT,

	PRIMARY KEY(id),
	FOREIGN KEY(file_id) REFERENCES files(id),
	FOREIGN KEY(user_id) REFERENCES users(id)
);
"""

class Work(Model):
	id: int
	file_id: uuid.UUID
	user_id: int
	score: int
	max_score: int
	sent_at: int
	score_detail: str
	sent_detail: str

	def __init__(
		self,
		id: int | None = None,
		file_id: uuid.UUID | None = None,
		user_id: int | None = None,
		score: int | None = None,
		max_score: int | None = None,
		sent_at: int | None = None,
		score_detail: str | None = None,
		sent_detail: str | None = None
	):
		self.id = id
		self.file_id = file_id
		self.user_id = user_id
		self.score = score
		self.max_score = max_score
		self.sent_at = sent_at
		self.score_detail = score_detail
		self.sent_detail = sent_detail

	def send(self, conn: Connection):
		sql = """
		INSERT INTO students_works
			(file_id, user_id, sent_at, sent_detail, score, max_score)
		VALUES
			(%s, %s, unix_timestamp(), %s, 0, 0)
		"""

		with conn.cursor() as cur:
			cur.execute(sql, (
				self.file_id,
				self.user_id,
				self.sent_detail
			))

			self.id = cur.lastrowid
			return self

