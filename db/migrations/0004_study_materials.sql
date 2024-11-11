-- migrate:up
CREATE TABLE study_materials (
	id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(255) NOT NULL,
	file_id CHAR(36),
	class TINYINT,
	quarter TINYINT,

	PRIMARY KEY(id),
	FOREIGN KEY(file_id) REFERENCES files(id)
);

-- migrate:down
DROP TABLE study_materials;

