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

# {
#   "album" : {
#     "album_type" : "album",
#     "artists" : [ {
#       "external_urls" : {
#         "spotify" : "https://open.spotify.com/artist/6DIS6PRrLS3wbnZsf7vYic"
#       },
#       "href" : "https://api.spotify.com/v1/artists/6DIS6PRrLS3wbnZsf7vYic",
#       "id" : "6DIS6PRrLS3wbnZsf7vYic",
#       "name" : "WALK THE MOON",
#       "type" : "artist",
#       "uri" : "spotify:artist:6DIS6PRrLS3wbnZsf7vYic"
#     } ],
#     "available_markets" : [ "AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ", "DK", "DO", "DE", "EC", "EE", "SV", "FI", "FR", "GR", "GT", "HN", "HK", "HU", "IS", "IE", "IT", "LV", "LT", "LU", "MY", "MT", "MX", "NL", "NZ", "NI", "NO", "PA", "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES", "SE", "CH", "TW", "TR", "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP", "TH", "VN", "RO", "IL", "ZA", "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS", "IN", "BY", "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "BD", "PK", "LK", "GH", "KE", "NG", "TZ", "UG", "AG", "AM", "BS", "BB", "BZ", "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM", "GE", "GD", "GW", "GY", "HT", "JM", "KI", "LS", "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR", "NE", "PW", "PG", "PR", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN", "LC", "VC", "SR", "TL", "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ", "GA", "GN", "KG", "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ", "MG", "MU", "MZ", "AO", "CI", "DJ", "ZM", "CD", "CG", "IQ", "LY", "TJ", "VE", "ET", "XK" ],
#     "external_urls" : {
#       "spotify" : "https://open.spotify.com/album/3mNoFlD1wsoXfkljfFzExT"
#     },
#     "href" : "https://api.spotify.com/v1/albums/3mNoFlD1wsoXfkljfFzExT",
#     "id" : "3mNoFlD1wsoXfkljfFzExT",
#     "images" : [ {
#       "height" : 640,
#       "url" : "https://i.scdn.co/image/ab67616d0000b27343294cfa2688055c9d821bf3",
#       "width" : 640
#     }, {
#       "height" : 300,
#       "url" : "https://i.scdn.co/image/ab67616d00001e0243294cfa2688055c9d821bf3",
#       "width" : 300
#     }, {
#       "height" : 64,
#       "url" : "https://i.scdn.co/image/ab67616d0000485143294cfa2688055c9d821bf3",
#       "width" : 64
#     } ],
#     "name" : "TALKING IS HARD",
#     "release_date" : "2014-12-02",
#     "release_date_precision" : "day",
#     "total_tracks" : 12,
#     "type" : "album",
#     "uri" : "spotify:album:3mNoFlD1wsoXfkljfFzExT"
#   },
#   "artists" : [ {
#     "external_urls" : {
#       "spotify" : "https://open.spotify.com/artist/6DIS6PRrLS3wbnZsf7vYic"
#     },
#     "href" : "https://api.spotify.com/v1/artists/6DIS6PRrLS3wbnZsf7vYic",
#     "id" : "6DIS6PRrLS3wbnZsf7vYic",
#     "name" : "WALK THE MOON",
#     "type" : "artist",
#     "uri" : "spotify:artist:6DIS6PRrLS3wbnZsf7vYic"
#   } ],
#   "available_markets" : [ "AR", "AU", "AT", "BE", "BO", "BR", "BG", "CA", "CL", "CO", "CR", "CY", "CZ", "DK", "DO", "DE", "EC", "EE", "SV", "FI", "FR", "GR", "GT", "HN", "HK", "HU", "IS", "IE", "IT", "LV", "LT", "LU", "MY", "MT", "MX", "NL", "NZ", "NI", "NO", "PA", "PY", "PE", "PH", "PL", "PT", "SG", "SK", "ES", "SE", "CH", "TW", "TR", "UY", "US", "GB", "AD", "LI", "MC", "ID", "JP", "TH", "VN", "RO", "IL", "ZA", "SA", "AE", "BH", "QA", "OM", "KW", "EG", "MA", "DZ", "TN", "LB", "JO", "PS", "IN", "BY", "KZ", "MD", "UA", "AL", "BA", "HR", "ME", "MK", "RS", "SI", "BD", "PK", "LK", "GH", "KE", "NG", "TZ", "UG", "AG", "AM", "BS", "BB", "BZ", "BT", "BW", "BF", "CV", "CW", "DM", "FJ", "GM", "GE", "GD", "GW", "GY", "HT", "JM", "KI", "LS", "LR", "MW", "MV", "ML", "MH", "FM", "NA", "NR", "NE", "PW", "PG", "PR", "WS", "SM", "ST", "SN", "SC", "SL", "SB", "KN", "LC", "VC", "SR", "TL", "TO", "TT", "TV", "VU", "AZ", "BN", "BI", "KH", "CM", "TD", "KM", "GQ", "SZ", "GA", "GN", "KG", "LA", "MO", "MR", "MN", "NP", "RW", "TG", "UZ", "ZW", "BJ", "MG", "MU", "MZ", "AO", "CI", "DJ", "ZM", "CD", "CG", "IQ", "LY", "TJ", "VE", "ET", "XK" ],
#   "disc_number" : 1,
#   "duration_ms" : 240000,
#   "explicit" : false,
#   "external_ids" : {
#     "isrc" : "USRC11402591"
#   },
#   "external_urls" : {
#     "spotify" : "https://open.spotify.com/track/71wT7aMCFPYfzutF66OLac"
#   },
#   "href" : "https://api.spotify.com/v1/tracks/71wT7aMCFPYfzutF66OLac",
#   "id" : "71wT7aMCFPYfzutF66OLac",
#   "is_local" : false,
#   "name" : "Aquaman",
#   "popularity" : 38,
#   "preview_url" : "https://p.scdn.co/mp3-preview/894c9229abdee24ac32e6a7afe87ab710417da37?cid=ba0253fce4b54077895c758661a02dc9",
#   "track_number" : 12,
#   "type" : "track",
#   "uri" : "spotify:track:71wT7aMCFPYfzutF66OLac"
# }%
