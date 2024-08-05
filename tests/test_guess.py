import pytest
from models.guess import *

def test_guess_creation():
    guess = Guess('Hypnotized', 'Purple Disco Machine')
    assert guess.title == 'Hypnotized'
    assert guess.artist == 'Purple Disco Machine'

def test_guess_str():
    guess = Guess('Hypnotized', 'Purple Disco Machine')
    assert str(guess) == 'Song: "Hypnotized" by Purple Disco Machine'

def test_empty_title():
    guess = Guess('', 'Purple Disco Machine')
    assert guess.title == ''
    assert guess.artist == 'Purple Disco Machine'
    assert str(guess) == 'Song: "" by Purple Disco Machine'

def test_empty_artist():
    guess = Guess('Hypnotized', '')
    assert guess.title == 'Hypnotized'
    assert guess.artist == ''
    assert str(guess) == 'Song: "Hypnotized" by '

def test_empty_title_and_artist():
    guess = Guess('', '')
    assert guess.title == ''
    assert guess.artist == ''
    assert str(guess) == 'Song: "" by '

if __name__ == '__main__':
    pytest.main()
