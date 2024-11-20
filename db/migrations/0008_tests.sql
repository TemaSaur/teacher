-- migrate:up
CREATE TABLE tests (
	id      INT     NOT NULL AUTO_INCREMENT,
	name    TEXT    NOT NULL,
	class   TINYINT NOT NULL,
	quarter TINYINT NOT NULL,
	topic   TEXT    NOT NULL,

	PRIMARY KEY(id)
);

CREATE TABLE questions (
	test_id   INT  NOT NULL,
	test_data JSON NOT NULL,

	PRIMARY KEY(test_id),
	FOREIGN KEY(test_id) REFERENCES tests(id)
);

-- migrate:down
DROP TABLE questions;

DROP TABLE tests;

