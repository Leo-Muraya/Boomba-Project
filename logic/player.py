from __future__ import annotations

from typing import Optional

from .models import Song
from .playlist import Playlist


class Player:
    """A simple music player that uses a playlist as its queue."""

    def __init__(self, playlist: Playlist) -> None:
        self.playlist = playlist
        self.current_index: int = 0
        self.is_playing: bool = False

    @property
    def current_song(self) -> Optional[Song]:
        if 0 <= self.current_index < len(self.playlist):
            return self.playlist.songs()[self.current_index]
        return None

    def play(self, index: Optional[int] = None) -> Optional[Song]:
        if index is not None:
            if 0 <= index < len(self.playlist):
                self.current_index = index
        if self.current_song is None:
            return None
        self.is_playing = True
        return self.current_song

    def pause(self) -> None:
        self.is_playing = False

    def stop(self) -> None:
        self.is_playing = False
        self.current_index = 0

    def next(self) -> Optional[Song]:
        if len(self.playlist) == 0:
            return None
        self.current_index = min(self.current_index + 1, len(self.playlist) - 1)
        self.is_playing = True
        return self.current_song

    def previous(self) -> Optional[Song]:
        if len(self.playlist) == 0:
            return None
        self.current_index = max(self.current_index - 1, 0)
        self.is_playing = True
        return self.current_song
