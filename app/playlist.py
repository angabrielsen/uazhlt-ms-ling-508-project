from track import Track

class Playlist:
    def __init__(self, id, user_id, name, tracks=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.tracks = tracks if tracks is not None else []

    def add_track(self, track):
        if isinstance(track, Track):
            self.tracks.append(track)
        else:
            raise TypeError("Only Track instances can be added")

    def remove_track(self, track_id):
        self.tracks = [track for track in self.tracks if track.id != track_id]

    def __str__(self):
        track_list = ', '.join([str(track) for track in self.tracks])
        return f'Playlist ID: {self.id}, User ID: {self.user_id}, Name: "{self.name}", Tracks: [{track_list}]'
