#The backbone of my code
import uuid #Give a song a unique ID number
import json #Acts as a translator
#Converting Song to dictionary format
class Song:
    def __init__(self, file_path: str, title: str, artist: str, album: str, length: float, genre: str):
        # Essential data from my data plan
        self.id = str(uuid.uuid4())  # Generates unique id automatically
        self.file_path = file_path
        self.title = title
        self.artist = artist
        self.album = album
        self.length = float(length)  # stored in seconds
        self.genre = genre

    def to_dict(self):
        """Converts the object to a dictionary for JSON saving."""
        return self.__dict__


#  (Managing the list of songs)
class MusicLibrary:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.songs = []  # Will hold a list of Song objects since it is empty

    def add_song(self, file_path: str, title: str, artist: str, album: str, length: float, genre: str):
        new_song = Song(file_path, title, artist, album, length, genre)
        self.songs.append(new_song)#places my new song to my collection
        self.save_to_file()
        print(f"Added: {title} (id: {new_song.id})")#Output it should bring when i save

    def save_to_file(self):
        # converts the list of objects to list of dictionaries for JSON
        data = [s.to_dict() for s in self.songs]
        with open(self.filename, 'w', encoding='utf-8') as f:#opens my library.jsonfile 
            json.dump(data, f, indent=4)#Takes list of dictionaries and writes them to file 'f'

