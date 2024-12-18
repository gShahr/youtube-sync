import os
import time
import subprocess
import json
import logging
import unicodedata
from pytube import Playlist
from yt_dlp import YoutubeDL

# Configuration
PLAYLIST_URL = "https://music.youtube.com/playlist?list=PLjBNkCPPfIQ7ZZ9tejPFiaNUaxWTMgBYC"
DOWNLOAD_DIR = "downloads"
PHONE_PATH = "/storage/emulated/0/Music/"
CHECK_INTERVAL = 600  # in seconds
PROCESSED_FILE = "processed_urls.json"
LOG_FILE = "playlist_downloader.log"

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Optional: to also log to the console
    ]
)

processed_urls = set()

def load_processed_urls():
    global processed_urls
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, "r") as file:
            processed_urls.update(json.load(file))
        logging.info("Loaded processed URLs from file.")

def save_processed_urls():
    with open(PROCESSED_FILE, "w") as file:
        json.dump(list(processed_urls), file)
    logging.info("Saved processed URLs to file.")

def fetch_playlist_videos(playlist_url):
    playlist = Playlist(playlist_url)
    return playlist.video_urls

def download_audio(video_url, output_dir):
    logging.info(f"Downloading audio for video: {video_url}")
    with YoutubeDL({'outtmpl': f'{output_dir}/%(title)s.%(ext)s'}) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        file_path = ydl.prepare_filename(info_dict)
    return file_path

def push_file_to_phone(file_path, phone_path):
    cmd = ["adb", "push", file_path, phone_path]
    logging.info(f"Pushing file to phone: {file_path}")
    subprocess.run(cmd, check=True)

def main():
    global processed_urls
    load_processed_urls()

    while True:
        logging.info("Checking playlist for new videos...")
        try:
            videos = fetch_playlist_videos(PLAYLIST_URL)
            for video in videos:
                if video not in processed_urls:
                    logging.info(f"New video found: {video}")
                    file_path = download_audio(video, DOWNLOAD_DIR)
                    push_file_to_phone(file_path, PHONE_PATH)
                    processed_urls.add(video)
                    save_processed_urls()

        except Exception as e:
            logging.error(f"Error occurred: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
