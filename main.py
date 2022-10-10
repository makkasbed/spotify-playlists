from pprint import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = "https://www.billboard.com/charts/hot-100/" + year

top_songs = requests.get(URL).text

soup = BeautifulSoup(top_songs, 'html.parser')

songs = soup.find_all(name="h3", class_="a-no-trucate")

top_hundred = [song.string.strip() for song in songs]
print(len(top_hundred))

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),
                                               client_secret=os.getenv("CLIENT_SECRET"),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))
user_id = sp.current_user()["id"]
# print(user_id)

song_year = year.split("-")[0]

song_data = []
for_spotify = []
for song in top_hundred:
    result = sp.search(q=f"track:{song} year:{song_year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_data.append({'name': song, 'spotify_url': uri})
        for_spotify.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

if len(song_data) > 0:
    playlist = sp.user_playlist_create(user_id, year + " Billboard 100", public=False)
    print(f"Playlist {playlist} created")
    if playlist:
        id = playlist['id']
        print(f"Playlist {id} created")
        sp.playlist_add_items(id, for_spotify)
