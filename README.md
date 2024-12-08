# YouTube Playlist Sync

This script downloads audio from a YouTube playlist and pushes the files to a connected Android phone.

## Configuration

- `PLAYLIST_URL`: URL of the YouTube playlist to sync.
- `DOWNLOAD_DIR`: Directory to store downloaded audio files.
- `PHONE_PATH`: Path on the phone where the files will be pushed.
- `CHECK_INTERVAL`: Interval in seconds to check for new videos in the playlist.
- `PROCESSED_FILE`: File to store processed video URLs.
- `LOG_FILE`: File to store logs.

## Requirements

- Python 3.x
- `pytube`
- `yt-dlp`
- `adb` (Android Debug Bridge)

## Setup

1. Install the required Python packages:
    ```sh
    pip install pytube yt-dlp
    ```

2. Ensure `adb` is installed and added to your system's PATH.

3. Connect your Android phone via USB and enable USB debugging.

## Usage

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd youtube-sync
    ```

2. Run the script:
    ```sh
    python test.py
    ```

The script will periodically check the playlist for new videos, download the audio, and push the files to the specified path on your phone.

## Logging

Logs are stored in the file specified by `LOG_FILE` and optionally printed to the console.

## License

This project is licensed under the MIT License.