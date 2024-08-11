from db.mysql_repository import MysqlRepository
from models.comment import Comment

class CommentService:
    repository = MysqlRepository()

    @staticmethod
    def save_comments(submission_id, comments):
        try:
            for comment_text in comments:
                comment = Comment(submission_id, comment_text)
                CommentService.repository.save_comment(comment)
        except Exception as e:
            print(f"Error saving comments: {str(e)}")
            raise

    @staticmethod
    def fetch_comments_by_submission_id(submission_id):
        try:
            repo = MysqlRepository()
            comments = repo.fetch_comments_by_submission_id(submission_id)
            return comments
        except Exception as e:
            raise Exception(f"Error fetching comments: {str(e)}")
