import mysql.connector
from db.mysql_repository import MysqlRepository

class SubmissionService:
    repository = MysqlRepository()

    @staticmethod
    def save_submission(submission_id, url, title):
        try:
            SubmissionService.repository.save_submission(submission_id, url, title)
        except mysql.connector.Error as e:
            print(f"Database error: {str(e)}")
            raise

    @staticmethod
    def fetch_all_submissions():
        try:
            return SubmissionService.repository.fetch_all_submissions()
        except mysql.connector.Error as e:
            print(f"Database error: {str(e)}")
            raise
