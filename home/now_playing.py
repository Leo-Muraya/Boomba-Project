import customtkinter as ctk

class NowPlaying:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, width=220, fg_color="#1a1a2e")
        self.frame.grid(row=0, column=2, sticky="nsew")
        self.frame.grid_propagate(False)

        self._build()

    def _build(self):
        # Title
        title = ctk.CTkLabel(
            self.frame,
            text="Now Playing",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        title.pack(pady=(20, 15), padx=20, anchor="w")

        # Album art placeholder
        self.album_art = ctk.CTkLabel(
            self.frame,
            text="🎵",
            width=160,
            height=160,
            fg_color="#2a2a4a",
            corner_radius=15,
            font=ctk.CTkFont(size=60)
        )
        self.album_art.pack(pady=(20, 25), padx = 20)

        # Song title
        self.song_label = ctk.CTkLabel(
            self.frame,
            text="No song playing",
            font=ctk.CTkFont(size=14, weight="bold"),
            wraplength=180
        )
        self.song_label.pack(pady=(0, 5), padx=15)

        # Artist name
        self.artist_label = ctk.CTkLabel(
            self.frame,
            text="Unknown Artist",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.artist_label.pack(pady=(0, 5))

        # Genre and duration
        self.meta_label = ctk.CTkLabel(
            self.frame,
            text="",
            font=ctk.CTkFont(size=11),
            text_color="#4a90d9"
        )
        self.meta_label.pack(pady=(0, 20))

    def update(self, song):
        """Call this method when a new song is selected"""
        self.song_label.configure(text=song.title)
        self.artist_label.configure(text=song.artist)
        self.meta_label.configure(text=f"{song.genre} • {song.duration}")