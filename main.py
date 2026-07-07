import customtkinter as ctk
import ctypes
from home.sidebar import Sidebar
from home.top_bar import TopBar
from home.player_bar import PlayerBar
from home.main_area import MainArea
from home.now_playing import NowPlaying
from logic.player import MusicPlayer
from logic.library import SONGS
from home.add_song import AddSongDialog
from home.create_playlist import CreatePlaylistDialog
from logic.playlist import PlaylistManager
from logic.favorites import add_favorite, get_favorites, remove_favorite


def run_app():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Boomba FM")
    app.geometry("1280x720")
    app.configure(fg_color="#000000")
    app.iconbitmap("assets/icon.ico")
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("musicplayer.app")

    # Grid configuration
    app.grid_rowconfigure(0, weight=0)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=0)
    app.grid_columnconfigure(0, weight=0)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=0, minsize=280)

    player = MusicPlayer()
    player.load_library(SONGS)

    playlist_manager = PlaylistManager()
    current_songs = SONGS
    current_view = "explore"

    top_bar = TopBar(app)
    now_playing = NowPlaying(app)
    main_area = MainArea(app)
    player_bar = PlayerBar(app)

    def on_song_added(new_song):
        SONGS.append(new_song)
        main_area._display_songs(SONGS)
        create_playlist_dialog.refresh_songs(SONGS)

    add_song_dialog = AddSongDialog(main_area.frame, on_song_added)

    def on_explore():
        nonlocal current_songs, current_view
        current_view = "explore"
        current_songs = SONGS
        player.load_library(current_songs)
        main_area._display_songs(current_songs)

    def on_playlist_selected(playlist):
        nonlocal current_songs, current_view
        current_view = "playlist"
        current_songs = playlist.songs
        player.load_library(current_songs)
        main_area._display_songs(current_songs)

    def on_playlist_created(name, songs):
        playlist = playlist_manager.create_playlist(name, songs)
        sidebar.refresh_playlists(playlist_manager.get_all_playlists())
        on_playlist_selected(playlist)

    def on_show_favorites():
        nonlocal current_songs, current_view
        current_view = "favorites"
        current_songs = get_favorites()
        player.load_library(current_songs)
        main_area._display_songs(current_songs, "No favorites yet")

    def on_favorite_toggled(song):
        nonlocal current_songs, current_view
        if song in get_favorites():
            remove_favorite(song.title)
        else:
            add_favorite(song)

        if current_view == "favorites":
            current_songs = get_favorites()
            main_area._display_songs(current_songs, "No favorites yet")
        else:
            main_area._display_songs(current_songs)

    create_playlist_dialog = CreatePlaylistDialog(main_area.frame, on_playlist_created, SONGS)
    sidebar = Sidebar(
        app,
        on_open_add_song=add_song_dialog.show,
        on_explore=on_explore,
        on_open_create_playlist=create_playlist_dialog.show,
        on_playlist_selected=on_playlist_selected,
        on_show_favorites=on_show_favorites,
    )

    def on_song_selected(song):
        print(f"Song selected: {song.title}")
        player.load_library(current_songs)
        player.play(song)
        now_playing.update(song)
        player_bar.song_title.configure(text=song.title)
        player_bar.artist_name.configure(text=song.artist)
        player_bar.play_btn.configure(image=player_bar.pause_icon)
        player_bar.update_album_art(song.image_path)

    def on_play_pause(event=None):
        player.toggle_play_pause()
        if player.is_playing:
            player_bar.play_btn.configure(image=player_bar.pause_icon)
        else:
            player_bar.play_btn.configure(image=player_bar.play_icon)
        return "break"

    def on_next():
        player.next_song()
        if player.current_song:
            on_song_selected(player.current_song)

    def on_previous():
        player.previous_song()
        if player.current_song:
            on_song_selected(player.current_song)

    def update_progress():
        if player.is_playing and player.current_song:
            position = player.get_position()
            length = player.song_length

            if length > 0:
                progress = position / length
                player_bar.progress_bar.set(progress)

                current_min = int(position // 60)
                current_sec = int(position % 60)
                player_bar.current_time.configure(text=f"{current_min}:{current_sec:02d}")

                total_min = int(length // 60)
                total_sec = int(length % 60)
                player_bar.total_time.configure(text=f"{total_min}:{total_sec:02d}")

                if position >= length - 0.5:
                    on_next()

        app.after(500, update_progress)

    def on_volume_change(value):
        player.set_volume(value)

    def on_seek(percentage):
        player.seek_to_percentage(percentage)

    def on_search(query):
        main_area.search_songs(query)

    player_bar.play_btn.configure(command=on_play_pause)
    player_bar.next_btn.configure(command=on_next)
    player_bar.previous_btn.configure(command=on_previous)
    player_bar.volume_slider.configure(command=on_volume_change)
    player_bar.on_seek = on_seek
    top_bar.on_search = on_search

    main_area.set_song_callback(on_song_selected)
    main_area.set_favorite_callback(on_favorite_toggled)

    app.bind("<space>", on_play_pause)

    update_progress()
    app.mainloop()


if __name__ == "__main__":
    run_app()
