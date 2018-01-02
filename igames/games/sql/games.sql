CREATE TABLE IF NOT EXISTS games ( 
	`id` int(8)						NOT NULL AUTO_INCREMENT,
	`name` varchar(64)				NOT NULL,
	`price` varchar(64)				NOT NULL,
	`score` varchar(64)				NOT NULL,
	`developer` varchar(255),
	`publisher` varchar(255),
	`description` TEXT				DEFAULT NULL,
	`review` TEXT					NOT NULL,
	`category` TEXT					NOT NULL,
	`cover_url` varchar(255)		NOT NULL,
	`advantages` TEXT				NOT NULL,
	`disadvantages` TEXT			NOT NULL,
	`language_number` varchar(32)	NOT NULL,
	`save_time` TIMESTAMP			NOT NULL,
	PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
