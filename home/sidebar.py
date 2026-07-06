import customtkinter as ctk


class Sidebar:
    def __init__(self, parent, on_open_add_song=None, on_explore=None, on_open_create_playlist=None, on_playlist_selected=None):
        self.frame = ctk.CTkFrame(master=parent, width=150, fg_color="#2d2d34")
        self.frame.grid(row=1, column=0, sticky="nsew", padx=(5, 0), pady=5)
        self.frame.grid_propagate(False)
        self.on_open_add_song = on_open_add_song
        self.on_explore = on_explore
        self.on_open_create_playlist = on_open_create_playlist
        self.on_playlist_selected = on_playlist_selected
        self.playlists = []

        self._build()

    def _show_all_songs(self):
        if self.on_explore:
            self.on_explore()

    def _show_playlist(self, playlist):
        if self.on_playlist_selected:
            self.on_playlist_selected(playlist)

    def refresh_playlists(self, playlists):
        self.playlists = playlists or []
        for widget in self.playlist_frame.winfo_children():
            widget.destroy()

        if not self.playlists:
            empty_label = ctk.CTkLabel(
                self.playlist_frame,
                text="No playlists yet",
                text_color="gray",
                font=ctk.CTkFont(size=11),
            )
            empty_label.pack(anchor="w", pady=2)
            return

        for playlist in self.playlists:
            btn = ctk.CTkButton(
                master=self.playlist_frame,
                text=playlist.name,
                anchor="w",
                fg_color="transparent",
                hover_color="#2a2a4a",
                font=ctk.CTkFont(family="SFNS Display Bold", size=14),
                command=lambda p=playlist: self._show_playlist(p),
            )
            btn.pack(fill="x", padx=(20, 10), pady=2)

    def _build(self):
        app_label = ctk.CTkLabel(master=self.frame, text="Your Library", font=ctk.CTkFont(size=18, weight="bold"))
        app_label.pack(pady=(30, 20), padx=20, anchor="w")

        explore_btn = ctk.CTkButton(
            master=self.frame,
            text="Explore",
            anchor="w",
            fg_color="transparent",
            hover_color="#2a2a4a",
            font=ctk.CTkFont(family="SFNS Display Bold", size=16),
            command=self._show_all_songs,
        )
        explore_btn.pack(fill="x", padx=(20, 10), pady=2)

        nav_buttons = ["Added Songs"]
        for btn_text in nav_buttons:
            btn = ctk.CTkButton(
                master=self.frame,
                text=btn_text,
                anchor="w",
                fg_color="transparent",
                hover_color="#2a2a4a",
                font=ctk.CTkFont(family="SFNS Display Bold", size=16),
            )
            btn.pack(fill="x", pady=2, padx=(20, 10))

        personal_buttons = ["Favorites", "Albums", "Genres"]
        for btn_text in personal_buttons:
            btn = ctk.CTkButton(
                master=self.frame,
                text=btn_text,
                anchor="w",
                fg_color="transparent",
                hover_color="#2a2a4a",
                font=ctk.CTkFont(family="SFNS Display Bold", size=16),
            )
            btn.pack(fill="x", padx=(20, 10), pady=2)

        playlist_label = ctk.CTkLabel(
            master=self.frame,
            text="Playlists",
            anchor="w",
            font=ctk.CTkFont(family="SFNS Display Bold", size=14, weight="bold"),
        )
        playlist_label.pack(fill="x", padx=(20, 10), pady=(10, 5))

        self.playlist_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        self.playlist_frame.pack(fill="x", padx=5, pady=2)

        add_song = ctk.CTkButton(
            master=self.frame,
            text="+ Add a song",
            anchor="w",
            fg_color="transparent",
            hover_color="#2a2a4a",
            font=ctk.CTkFont(family="SFNS Display Bold", size=13),
            command=lambda: self.on_open_add_song() if self.on_open_add_song else None,
        )
        add_song.pack(fill="x", padx=(5, 10), pady=(0, 5), side="bottom")

        create_playlist = ctk.CTkButton(
            master=self.frame,
            text="+ Create Playlist",
            anchor="w",
            fg_color="transparent",
            hover_color="#2a2a4a",
            font=ctk.CTkFont(family="SFNS Display Bold", size=13),
            command=lambda: self.on_open_create_playlist() if self.on_open_create_playlist else None,
        )
        create_playlist.pack(fill="x", padx=(5, 10), pady=(0, 5), side="bottom")

