import pygame
import os


class MusicPlayer:
    def __int__(self):
        # initializing the pygame
        
        pygame.mixer.init()
        
        self.current_song = None
        self.current_index = 0
        self.is_playing = False
        self.songs = []
        
    def load_library (self, songs):
        self.songs =  songs
        
        
    def play(self, song):
        
        # for playing a specific song
        
        if not os.path.exists(song.file_path):
            print(f"File not found: {song.file_path}")
            return
        
        self.current_song = song
        self.current_index = self.songs.index(song)
        self.is_playing = True
        