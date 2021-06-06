from bs4.element import AttributeValueWithCharsetSubstitution
import requests
from bs4 import BeautifulSoup

# get user response
hot_100_week = input('Enter a week to see the Hot 100 list (YYYY-MM-DD): ')

base_url = 'https://www.billboard.com/charts/hot-100/'
url = base_url + hot_100_week

response = requests.get(url)
hot_100_page = response.text
soup = BeautifulSoup(hot_100_page, 'html.parser')

songs = soup.find_all(name='span', class_="chart-element__information__song text--truncate color--primary")

songs_list =[]

for song in songs:
    songs_list.append(song.getText())

artists = soup.find_all(name='span', class_="chart-element__information__artist text--truncate color--secondary")
artists_list = []
for artist in artists:
    artists_list.append(artist.getText())

track_list = []
for artist, song in zip(artists_list, songs_list):
    track_list.append(song + ' by ' + artist)

print(track_list[:5])

