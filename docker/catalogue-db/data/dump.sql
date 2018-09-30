CREATE USER IF NOT EXISTS 'catalogue_user' IDENTIFIED BY 'default_password';

GRANT ALL ON socksdb.* TO 'catalogue_user';

CREATE TABLE IF NOT EXISTS sock (
	sock_id varchar(40) NOT NULL, 
	name varchar(20), 
	description varchar(200), 
	price float, 
	count int, 
	image_url_1 varchar(40), 
	image_url_2 varchar(40), 
	PRIMARY KEY(sock_id)
);

CREATE TABLE IF NOT EXISTS tag (
	tag_id MEDIUMINT NOT NULL AUTO_INCREMENT, 
	name varchar(20), 
	PRIMARY KEY(tag_id)
);

CREATE TABLE IF NOT EXISTS sock_tag (
	sock_id varchar(40), 
	tag_id MEDIUMINT NOT NULL, 
	FOREIGN KEY (sock_id) 
		REFERENCES sock(sock_id), 
	FOREIGN KEY(tag_id)
		REFERENCES tag(tag_id)
);

truncate table sock_tag;
truncate table tag;
truncate table sock;



