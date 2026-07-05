# Boomba-FM

Boomba-FM is a desktop music player built with Python and CustomTkinter. It provides a graphical interface for browsing a song library, playing audio, creating playlists, and adding new songs.

## Features

- CustomTkinter-based desktop interface
- Song library with metadata for title, artist, genre, and duration
- Play, pause, next, previous controls
- Volume control and seek/progress support
- Playlist creation and playlist selection
- Add new MP3 files to the library
- Now playing panel with song metadata and cover art support

## Project Structure

- `main.py` - Application entry point. Initializes the player, UI components, and event callbacks.
- `login.py` - Login screen module (currently contains the login UI and references the main app entry point).
- `logic/` - Core application logic:
  - `library.py` - Song model and initial song definitions.
  - `player.py` - Audio playback logic using `pygame` and `mutagen`.
  - `playlist.py` - Playlist data model and playlist manager.
  - `favorites.py` - Favorites logic placeholder.
- `home/` - Custom UI components and dialogs:
  - `sidebar.py` - Library sidebar and playlist navigation.
  - `top_bar.py` - Top navigation bar with search field.
  - `player_bar.py` - Playback controls, progress bar, and volume slider.
  - `main_area.py` - Song list display and click handling.
  - `now_playing.py` - Currently playing song panel.
  - `add_song.py` - Dialog for adding new songs to the library.
  - `create_playlist.py` - Dialog for creating new playlists.
- `assets/` - Static files including images and song files.

## Dependencies

The application depends on the following Python packages:

- `customtkinter`
- `pygame`
- `mutagen`
- `Pillow`

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the environment:

- Windows PowerShell:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- Windows Command Prompt:
  ```cmd
  .\venv\Scripts\activate.bat
  ```

3. Install dependencies:

```bash
pip install customtkinter pygame mutagen pillow
```

## Running the App

Start the main application from the workspace root:

```bash
python main.py 
```
or 

```bash
python3 main.py 
```
If you want to run the login screen directly, use:

```bash
python login.py
```

## Usage

- Browse the song library from the main area.
- Click any song row to load and play that song.
- Use the playback bar to pause, resume, skip forward, or skip backward.
- Adjust volume with the slider.
- Create playlists from available songs using the playlist dialog.
- Add new songs by selecting an MP3 file from your system.
- Use the search field to filter songs by title, artist, or genre.

## Notes

- Song files are referenced using the `file_path` property in `logic/library.py`.
- The application uses `pygame.mixer` for audio playback and `mutagen` to read MP3 duration metadata.

## Future Improvements

- Add authentication and secure login flow.
- Store playlists and library entries persistently.
- Improve error handling for missing or unsupported audio files.
- Enhance UI elements, including better album art loading and themed controls.

