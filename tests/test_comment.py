import pytest
from unittest.mock import MagicMock, patch
from services.comment_service import CommentService
from models.comment import Comment
@pytest.fixture
def mock_repository():
    with patch('services.comment_service.MysqlRepository') as MockRepository:
        mock_repo = MockRepository.return_value
        yield mock_repo


# def test_save_comments(mock_repository):
#     submission_id = '123abc'
#     comments = ['Great post!', 'Very informative.']
#
#     mock_repository.save_comment = MagicMock()
#
#     CommentService.save_comments(submission_id, comments)
#
#     assert mock_repository.save_comment.call_count == len(comments)
#
#     for comment_text in comments:
#         comment = Comment(submission_id, comment_text)
#         mock_repository.save_comment.assert_any_call(comment)


def test_fetch_comments_by_submission_id(mock_repository):
    submission_id = '123abc'
    expected_comments = ['Great post!', 'Very informative.']

    mock_repository.fetch_comments_by_submission_id = MagicMock(return_value=expected_comments)

    comments = CommentService.fetch_comments_by_submission_id(submission_id)

    assert comments == expected_comments
    mock_repository.fetch_comments_by_submission_id.assert_called_once_with(submission_id)