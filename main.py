import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint

dotenv_path = Path('auth.env')
load_dotenv(dotenv_path=dotenv_path)

date = input("what year you would like to travel to in YYYY-MM-DD format. ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('CLIENTID'),
                                               client_secret=os.getenv('CLIENTSECRET'),
                                               redirect_uri=os.getenv('REDIRECT_URL'),
                                               show_dialog=True,
                                               cache_path=".cache",
                                               scope="playlist-modify-private"))

user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


# TO TRACK YOUR CURRENT LIKED SONGS.

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items'], 1):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

# SEARCH FOR THE SONGS.

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv('CLIENTID'),
#                                                            client_secret=os.getenv('CLIENTSECRET')))
#
# results = sp.search(q='tum hi ho', limit=50)
# for idx, track in enumerate(results['tracks']['items'], 1):
#     print(idx, track['name'])
