import os
from moviepy.editor import VideoFileClip
from pytube import YouTube
from dotenv import load_dotenv


def run(q):
    if "youtube.com" in q:
        download_from_youtube(q)
    else:
        for song in q.split(','):
            print("Searching: " + song)
            os.system('cd ' + os.getenv('output_dir') + ' & spotdl download "' + song + '"')

    print("===")


def download_from_youtube(q):
    filename = download_video(q)
    convert_to_mp3(filename)
    os.remove(filename)


def download_video(url):
    video = YouTube(url)
    stream = video.streams.get_by_itag(18)
    stream.download()
    return stream.default_filename


def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    mp3Name = filename[:-4] + ".mp3"
    clip.audio.write_audiofile(mp3Name)
    os.replace(mp3Name, os.getenv('output_dir') + '/' + mp3Name)
    clip.close()


if __name__ == "__main__":
    load_dotenv()
    print("Okay, let's go!")
    try:
        while True:
            run(input())
    except KeyboardInterrupt:
        pass
