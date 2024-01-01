CREATE  TABLE mathcounts.users (
  user_id int(8) NOT NULL AUTO_INCREMENT,
  email VARCHAR(200) NOT NULL ,
  password VARCHAR(100) NOT NULL ,
  name VARCHAR(50) NOT NULL ,
  enabled TINYINT NOT NULL DEFAULT 1 ,
  PRIMARY KEY (user_id)
);

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
