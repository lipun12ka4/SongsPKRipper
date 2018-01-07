import os
from urllib.parse import quote

# os.system("dir")
# os.system(r'C:\"Program Files (x86)"\"Internet Download Manager"\idman.exe /n /a /d ' +
#          "http://320net.songspk.onl/indian/Aa-Gaya-Hero-2017-320Kbps[Songspk.NAME].zip" + " /p " +
#          "D:\SongsPK")


mp3_link = 'http://sound30.mp3slash.net/indian/aagayahero/01 - Lohe Da Liver - Aa Gaya Hero [Songspk.NAME].mp3'
print(mp3_link)
print(quote(mp3_link))
# link = mp3_link.replace("http://", "")
# print(link)
os.system(r'C:\"Program Files (x86)"\"Internet Download Manager"\idman.exe /n /a /d ' + "http://" + quote(mp3_link.replace("http://", "")) +
          " /p " + "D:\SongsPK")
