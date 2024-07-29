import mysql.connector

class MysqlRepository():
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # Change to 'localhost' for local testing
            'port': '32000',  # Change to '32000' for local testing
            'database': 'r_music_maker'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor(dictionary=True)
        self.create_tables()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tracks (
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                artist_name VARCHAR(255) NOT NULL,
                uri VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS playlists (
                id INT NOT NULL AUTO_INCREMENT,
                user_id INT NOT NULL,
                name VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
            )
        """)

    def fetch_all_tracks(self):
        query = "SELECT * FROM tracks"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def fetch_all_playlists(self):
        query = "SELECT * FROM playlists"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


if __name__ == "__main__":
    repository = MysqlRepository()
    tracks = repository.fetch_all_tracks()
    playlists = repository.fetch_all_playlists()

    print("Tracks:")
    for track in tracks:
        print(track)

    print("\nPlaylists:")
    for playlist in playlists:
        print(playlist)
