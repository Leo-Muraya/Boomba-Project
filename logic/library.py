
import os
from playsound import playsound 

# 1. Setup our basic song collection list

music_library = [
    {"id": 1, "title": "lofi chill", "artist": "sleepy head", "file_path": r"C:\Users\kariu\Documents\project\Boomba-Project\logic\music\chill.mp3.mp3"},
    {"id": 2, "title": "Background Beat", "artist": "Artist B", "file_path":r"C:\Users\kariu\Documents\project\Boomba-Project\logic\music\background beat.mp3"},

]

print("Welcome to BOOMBA FM Music Player!")

# 2. Main interactive loop
while True:
    print("\n----- MENU -----")
    print("1. View your library")
    print("2. Add a new song")
    print("3. Play real music")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")

    # Option 1: View you library
    if choice == "1":
        print("\n--- YOUR SONGS ---")
        for song in music_library:
            print(f"[{song['id']}] {song['title']} by {song['artist']}")
            print(f"    File: {song['file_path']}")
            input("\nPress Enter to return to the menu...")
            
    # Option 2: Add a new song to the list
    elif choice == "2":
        print("\n---ADD NEW SONG---")
        new_title = input("Enter song title: ")
        new_artist = input("Enter artist name: ")
        new_path = input("Enter file path (Example: music/track.mp3): ").replace('"','').strip()

        new_id = len(music_library) + 1

        if os.path.exists(new_path):
            new_song = {"id": new_id, "title": new_title, "artist": new_artist, "file_path": new_path}
            music_library.append(new_song)
            print(f"Added {new_title} successfully!")
        else:
            print("Error: could not find file at that path.")
        input("\nPress Enter to return to the menu...")

    # Option 3: Play real music using playsound
    elif choice == "3":
        print("\n--PLAY MUSIC-- ")
        song_id_input = input("Enter the song ID you want to play: ")
        chosen_id = int(song_id_input)

        found = False
        full_windows_path = None
        for song in music_library:
            if song["id"] == chosen_id:
                found = True
                print(f"\n Trying to play: {song['title']} ")
                full_windows_path = os.path.abspath(song["file_path"])
                break

        if found and full_windows_path and os.path.exists(full_windows_path):
            print(f"Playing: {song['title']}")
            playsound(full_windows_path)
            print("Song finished playing!")
        else:
            if found:
                print("\n ERROR: Python cannot find that file!")
                print(f"Please check your spelling. Looked for: '{full_windows_path}'")
            else:
                print("\n ERROR: Song not found!")
        input("\nPress Enter to return to the menu...")

    # Option 4: Close the  music player
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
        input("\nPress Enter to return to menu...")