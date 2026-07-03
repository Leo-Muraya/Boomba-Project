from dataclasses import dataclass, field
from typing import List


@dataclass
class Playlist:
    name: str
    songs: List[object] = field(default_factory=list)


class PlaylistManager:
    def __init__(self):
        self.playlists: List[Playlist] = []

    def create_playlist(self, name: str, songs: List[object]) -> Playlist:
        playlist = Playlist(name=name, songs=songs)
        self.playlists.append(playlist)
        return playlist

    def get_playlist(self, name: str):
        for playlist in self.playlists:
            if playlist.name.lower() == name.lower():
                return playlist
        return None

    def get_all_playlists(self) -> List[Playlist]:
        return self.playlists
