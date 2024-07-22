import pytest
from app.track import *

def test_track_creation():
    track = Track('1', 'Hypnotized', 'Purple Disco Machine', 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2')
    assert track.id == '1'
    assert track.name == 'Hypnotized'
    assert track.artist_name == 'Purple Disco Machine'
    assert track.uri == 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2'

def test_track_str():
    track = Track('1', 'Hypnotized', 'Purple Disco Machine', 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2')
    assert str(track) == 'Track ID: 1, Name: "Hypnotized", Artist: Purple Disco Machine, URI: spotify:track:0OeFuOAu0P1ONYz5EDdqb2'

def test_empty_attributes():
    track = Track('', '', '', '')
    assert track.id == ''
    assert track.name == ''
    assert track.artist_name == ''
    assert track.uri == ''
    assert str(track) == 'Track ID: , Name: "", Artist: , URI: '

if __name__ == '__main__':
    pytest.main()

# {
#   "album" : {
#     "album_type" : "single",
#     "artists" : [ {
#       "external_urls" : {
#         "spotify" : "https://open.spotify.com/artist/2WBJQGf1bT1kxuoqziH5g4"
#       },
#       "href" : "https://api.spotify.com/v1/artists/2WBJQGf1bT1kxuoqziH5g4",
#       "id" : "2WBJQGf1bT1kxuoqziH5g4",
#       "name" : "Purple Disco Machine",
#       "type" : "artist",
#       "uri" : "spotify:artist:2WBJQGf1bT1kxuoqziH5g4"
#     }, {
#       "external_urls" : {
#         "spotify" : "https://open.spotify.com/artist/4FrXHrpbDLNyO3pbVv8RmF"
#       },
#       "href" : "https://api.spotify.com/v1/artists/4FrXHrpbDLNyO3pbVv8RmF",
#       "id" : "4FrXHrpbDLNyO3pbVv8RmF",
#       "name" : "Sophie and the Giants",
#       "type" : "artist",
#       "uri" : "spotify:artist:4FrXHrpbDLNyO3pbVv8RmF"
#     } ],
#     "available_markets" : [ "GB", "IE", "US" ],
#     "external_urls" : {
#       "spotify" : "https://open.spotify.com/album/07UKVsstXPhVacXjjPJAJh"
#     },
#     "href" : "https://api.spotify.com/v1/albums/07UKVsstXPhVacXjjPJAJh",
#     "id" : "07UKVsstXPhVacXjjPJAJh",
#     "images" : [ {
#       "height" : 640,
#       "url" : "https://i.scdn.co/image/ab67616d0000b273cbd22c36b39c977cdf2e36bf",
#       "width" : 640
#     }, {
#       "height" : 300,
#       "url" : "https://i.scdn.co/image/ab67616d00001e02cbd22c36b39c977cdf2e36bf",
#       "width" : 300
#     }, {
#       "height" : 64,
#       "url" : "https://i.scdn.co/image/ab67616d00004851cbd22c36b39c977cdf2e36bf",
#       "width" : 64
#     } ],
#     "name" : "Hypnotized",
#     "release_date" : "2020-04-08",
#     "release_date_precision" : "day",
#     "total_tracks" : 1,
#     "type" : "album",
#     "uri" : "spotify:album:07UKVsstXPhVacXjjPJAJh"
#   },
#   "artists" : [ {
#     "external_urls" : {
#       "spotify" : "https://open.spotify.com/artist/2WBJQGf1bT1kxuoqziH5g4"
#     },
#     "href" : "https://api.spotify.com/v1/artists/2WBJQGf1bT1kxuoqziH5g4",
#     "id" : "2WBJQGf1bT1kxuoqziH5g4",
#     "name" : "Purple Disco Machine",
#     "type" : "artist",
#     "uri" : "spotify:artist:2WBJQGf1bT1kxuoqziH5g4"
#   }, {
#     "external_urls" : {
#       "spotify" : "https://open.spotify.com/artist/4FrXHrpbDLNyO3pbVv8RmF"
#     },
#     "href" : "https://api.spotify.com/v1/artists/4FrXHrpbDLNyO3pbVv8RmF",
#     "id" : "4FrXHrpbDLNyO3pbVv8RmF",
#     "name" : "Sophie and the Giants",
#     "type" : "artist",
#     "uri" : "spotify:artist:4FrXHrpbDLNyO3pbVv8RmF"
#   } ],
#   "available_markets" : [ "GB", "IE", "US" ],
#   "disc_number" : 1,
#   "duration_ms" : 195704,
#   "explicit" : false,
#   "external_ids" : {
#     "isrc" : "AUDCB1701555"
#   },
#   "external_urls" : {
#     "spotify" : "https://open.spotify.com/track/0OeFuOAu0P1ONYz5EDdqb2"
#   },
#   "href" : "https://api.spotify.com/v1/tracks/0OeFuOAu0P1ONYz5EDdqb2",
#   "id" : "0OeFuOAu0P1ONYz5EDdqb2",
#   "is_local" : false,
#   "name" : "Hypnotized",
#   "popularity" : 44,
#   "preview_url" : null,
#   "track_number" : 1,
#   "type" : "track",
#   "uri" : "spotify:track:0OeFuOAu0P1ONYz5EDdqb2"
# }%
