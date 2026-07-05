class Song:
    def __init__(self, title, artist, genre, duration="0.00"):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration

    def __repr__(self):
        return f"{self.title} - {self.artist} ({self.genre}, {self.duration})"

SONGS = [

    Song("Nzaza", "Asake", "Afrobeats", "3:03"),
    Song("Blackbirds", "Lancey Foux", "Hip Hop", "3:12"),
    Song("Face The Flame", "Yeat ft. YoungBoy Never Broke Again & Grimes", "Hip Hop", "2:50"),
    Song("Ensalada", "Freddie Gibbs & The Alchemist ft. Anderson .Paak", "Hip Hop", "3:20"),
    Song("Good Flirts", "Baby Keem ft. Kendrick Lamar & Momo Boyd", "Hip Hop", "3:40"),
    Song("Bazooka", "Miami XO", "Hip Hop", "2:15"),
    Song("You're the Best", "Joe Esposito", "Rock", "2:59"),
    Song("Chicago", "Michael Jackson", "Pop", "4:05"),
    Song("One Dance", "Drake ft. Wizkid & Kyla", "Afrobeats", "2:54"),
    Song("Ex-Factor", "Lauryn Hill", "R&B", "5:26"),
    Song("Fountains", "Drake ft. Tems", "Afrobeats", "3:12"),
    Song("Glamorous", "Fergie ft. Ludacris", "Pop", "4:03"),
    Song("Gin and Juice", "Snoop Dogg", "Hip Hop", "3:31"),
    Song("Hips Don't Lie", "Shakira ft. Wyclef Jean", "Pop", "3:38"),
    Song("Get Lucky", "Daft Punk ft. Pharrell Williams & Nile Rodgers", "Pop", "4:08"),
    Song("No One", "Alicia Keys", "R&B", "4:13"),
    Song("Sky", "Playboi Carti", "Hip Hop", "2:48"),
    Song("Last Friday Night (T.G.I.F.)", "Katy Perry", "Pop", "3:50"),
    Song("Umbrella", "Rihanna ft. JAY-Z", "Pop", "4:35"),
    Song("Waterfalls", "TLC", "R&B", "4:39"),
    Song("Magnolia", "Playboi Carti", "Hip Hop", "3:01"),
    Song("Firework", "Katy Perry", "Pop", "3:50"),
    Song("Diamonds", "Rihanna", "Pop", "3:45"),
    Song("No Scrubs", "TLC", "R&B", "3:36"),
    Song("Billie Jean", "Michael Jackson", "Pop", "4:54"),
    Song("God's Plan", "Drake", "Hip Hop", "3:18"),
    Song("Terminator", "Asake", "Afrobeats", "3:25"),
    Song("Empire State of Mind", "JAY-Z ft. Alicia Keys", "Hip Hop", "4:37"),
    Song("Waka Waka (This Time for Africa)", "Shakira ft. Freshlyground", "Pop", "3:22"),
    Song("Hot N Cold", "Katy Perry", "Pop", "3:40"),
    Song("Don't Stop the Music", "Rihanna", "Pop", "4:27"),
    Song("Stronger", "Kanye West", "Hip Hop", "5:12"),
    Song("Roses", "Kanye West", "Hip Hop", "4:06"),
    Song("All of the Lights", "Kanye West ft. Rihanna & Kid Cudi", "Hip Hop", "4:59"),
    Song("Natural High", "Freddie Gibbs", "Hip Hop", "3:31"),
    Song("SDP Interlude", "Travis Scott", "Hip Hop", "3:11"),
    Song("Antidote", "Travis Scott", "Hip Hop", "4:22"),
    Song("Lights", "Ellie Goulding", "Pop", "3:30"),
    Song("Lush Life", "Zara Larsson", "Pop", "3:21"),
    Song("No Role Modelz", "J. Cole", "Hip Hop", "4:52"),
]

FAVORITES = []

def add_favorite(title: str) -> str:
    song = find_song(title)
    if song is None:
        return f"ERROR: '{title}' not found in library."
    if song in FAVORITES:
        return f"'{song.title}' is already in your favorites."
    FAVORITES.append(song)
    return f"✓ '{song.title}' added to favorites."

def remove_favorite(title: str) -> str:
    song = find_song(title)
    if song is None:
        return f"ERROR: '{title}' not found in library."
    if song not in FAVORITES:
        return f"'{song.title}' is not in your favorites."
    FAVORITES.remove(song)
    return f"✓ '{song.title}' removed from favorites."

def show_favorites():
    if not FAVORITES:
        print("Your favorites list is empty")
    else:
        print("Your favorites:")
        for song in FAVORITES:
            print(f" - {song}")
