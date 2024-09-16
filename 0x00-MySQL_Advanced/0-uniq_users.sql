-- Script that creates the users table with the following requirements:
-- id INT, unique, can’t be null, auto increment and is a primary key
-- email String(255), unique, can’t be null
-- name String(255)
-- country ENUM(‘US’, ‘CO’, ‘TN’), can be null


CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US',
    PRIMARY KEY (id)
);