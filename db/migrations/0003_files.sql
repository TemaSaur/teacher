-- migrate:up
CREATE TABLE files (
	id CHAR(36) NOT NULL,
	fname VARCHAR(255),
	fsize INT,
	ftype VARCHAR(63),
	fdata LONGBLOB,

	PRIMARY KEY(id)
);

-- migrate:down
DROP TABLE files;

