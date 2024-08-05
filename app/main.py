from db.mysql_repositry import MysqlRepository

def main():
    print("Welcome to the Music Maker App!")

    repository = MysqlRepository()

    tracks = repository.fetch_all_tracks()
    print("\nTracks:")
    for track in tracks:
        print(track)

    playlists = repository.fetch_all_playlists()
    print("\nPlaylists:")
    for playlist in playlists:
        print(playlist)

if __name__ == "__main__":
    main()
