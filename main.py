import customtkinter as ctk
from home.sidebar import Sidebar
from home.player_bar import PlayerBar
from home.main_area import MainArea
from home.now_playing import NowPlaying

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Boomba FM")
app.geometry("1100x680")
app.configure(fg_color = "#0d0d0d")

app.iconbitmap("logo3.ico")

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=0)
app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=0)

sidebar = Sidebar(app)
player_bar = PlayerBar(app)
main_area = MainArea(app)
now_playing = NowPlaying(app)

app.mainloop()