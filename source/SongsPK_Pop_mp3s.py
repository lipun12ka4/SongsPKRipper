import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import quote

def get_single_album_mp3s(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    '''
    # Download Zip Files
    for item_name in soup.find_all('a', {'class': 'btn btn-block btn-default'}):
        zip_link = item_name.get('href')
        if '320Kbps' in zip_link:
            print(zip_link)
    '''
    # Create a folder with the name of the Album
    # Get name from item_url
    folder_name = item_url.replace("http://www.songspk.io/", "").replace(".html", "")
    if not os.path.exists('D:/SongsPK_Pop/' + folder_name):
        os.makedirs('D:/SongsPK_Pop/' + folder_name)
    # Search for all mp3 files on that page
    for item_name in soup.find_all('a', {'class': 'btn col-md-5 btn-default btn-block'}):
        mp3_link = item_name.get('href')
        print(mp3_link)
        # Download the Mp3 into the respective folder
        if '.mp3' in mp3_link:
            os.system(r'C:\"Program Files (x86)"\"Internet Download Manager"\idman.exe /n /a /d ' + "http://"
                      + quote(mp3_link.replace("http://", "")) + " /p " + "D:\SongsPK_Pop" + "\\" + folder_name)
        else:
            os.system(r'C:\"Program Files (x86)"\"Internet Download Manager"\idman.exe /n /a /d ' +
                      mp3_link + r" /p " + "D:\SongsPK_Pop" + "\\" + folder_name)


def album_spider(letter, max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.songspk.io/browse/pop-remix-albums/' + str(letter) + '?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.find_all('a', {'class': 'image-hover'}):
            href = 'http://www.songspk.io' + link.get('href')
            print(href)
            get_single_album_mp3s(href)
        page += 1

import sys

import string
a2z_list = list(string.ascii_lowercase)

# a2z_list = ['c', 'd', 'e', 'f', 'g', 'h', 'i']
# a2z_list = ['a']
# a2z_list =['0-9']

import time

for letter in a2z_list:
    sys.stdout = open("D:/SongsPK_Pop/" + str(letter) + "_list" + "_mp3.txt", "w")
    album_spider(letter, 15)
    sys.stdout.close()
    time.sleep(1)



