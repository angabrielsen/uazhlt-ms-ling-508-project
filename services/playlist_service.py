from models.playlist import Playlist
class PlaylistService:
    def add_track(self, playlist: Playlist, track_id: int):
        if not isinstance(track_id, int):
            raise TypeError("Track ID must be an integer")
        playlist.tracks.append(track_id)

    def remove_track(self, playlist: Playlist, track_id: int):
        playlist.tracks = [tid for tid in playlist.tracks if tid != track_id]
