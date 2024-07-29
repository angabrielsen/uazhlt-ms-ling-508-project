CREATE DATABASE r_music_maker;
ALTER DATABASE r_music_maker CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use r_music_maker;

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

CREATE TABLE playlists (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE playlist_tracks (
    playlist_id INT NOT NULL,
    track_id INT NOT NULL,
    FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE,
    FOREIGN KEY (track_id) REFERENCES tracks(id) ON DELETE CASCADE,
    PRIMARY KEY (playlist_id, track_id)
);