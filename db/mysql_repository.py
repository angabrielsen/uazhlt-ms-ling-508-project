import mysql.connector

class MysqlRepository:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'r_music_maker'
        }
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor(dictionary=True)
            self.create_tables()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None
            self.cursor = None

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create_tables(self):
        if self.connection and self.cursor:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS submissions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    submission_id VARCHAR(255) UNIQUE NOT NULL,
                    url VARCHAR(255) NOT NULL,
                    title VARCHAR(255) NOT NULL
                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS comments (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    submission_id VARCHAR(255),
                    comment_text TEXT,
                    FOREIGN KEY (submission_id) REFERENCES submissions(submission_id)
                )
            """)

    def fetch_all_submissions(self):
        if self.connection and self.cursor:
            query = "SELECT * FROM submissions"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        return []

    def save_submission(self, submission_id, url, title):
        if self.connection and self.cursor:
            query = """
                INSERT INTO submissions (submission_id, url, title)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE url = VALUES(url), title = VALUES(title)
            """
            self.cursor.execute(query, (submission_id, url, title))
            self.connection.commit()

    def save_comment(self, comment):
        if self.connection and self.cursor:
            query = """
                INSERT INTO comments (submission_id, comment_text)
                VALUES (%s, %s)
            """
            self.cursor.execute(query, (comment.submission_id, comment.comment_text))
            self.connection.commit()

    def fetch_comments_by_submission_id(self, submission_id):
        if self.connection and self.cursor:
            query = """
                SELECT comment_text FROM comments
                WHERE submission_id = %s
            """
            self.cursor.execute(query, (submission_id,))
            result = self.cursor.fetchall()
            return [row['comment_text'] for row in result]
        return []
