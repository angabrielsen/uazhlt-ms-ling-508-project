class Track:
    def __init__(self, id, name, artist_name, uri):
        self.id = id
        self.name = name
        self.artist_name = artist_name
        self.uri = uri

    def __str__(self):
        return f'Track ID: {self.id}, Name: "{self.name}", Artist: {self.artist_name}, URI: {self.uri}'
