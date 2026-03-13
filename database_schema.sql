CREATE TABLE users (
user_id INT PRIMARY KEY,
name VARCHAR(100)
);

CREATE TABLE user_activity (
activity_id INT PRIMARY KEY,
user_id INT,
item VARCHAR(255),
timestamp TIMESTAMP
);

CREATE TABLE recommendations (
rec_id INT PRIMARY KEY,
user_id INT,
item VARCHAR(255)
);
