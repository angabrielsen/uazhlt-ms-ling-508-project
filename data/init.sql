CREATE DATABASE IF NOT EXISTS r_music_maker;

USE r_music_maker;

CREATE TABLE IF NOT EXISTS submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    submission_id VARCHAR(255) UNIQUE NOT NULL,
    url VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    submission_id VARCHAR(255),
    comment_text VARCHAR(1000),
    FOREIGN KEY (submission_id) REFERENCES submissions(submission_id)
);