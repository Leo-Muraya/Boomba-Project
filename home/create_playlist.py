import customtkinter as ctk
from tkinter import BooleanVar


class CreatePlaylistDialog:
    def __init__(self, parent, on_playlist_created, available_songs):
        self.parent = parent
        self.on_playlist_created = on_playlist_created
        self.available_songs = available_songs or []

        self.frame = ctk.CTkScrollableFrame(
            parent,
            bg_color="transparent",
            fg_color="#000000",
            corner_radius=25,
            border_width=1,
            border_color="#2a2a4a",
        )

        self._build()

    def _build(self):
        close_btn = ctk.CTkButton(
            self.frame,
            text="✕",
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#2a2a4a",
            command=self.hide,
        )
        close_btn.pack(anchor="ne", padx=10, pady=10)

        ctk.CTkLabel(
            self.frame,
            text="Create Playlist",
            font=ctk.CTkFont(size=18, weight="bold"),
        ).pack(pady=(0, 15))

        ctk.CTkLabel(self.frame, text="Playlist Name", anchor="w").pack(fill="x", padx=40)
        self.name_entry = ctk.CTkEntry(
            master=self.frame,
            placeholder_text="Enter playlist name",
            font=ctk.CTkFont(family="San Fransisco Display Bold", weight="bold", size=13),
        )
        self.name_entry.pack(fill="x", padx=40, pady=(5, 15))

        ctk.CTkLabel(self.frame, text="Choose songs", anchor="w").pack(fill="x", padx=40)
        self.song_frame = ctk.CTkScrollableFrame(self.frame, fg_color="transparent", height=220)
        self.song_frame.pack(fill="x", padx=20, pady=(5, 15))

        self.song_vars = []
        self._populate_song_options()

        self.message_label = ctk.CTkLabel(
            self.frame,
            text="",
            text_color="red",
            font=ctk.CTkFont(size=11),
        )
        self.message_label.pack(pady=(0, 10))

        create_btn = ctk.CTkButton(
            self.frame,
            text="Create Playlist",
            command=self._create_playlist,
            fg_color="#4a90d9",
            hover_color="#357abd",
        )
        create_btn.pack(pady=(0, 20))

    def refresh_songs(self, songs):
        self.available_songs = songs or []
        self._populate_song_options()

    def _populate_song_options(self):
        for widget in self.song_frame.winfo_children():
            widget.destroy()

        self.song_vars = []
        for song in self.available_songs:
            var = BooleanVar(value=False)
            checkbox = ctk.CTkCheckBox(
                self.song_frame,
                text=f"{song.title} — {song.artist}",
                variable=var,
                onvalue=True,
                offvalue=False,
                fg_color="#4a90d9",
            )
            checkbox.pack(anchor="w", pady=2)
            self.song_vars.append((song, var))

    def _create_playlist(self):
        name = self.name_entry.get().strip()
        selected_songs = [song for song, var in self.song_vars if var.get()]

        if not name:
            self.message_label.configure(text="Please enter a playlist name")
            return

        if not selected_songs:
            self.message_label.configure(text="Please pick at least one song")
            return

        self.on_playlist_created(name, selected_songs)
        self.hide()

    def show(self):
        self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.72, relheight=0.8)
        self.frame.lift()

    def hide(self):
        self.frame.place_forget()
        self.message_label.configure(text="")
        self.name_entry.delete(0, "end")
        for _, var in self.song_vars:
            var.set(False)
