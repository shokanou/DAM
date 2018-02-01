import os
import sys
import urllib2,urllib
import re
from bs4 import BeautifulSoup

keyword = raw_input("Please enter song name:")
url = 'http://music.baidu.com/search?key='+keyword
url1 = 'http://music.baidu.com/data/music/file?link=&song_id='
base_path = '/Users/Ousyoukan/Desktop/microblog/app/static/data/web/'
filepath = '/Users/Ousyoukan/Desktop/microblog/app/static/data/web/'+keyword+'.mp3'
album_url_t = 'http://music.baidu.com/album/'
album_filepath = base_path+keyword+'.jpg'
def Schedule(a,b,c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

def get_id(url):
	page = urllib2.urlopen(url)
	first="href="
	last="target="
	mid = 'song'
	mid1 = 'album'
	contents = page.read()
	soup = BeautifulSoup(contents)
	soup1 = soup.find("li",id="first_song_li")
	soup2 = soup1.a
	album = soup1.span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
	album_t = album.a
	soup3 = str(soup2)
	album1 = str(album_t)
	soup4 = soup3[soup3.index(first)+6:]
	soup5 = soup4[:soup4.index(last)-2]
	song_id = soup5[soup5.index(mid)+5:]
	album2 = album1[album1.index(first)+6:]
	album3 = album2[:album2.index(last)-2]
	album_id = album3[album3.index(mid1)+6:]
	url2 = url1+song_id
	#urllib.urlretrieve(url2,filepath,Schedule)
	return album_id

def get_album(album_id): 
	first = 'src'
	last = 'title' 
	album_url=album_url_t+album_id
	page = urllib2.urlopen(album_url)
	content = page.read()
	soup = BeautifulSoup(content)
	soup1 = soup.find("span",class_="cover")
	soup2 = soup1.img
	album_t = str(soup2)
	album_t1 = album_t[album_t.index(first)+5:]
	album = album_t1[:album_t1.index(last)-2]
	urllib.urlretrieve(album,album_filepath,Schedule)
	print album

a = get_id(url)
get_album(a)

