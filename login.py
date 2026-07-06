import customtkinter as ctk
from tkinter import messagebox
import main
import ctypes

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

login = ctk.CTk()
login.title("Boomba - Login")
login.geometry("500x600")
login.configure(fg_color="#0d0d0d")
login.iconbitmap("assets/icon.ico")
login.resizable(False, False)
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("musicplayer.app")



# Main frame with rounded corners
main_frame = ctk.CTkFrame(master=login, fg_color="#1a1a1a", corner_radius=15)
main_frame.pack(padx=30, pady=30, fill="both", expand=True)

# Title
title_label = ctk.CTkLabel(
    master=main_frame,
    text="Welcome Back",
    text_color="#ffffff",
    font=ctk.CTkFont(family="SFNS Display Bold", size=36, weight="bold"),
)
title_label.pack(anchor="center", padx=20, pady=(40, 10))


# Username entry
username_label = ctk.CTkLabel(
    master=main_frame,
    text="Username",
    text_color="#ffffff",
    font=ctk.CTkFont(family="SFNS Display Bold", size=15, weight="bold"),
)
username_label.pack(anchor="w", padx=30, pady=(40, 8))

username = ctk.CTkEntry(
    master=main_frame,
    placeholder_text="Enter your username",
    height=45,
    border_width=2,
    border_color="#404040",
    fg_color="#262626",
    text_color="#ffffff",
    font=ctk.CTkFont(family="SFNS Display Bold", size=14),
    
)
username.pack(padx=30, pady=(0, 25), fill="x")

# Password entry
password_label = ctk.CTkLabel(
    master=main_frame,
    text="Password",
    text_color="#ffffff",
    font=ctk.CTkFont(family="SFNS Display Bold", size=15, weight="bold"),
)
password_label.pack(anchor="w", padx=30, pady=(0, 8))

password = ctk.CTkEntry(
    master=main_frame,
    placeholder_text="Enter your password",
    show="*",
    height=45,
    border_width=2,
    border_color="#404040",
    fg_color="#262626",
    text_color="#ffffff",
    font=ctk.CTkFont(family="SFNS Display Bold", size=14),
)
password.pack(padx=30, pady=(0, 30), fill="x")


def click():
    user = username.get().strip()
    pwd = password.get().strip()

    if not user or not pwd:
        messagebox.showerror("Login Error", "Please enter both username and password.")
        return

    if user != "Jeff" or pwd != "1234":
        messagebox.showerror("Login Error", "Invalid username or password.")
        return

    login.destroy()
    main.run_app()

# Login button
button = ctk.CTkButton(
    master=main_frame,
    text="Login",
    height=50,
    font=ctk.CTkFont(family="SFNS Display Bold", size=15, weight="bold"),
    fg_color="#1f7bef",
    hover_color="#1565c0",
    text_color="#ffffff",
    cursor="hand2",
    corner_radius=22,
    command=click
)
button.pack(padx=110, pady=(0, 20), fill="x")



login.mainloop()