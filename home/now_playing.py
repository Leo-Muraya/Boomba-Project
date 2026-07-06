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

from PIL import Image
import os

class NowPlaying:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ctk.CTkFrame(parent, width=320, fg_color="#1a1a2e")
        self.frame.grid(row=1, column=2, sticky="nsew", padx=(0, 5), pady=5)
        self.frame.grid(row=1, column=2, sticky="nsew", padx=(0,5), pady=5)
        self.frame.grid_propagate(False)
        
        # Store current image to prevent garbage collection
        self.current_ctk_image = None
        
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
        self.album_art.pack(pady=(5, 15), padx=15)

        # Song title
        self.song_label = ctk.CTkLabel(
            self.frame,
            text="No song playing",
            font=ctk.CTkFont(family="SFNS Display Bold", size=25, weight="bold"),
            wraplength=270
        )
        self.song_label.pack(anchor="w", pady=(0, 2), padx=(13, 15))
            font=ctk.CTkFont(family=("SNFS Display Bold", "Arial"), size=24, weight="bold"),
            wraplength=250
        )
        self.song_label.pack(anchor="w", pady=(0,), padx=(25,15))

        # Artist name
        self.artist_label = ctk.CTkLabel(
            self.frame,
            text="Unknown Artist",
            font=ctk.CTkFont(family="SFNS Display Bold", size=16),
            text_color="gray"
        )
        self.artist_label.pack(pady=(0, 5), padx=(13, 15), anchor="w")
            font=ctk.CTkFont(family=("SNFS Display", "Arial"), size=15, weight="bold"),
            text_color="gray"
        )
        self.artist_label.pack(pady=(0, 5), padx=(25,15), anchor="w")

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
        self.meta_label.pack(pady=(0, 20))

    def load_image(self, image_path):
        """Load image from path and return CTkImage object"""
        try:
            if image_path and os.path.exists(image_path):
                # Open and resize image
                image = Image.open(image_path)
                # Convert to RGB if necessary (for PNG with alpha)
                if image.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', image.size, (42, 42, 74))  # #2a2a4a
                    background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                    image = background
                elif image.mode != 'RGB':
                    image = image.convert('RGB')
                
                # Create CTkImage
                ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(280, 280))
                return ctk_image
            return None
        except Exception as e:
            print(f"Error loading image from {image_path}: {e}")
            return None

    def update(self, song):
        """Update the display with a new song"""
        if not song:
            self.song_label.configure(text="No song playing")
            self.artist_label.configure(text="Unknown Artist")
            self.meta_label.configure(text="")
            self.album_art.configure(image=None, text="🎵")
            self.current_ctk_image = None
            return
            
        # Update text info
        self.song_label.configure(text=song.title)
        self.artist_label.configure(text=song.artist)
        self.meta_label.configure(text=f"{song.genre} • {song.duration}")
        
        # Load and display album art from the song's image_path
        if song.image_path:
            ctk_image = self.load_image(song.image_path)
            if ctk_image:
                # Store reference to prevent garbage collection
                self.current_ctk_image = ctk_image
                self.album_art.configure(image=ctk_image, text="")
                return
        
        # If no image loaded, show placeholder
        self.album_art.configure(image=None, text="🎵")
        self.current_ctk_image = None
