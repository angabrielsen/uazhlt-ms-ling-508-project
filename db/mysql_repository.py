import mysql.connector  # Ensure this import is correct

class MysqlRepository:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'r_music_maker'
        }
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor(dictionary=True)
        self.create_tables()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS submissions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                submission_id VARCHAR(255) UNIQUE NOT NULL,
                url VARCHAR(255) NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                submission_id VARCHAR(255),
                comment_text VARCHAR(1000),
                FOREIGN KEY (submission_id) REFERENCES submissions(submission_id)
            )
        """)

    def fetch_all_submissions(self):
        query = "SELECT * FROM submissions"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def fetch_all_comments(self):
        query = "SELECT * FROM comments"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def save_submission(self, submission_id, url):
        query = "INSERT INTO submissions (submission_id, url) VALUES (%s, %s)"
        self.cursor.execute(query, (submission_id, url))
        self.connection.commit()
