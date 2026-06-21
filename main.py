from logic import FavoritesManager, MusicLibrary, Player, Playlist, Song


def main() -> None:
    library = MusicLibrary()

    songs = [
        Song(title="Sunny Side Up", artist="The Boombas", duration=3.2, album="Morning Drive", genre="Pop", year=2023),
        Song(title="Night Groove", artist="DJ Wave", duration=4.5, album="After Hours", genre="Electronic", year=2024),
        Song(title="Heartstrings", artist="Luna", duration=5.1, album="Open Skies", genre="Indie", year=2022),
    ]

    library.load_songs(songs)

    playlist = Playlist("Road Trip")
    playlist.add_song(songs[0])
    playlist.add_song(songs[2])

    favorites = FavoritesManager()
    favorites.add(songs[1])
    favorites.add(songs[2])

    player = Player(playlist)
    player.play()

    print("Library songs:")
    for song in library.list_songs():
        print(f"- {song}")

    print("\nPlaylist:")
    for song in playlist.songs():
        print(f"- {song}")

    print("\nFavorite songs:")
    for song in favorites.list_favorites(library.list_songs()):
        print(f"- {song}")

    print("\nNow playing:", player.current_song)
    player.next()
    print("Next song:", player.current_song)


if __name__ == "__main__":
    main()
