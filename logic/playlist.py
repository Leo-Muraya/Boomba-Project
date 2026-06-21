from __future__ import annotations

from typing import Iterable, List, Optional

from .models import Song


class Playlist:
    """A playlist of songs with ordering and duration utilities."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._songs: List[Song] = []

    def add_song(self, song: Song) -> None:
        self._songs.append(song)

    def remove_song(self, song_id: str) -> bool:
        for index, song in enumerate(self._songs):
            if song.id == song_id:
                del self._songs[index]
                return True
        return False

    def move_song(self, song_id: str, new_index: int) -> bool:
        if new_index < 0 or new_index >= len(self._songs):
            return False
        for index, song in enumerate(self._songs):
            if song.id == song_id:
                self._songs.insert(new_index, self._songs.pop(index))
                return True
        return False

    def find_song(self, song_id: str) -> Optional[Song]:
        for song in self._songs:
            if song.id == song_id:
                return song
        return None

    def songs(self) -> List[Song]:
        return list(self._songs)

    def total_duration(self) -> float:
        return sum(song.duration for song in self._songs)

    def __len__(self) -> int:
        return len(self._songs)

    def __iter__(self) -> Iterable[Song]:
        return iter(self._songs)
