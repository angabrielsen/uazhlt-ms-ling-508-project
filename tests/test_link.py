import pytest
from models.link import *

def test_valid_link():
    link = Link('http://www.reddit.com/r/music/some-post')
    assert isinstance(link, str)
    assert str(link) == 'http://www.reddit.com/r/music/some-post'

def test_invalid_link_prefix():
    with pytest.raises(ValueError):
        Link('http://www.example.com/r/music/some-post')

def test_link_without_prefix():
    with pytest.raises(ValueError):
        Link('http://www.reddit.com/r/other/some-post')

def test_link_with_correct_prefix():
    link = Link('http://www.reddit.com/r/music/another-post')
    assert isinstance(link, str)
    assert str(link) == 'http://www.reddit.com/r/music/another-post'

if __name__ == '__main__':
    pytest.main()
