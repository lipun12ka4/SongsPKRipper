import os
import shutil
from mutagen.mp3 import MP3

# audio = MP3("A Kabaria (Title Song).mp3")
# # print ("Track: " + audio.get("TIT2").text[0])
# # print ("Encoded By: " + audio.get("TENC").text[0])
# print(audio.get("TALB").text[0])

for i in os.listdir(os.getcwd()):
    if i.endswith(".mp3"):
        print(i)
        audio = MP3(i)
        print(audio.get("TALB").text[0])
        directory = audio.get("TALB").text[0]
        if not os.path.exists(directory):
            os.makedirs(directory)
        target = directory+"/"+i
        shutil.move(i, target)
        continue
    else:
        continue