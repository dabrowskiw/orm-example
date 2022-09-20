CREATE DATABASE orm CHARACTER SET UTF8;
CREATE USER ormuser@localhost IDENTIFIED BY '5YAPwyTWhPwcLuX';
GRANT ALL PRIVILEGES ON orm.* TO ormuser@localhost;
FLUSH PRIVILEGES;

CREATE TABLE patient(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(200), age INT, station_id, CONSTRAINT FOREIGN KEY(station_id) REFERENCES station(id));
CREATE TABLE station(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(200), capacity INT);

INSERT INTO station(id, name, capacity) VALUES(1, "Behandlung", 1);
INSERT INTO station(id, name, capacity) VALUES(2, "Genesung", 10);

INSERT INTO patient(name, age, station_id) VALUES("Dade Murphy", 27, 1);
INSERT INTO patient(name, age, station_id) VALUES("Kate Libby", 29, 2);
INSERT INTO patient(name, age, station_id) VALUES("Emmanuel Goldstein", 25, 2);
INSERT INTO patient(name, age, station_id) VALUES("Paul Cook", 37, 2);
INSERT INTO patient(name, age, station_id) VALUES("Ramon Sanchez", 31, 2);
