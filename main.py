import os
import re
from pytube import YouTube

video_url = input("Enter the YouTube video URL: ")
download_path = input("Enter the download path: ")

# Use regular expression to match the YouTube link pattern
regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$'
if not re.match(regex, video_url):
    print("Error: Invalid YouTube video URL")
else:
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    file_name = video.default_filename
    file_path = os.path.join(download_path, file_name)
    video.download(output_path=download_path, filename=file_name)
    print(f"The video has been downloaded to: {file_path}")
