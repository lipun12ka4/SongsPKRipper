# This is an attempt to download the songs.pk compiled Zip archives
import requests
from bs4 import BeautifulSoup

def get_single_album_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    # Download Zip Files
    for item_name in soup.find_all('a', {'class': 'btn btn-block btn-default'}):
        zip_link = item_name.get('href')
        if '320Kbps' in zip_link:
            print(zip_link)


def album_spider(letter, max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.songspk.io/browse/compilations/' + str(letter) + '?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.find_all('a', {'class': 'image-hover'}):
            href = 'http://www.songspk.io' + link.get('href')
            # print(href)
            get_single_album_data(href)
        page += 1

import sys

import string
a2z_list = list(string.ascii_lowercase) + ['0-9']
# a2z_list = ['0-9']

import time

for letter in a2z_list:
    sys.stdout = open("D:/SongsPK_Compilations/" + str(letter) + "_list" + "_320Kbps.txt", "w")
    album_spider(letter, 10)
    sys.stdout.close()
    time.sleep(1)



