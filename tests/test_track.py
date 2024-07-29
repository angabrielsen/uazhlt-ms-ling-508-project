import pytest
from app.track import Track

def test_track_creation():
    track = Track(1, 'Hypnotized', 'Purple Disco Machine', 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2')
    assert track.id == 1
    assert track.name == 'Hypnotized'
    assert track.artist_name == 'Purple Disco Machine'
    assert track.uri == 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2'

def test_track_str():
    track = Track(1, 'Hypnotized', 'Purple Disco Machine', 'spotify:track:0OeFuOAu0P1ONYz5EDdqb2')
    assert str(track) == 'Track ID: 1, Name: "Hypnotized", Artist: Purple Disco Machine, URI: spotify:track:0OeFuOAu0P1ONYz5EDdqb2'

def test_empty_attributes():
    track = Track(0, '', '', '')
    assert track.id == 0
    assert track.name == ''
    assert track.artist_name == ''
    assert track.uri == ''
    assert str(track) == 'Track ID: 0, Name: "", Artist: , URI: '

if __name__ == '__main__':
    pytest.main()
