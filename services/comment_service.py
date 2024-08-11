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
    def fetch_all_comments():
        try:
            return CommentService.repository.fetch_all_comments()
        except Exception as e:
            print(f"Database error: {str(e)}")
            raise
