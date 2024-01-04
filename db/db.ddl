CREATE SCHEMA `new_schema` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;

CREATE TABLE mathcounts.levels (
	level_id int(1) NOT NULL,
    level VARCHAR(10) NOT NULL,
    PRIMARY KEY (level_id)
);

CREATE TABLE mathcounts.rounds (
	round_id int(1) NOT NULL,
    round VARCHAR(20) NOT NULL,
    PRIMARY KEY (round_id)
);

CREATE TABLE mathcounts.questions (
	question_id int(8) NOT NULL AUTO_INCREMENT,
    level_id int(1) NOT NULL,
    round_id int(1) NOT NULL,
    year int(4) NOT NULL,
    question TEXT NOT NULL,
    answers VARCHAR(200) NOT NULL,
    credit VARCHAR(50),
    PRIMARY KEY (question_id),
    CONSTRAINT fk_level_id FOREIGN KEY (level_id) REFERENCES mathcounts.levels (level_id),
    CONSTRAINT fk_round_id FOREIGN KEY (round_id) REFERENCES mathcounts.rounds (round_id)
);

CREATE TABLE mathcounts.images (
	image_id int(8) NOT NULL AUTO_INCREMENT,
    question_id int(8) NOT NULL,
    url VARCHAR(200),
    PRIMARY KEY (image_id),
    CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES mathcounts.questions (question_id)
);

CREATE  TABLE mathcounts.contact_message (
  message_id int NOT NULL AUTO_INCREMENT,
  name VARCHAR(200) NOT NULL,
  email VARCHAR(200) NOT NULL,
  subject VARCHAR(200) NOT NULL,
  message TEXT,
  PRIMARY KEY (message_id)
);
