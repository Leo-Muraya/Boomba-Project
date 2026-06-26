import customtkinter as ctk

class Sidebar:
    def __init__(self, parent):
        # sidebar frame
        self.frame = ctk.CTkFrame(master=parent, width=150, fg_color = "#1a1a2e")
        self.frame.grid(row=0, column=0, sticky="nsew", padx =(5,0), pady= 5)
        self.frame.grid_propagate(False)

        self._build()
    
    def _build(self):
        #App title
        app_label = ctk.CTkLabel(master= self.frame , text = "App", font= ctk.CTkFont(size= 18, weight="bold"))
        app_label.pack(pady = (20 ,30), padx =20, anchor= "w")

        #nav buttons

        nav_buttons = ["Explore", "Suggest", "Top Chart", "New Stuff"]

        for btn_text in nav_buttons:
            btn = ctk.CTkButton(
                master= self.frame,
                text= btn_text,
                anchor = "w",
                fg_color="transparent",
                hover_color ="#2a2a4a",
                font=ctk.CTkFont(size = 13)
            )

            btn.pack(fill="x", pady = 2, padx =10)
        
        #personal section label

        personal_label = ctk.CTkLabel(master = self.frame, text ="Personal", font= ctk.CTkFont(size = 11), text_color="gray")
        personal_label.pack(pady = (20, 5), padx = 20, anchor = "w")

        #personal buttons

        personal_buttons = ["Favorites", "Albums", "Playlist" , "Genres"]
        for btn_text in personal_buttons:
            btn = ctk.CTkButton(
                master = self.frame,
                text = btn_text,
                anchor = "w",
                fg_color="transparent",
                hover_color="#2a2a4a",
                font=ctk.CTkFont(size = 13)
            )
            btn.pack(fill = "x",padx = 10, pady = 2)

        
        #playlist button at the bottom
        create_playlist = ctk.CTkButton(master = self.frame, 
                                        text ="+ Create Playlist", 
                                        anchor = "w",
                                        fg_color="transparent",
                                        hover_color="#2a2a4a",
                                        font = ctk.CTkFont(size = 13)
                                        )
        create_playlist.pack(fill = "x", padx= 10, pady=20, side ="bottom")

