from logic.library import SONGS

FAVORITES = []


def find_song(title):
    for song in SONGS:
        if song.title.lower() == title.lower():
            return song
    return None


def add_favorite(song_or_title):
    if isinstance(song_or_title, str):
        song = find_song(song_or_title)
    else:
        song = song_or_title

    if song is None:
        return f"ERROR: '{song_or_title}' not found in library."
    if song in FAVORITES:
        return f"'{song.title}' is already in your favorites."

    FAVORITES.append(song)
    return f"'{song.title}' added to favorites."


def remove_favorite(song_or_title):
    if isinstance(song_or_title, str):
        song = find_song(song_or_title)
    else:
        song = song_or_title

    if song is None:
        return f"ERROR: '{song_or_title}' not found in library."
    if song not in FAVORITES:
        return f"'{song.title}' is not in your favorites."

    FAVORITES.remove(song)
    return f"'{song.title}' removed from favorites."


def is_favorite(song):
    return song in FAVORITES


def get_favorites():
    return list(FAVORITES)


def show_favorites():
    return list(FAVORITES)
