import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

def round_image(image_path, size, radius):
    """Returns a PIL image with rounded corners"""
    img = Image.open(image_path).resize(size)
    
    # Create a rounded mask
    mask = Image.new("L", size, 0)
    from PIL import ImageDraw
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), size], radius=radius, fill=255)
    
    # Apply mask to image
    img = img.convert("RGBA")
    img.putalpha(mask)
    
    return img


class NowPlaying:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, width=320, fg_color="#1a1a2e")
        self.frame.grid(row=1, column=2, sticky="nsew", padx=(0, 5), pady=5)
        self.frame.grid_propagate(False)

        self._build()

    def _build(self):
        # Title
        title = ctk.CTkLabel(
            self.frame,
            text="Now Playing",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        title.pack(pady=(20, 5), padx=25, anchor="w")

        # Default album art
        self.default_image = CTkImage(
          round_image("assets/images/cover.jpg", (280, 280), radius=10),
          size=(280, 280)
)

        # Album art
        self.album_art = ctk.CTkLabel(
            self.frame,
            text="",
            image=self.default_image,
            width=280,
            height=280,
            corner_radius=12,
        )
        self.album_art.pack(pady=(5, 15), padx=0)

        # Song title
        self.song_label = ctk.CTkLabel(
            self.frame,
            text="No song playing",
            font=ctk.CTkFont(family="SFNS Display Bold", size=25, weight="bold"),
            wraplength=270
        )
        self.song_label.pack(anchor="w", pady=(0, 2), padx=(13, 15))

        # Artist name
        self.artist_label = ctk.CTkLabel(
            self.frame,
            text="Unknown Artist",
            font=ctk.CTkFont(family="SFNS Display Bold", size=16),
            text_color="gray"
        )
        self.artist_label.pack(pady=(0, 5), padx=(13, 15), anchor="w")

        # Genre and duration
        self.meta_label = ctk.CTkLabel(
            self.frame,
            text="",
            font=ctk.CTkFont(size=11),
            text_color="#4a90d9"
        )
        self.meta_label.pack(pady=(0, 20), padx=(25, 15), anchor="w")

    def update(self, song):
        """Update when a new song is selected"""
        self.song_label.configure(text=song.title)
        self.artist_label.configure(text=song.artist)
        self.meta_label.configure(text=f"{song.genre} • {song.duration}")

        # Load album art
        if song.image_path:
            try:
                img = CTkImage(Image.open(song.image_path), size=(280, 280))
                self.album_art.configure(image=img)
                self.album_art.image = img  # prevent garbage collection
            except:
                self.album_art.configure(image=self.default_image)