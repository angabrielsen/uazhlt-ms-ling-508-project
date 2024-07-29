import mysql.connector
from db.repository import Repository

class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # Change to 'localhost' for local testing
            'port': '32000',  # Change to '32000' for local testing
            'database': 'tracks'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor(dictionary=True)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def fetch_all_tracks(self):
        query = "SELECT * FROM tracks"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

if __name__ == "__main__":
    repository = MysqlRepository()
    tracks = repository.fetch_all_tracks()
    for track in tracks:
        print(track)
