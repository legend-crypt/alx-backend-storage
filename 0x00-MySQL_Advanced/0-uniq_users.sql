-- Script that creates the users table with the following requirements:
-- The database name will be passed as an argument of mysql command
-- If the table users already exists, your script should not fail
-- If the table users does not exist, your script should create it and all the required fields in the table users must have the following requirements:
-- email: string, unique, can’t be null
-- name: string, can be null
-- The database name will be passed as an argument of the mysql command


CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);