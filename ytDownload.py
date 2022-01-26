from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

vidQualities = [
    "240p",
    "360p",
    "480p",
    "720p",
    "1080p",
    "1440p",
    "2160p"
]

print("format type(default mp4): \n0) mp4\n1) mp3 \ntype number to choose")
format = input("format = ").strip()

if (format == '1'):
    print("\nmp3 chosen")
    format = 1
else:
    print("\nmp4 chosen")
    format = 0

quality = "unchosen"
if (format == 0):
    print('\n')
    print("what quality would you like? (default highest)")
    print("0) highest \n1) lowest \n2) 2160p (4k) \n3) 1440p (2k) \n4) 1080p (full hd) \n5) 720p \n6) 480p \n7) 360p \n8) 240p")
    c = input("quality: ")
    try:
        c = int(c)
        if (c == 8):
            quality = vidQualities[0]
        elif (c == 7):
            quality = vidQualities[1]
        elif (c == 6):
            quality = vidQualities[2]
        elif (c == 5):
            quality = vidQualities[3]
        elif (c == 4):
            quality = vidQualities[4]
        elif (c == 3):
            quality = vidQualities[5]
        elif (c == 2):
            quality = vidQualities[6]
        elif (c == 1):
            quality = "lowest"
        else:
            quality = "highest"
    except:
        quality = "highest"
    print(quality + " quality chosen")

print('\n')
isPlayList = input("Is the download a playlist?(default: no) (Y/N): ").lower().strip()

if (isPlayList == "y"):
    print("\nplaylist chosen")
    isPlayList = True
else:
    print("\nvideo chosen\n")
    isPlayList = False

downloadUrl = input("download url: ")
outFolder = input("output destination: ")
print('\n')

fileNames = []

if (format == 1):
    if (isPlayList):
        pl = Playlist(downloadUrl)
        for e in range(2):
            url = pl[e]
            yt = YouTube(url)
            fileNames.append((yt.streams[0].title + ".mp4"))
            yt.streams.filter(only_audio=True).first().download(outFolder)
            print("downloaded " + yt.streams[0].title)
    else:
        yt = YouTube(downloadUrl)
        fileNames.append((yt.streams[0].title + ".mp4"))
        yt.streams.filter(only_audio=True).first().download(outFolder)
        print("downloaded " + yt.streams[0].title)

else:
    if (isPlayList):
        pl = Playlist(downloadUrl)
        for url in range(pl):
            yt = YouTube(url)
            if (quality == "highest"):
                yt.streams.get_highest_resolution().download(outFolder)
            elif (quality == 'lowest'):
                yt.streams.get_lowest_resolution().download(outFolder)
            else:
                q = yt.streams.get_highest_resolution().resolution
                for i, v in enumerate(vidQualities):
                    if (q == v):
                        q = i
                        break
                
                p = 0
                for i, v in enumerate(vidQualities):
                    if (quality == v):
                        p = i
                        break
                if (p > q):
                    quality = vidQualities[q]

                yt.streams.filter(res=quality).first().download(outFolder)
                print("downloaded " + yt.streams[0].title)

    else:
        yt = YouTube(downloadUrl)
        if (quality == "highest"):
            yt.streams.get_highest_resolution().download(outFolder)
        elif (quality == 'lowest'):
            yt.streams.get_lowest_resolution().download(outFolder)
        else:
            q = yt.streams.get_highest_resolution().resolution
            for i, v in enumerate(vidQualities):
                if (q == v):
                    q = i
                    break
            
            p = 0
            for i, v in enumerate(vidQualities):
                if (quality == v):
                    p = i
                    break
            if (p > q):
                quality = vidQualities[q]

            yt.streams.filter(res=quality).first().download(outFolder)
            print("downloaded " + yt.streams[0].title)

if (format == 1):
    for file in os.listdir(outFolder):
        if re.search('mp4', file):
            if (file in fileNames):
                mp4_path = os.path.join(outFolder,file)
                mp3_path = os.path.join(outFolder,os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)