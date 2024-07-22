class Guess:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f'Song: "{self.title}" by {self.artist}'
