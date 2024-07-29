CREATE DATABASE tracks;
ALTER DATABASE tracks CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use tracks;

CREATE TABLE tracks (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    artist_name VARCHAR(255) NOT NULL,
    uri VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO tracks
    (name, artist_name, uri)
VALUES
    ('Hypnotized', 'Purple Disco Machine', 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2'),
    ('Aquaman', 'WALK THE MOON', 'spotify:track:71wT7aMCFPYfzutF66OLac')
;