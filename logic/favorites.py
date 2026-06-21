from __future__ import annotations

from typing import List

from .models import Song


class FavoritesManager:
    """Track favorite songs by ID and expose filtered views."""

    def __init__(self) -> None:
        self._favorite_ids: set[str] = set()

    def add(self, song: Song) -> None:
        self._favorite_ids.add(song.id)

    def remove(self, song: Song) -> None:
        self._favorite_ids.discard(song.id)

    def toggle(self, song: Song) -> None:
        if self.is_favorite(song):
            self.remove(song)
        else:
            self.add(song)

    def is_favorite(self, song: Song) -> bool:
        return song.id in self._favorite_ids

    def list_favorites(self, songs: List[Song]) -> List[Song]:
        return [song for song in songs if song.id in self._favorite_ids]
