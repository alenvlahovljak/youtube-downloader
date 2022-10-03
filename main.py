import pathlib
import pytube

VIDEO_URL = 'https://www.youtube.com/watch?v=_uQrJ0TkZlc'
PATH = f"{pathlib.Path().resolve()}/resources"

print(PATH)

try:
    youtube = pytube.YouTube(VIDEO_URL)
    video = youtube.streams.first()
    video.download(PATH)
    print("Download successfully!")
except Exception as e:
    print("Something went wrong !")
    print(e)
