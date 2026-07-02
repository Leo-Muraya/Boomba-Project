import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image, ImageDraw

def round_image(image_path, size, radius):
    """Returns a PIL image with rounded corners"""
    img = Image.open(image_path).resize(size)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), size], radius=radius, fill=255)
    img = img.convert("RGBA")
    img.putalpha(mask)
    return img


class PlayerBar:
    def __init__(self, parent):
        self.on_seek = None
        self.frame = ctk.CTkFrame(master=parent, height=80, fg_color="#000000")
        self.frame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=5, pady=(0, 5))
        self.frame.grid_propagate(False)
        self.frame.grid_columnconfigure(1, weight=1)

        self._build()

    def _build(self):
        # ── Left side ──────────────────────────────────
        left_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent", width=170)
        left_frame.grid(row=0, column=0, sticky="w", padx=8, pady=(1, 10))

        # Default album art thumbnail
        self.default_thumb = CTkImage(
           round_image("assets/images/cover.jpg", (55, 55), radius=4),
           size=(60, 60)
         )

        # Album art thumbnail
        self.album_thumb = ctk.CTkLabel(
            master=left_frame,
            text="",
            image=self.default_thumb,
            width=60,
            height=60,
            corner_radius=4,
        )
        self.album_thumb.pack(side="left", padx=(0, 10))

        song_info = ctk.CTkFrame(master=left_frame, fg_color="transparent")
        song_info.pack(side="left")

        self.song_title = ctk.CTkLabel(
            master=song_info,
            text="No Song",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=150,
            anchor="w"
        )
        self.song_title.pack(anchor="w")

        self.artist_name = ctk.CTkLabel(
            master=song_info,
            text="No Artist",
            font=ctk.CTkFont(family="SFNS Display Bold", size=12),
            text_color="gray"
        )
        self.artist_name.pack(anchor="w", pady = 0)

        # ── Center ─────────────────────────────────────
        center_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        center_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=10)
        center_frame.grid_propagate(False)

        controls_frame = ctk.CTkFrame(master=center_frame, fg_color="transparent")
        controls_frame.pack(pady=(0, 0))

        # Previous button
        prev_icon = CTkImage(Image.open("assets/images/prev.png"), size=(30, 26))
        self.prev_icon = prev_icon

        self.previous_btn = ctk.CTkButton(
            master=controls_frame,
            text="",
            image=self.prev_icon,
            width=20,
            height=20,
            fg_color="transparent",
            hover_color="#000000",
            corner_radius=25
        )
        self.previous_btn.pack(side="left", padx=0)

        # Play / Pause icons
        self.play_icon = CTkImage(Image.open("assets/images/play.png"), size=(35, 35))
        self.pause_icon = CTkImage(Image.open("assets/images/pause.png"), size=(35, 35))

        # Play button
        self.play_btn = ctk.CTkButton(
            controls_frame,
            text="",
            image=self.play_icon,
            width=20,
            height=20,
            fg_color="transparent",
            hover_color="#000000",
            corner_radius=25
        )
        self.play_btn.pack(side="left", padx=5)

        # Next button
        next_icon = CTkImage(Image.open("assets/images/next.png"), size=(30, 26))
        self.next_icon = next_icon

        self.next_btn = ctk.CTkButton(
            master=controls_frame,
            text="",
            image=self.next_icon,
            width=20,
            height=20,
            fg_color="transparent",
            hover_color="#000000",
            corner_radius=25
        )
        self.next_btn.pack(side="left", padx=0)

        # Progress bar and time
        progress_frame = ctk.CTkFrame(master=center_frame, fg_color="transparent", width=150)
        progress_frame.pack(fill="x", padx=50, anchor="center")

        self.current_time = ctk.CTkLabel(
            master=progress_frame,
            text="0:00",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        self.current_time.pack(side="left")

        self.progress_bar = ctk.CTkSlider(
            progress_frame,
            from_=0,
            to=1,
            fg_color="#2a2a4a",
            progress_color="#4a90d9",
            button_color="#4a90d9",
            button_hover_color="#357abd",
            height=12,
            command=self._on_seek_drag
        )
        self.progress_bar.pack(side="left", fill="x", expand=True, padx=10)
        self.progress_bar.set(0)

        self.total_time = ctk.CTkLabel(
            master=progress_frame,
            text="0:00",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        self.total_time.pack(side="left")

        # ── Right side — volume ────────────────────────
        right_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        right_frame.grid(row=0, column=2, sticky="e", padx=20, pady=10)

        speaker_icon = CTkImage(Image.open("assets/images/speaker.png"), size=(20, 20))
        self.speaker_icon = speaker_icon

        volume_label = ctk.CTkLabel(
            master=right_frame,
            text="",
            image=self.speaker_icon,
            font=ctk.CTkFont(size=14)
        )
        volume_label.pack(side="left", padx=(0, 8))

        self.volume_slider = ctk.CTkSlider(
            master=right_frame,
            width=120,
            from_=0,
            to=1,
            fg_color="#1b2841",
            progress_color="#2563eb"
        )
        self.volume_slider.pack(side="left")
        self.volume_slider.set(0.7)

    def update_album_art(self, image_path):
       try:
        img = CTkImage(round_image(image_path, (55, 55), radius=8), size=(55, 55))
        self.album_thumb.configure(image=img)
        self.album_thumb.image = img
       except:
        self.album_thumb.configure(image=self.default_thumb)

    def _on_seek_drag(self, value):
        if self.on_seek:
            self.on_seek(value)