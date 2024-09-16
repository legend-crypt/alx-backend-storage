--- CREATE TABLE uniq_users AS
--- email unique

CREATE TABLE IF NOT EXISTS users(
    id INT NOT NUll AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY(id)

)