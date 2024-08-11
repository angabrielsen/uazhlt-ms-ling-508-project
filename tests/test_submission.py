import pytest
from models.submission import Submission

def test_submission_creation():
    submission = Submission(id=1, submission_id='abc123', url='https://www.reddit.com/r/example/comments/abc123/')
    assert submission.id == 1
    assert submission.submission_id == 'abc123'
    assert submission.url == 'https://www.reddit.com/r/example/comments/abc123/'

def test_submission_str():
    submission = Submission(id=1, submission_id='abc123', url='https://www.reddit.com/r/example/comments/abc123/')
    expected_str = 'Submission ID: abc123, URL: "https://www.reddit.com/r/example/comments/abc123/", ID: 1'
    assert str(submission) == expected_str


if __name__ == '__main__':
    pytest.main()
