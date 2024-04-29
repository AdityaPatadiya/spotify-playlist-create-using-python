# Billboard Hot 100 Playlist Creator On Spotify
This Python script fetches Billboard Hot 100 songs from [Billboard Hot 100](https://www.billboard.com/charts/hot-100/), for a given date and creates a Spotify playlist with those songs.

## Prerequisites
Before running the script, make sure you have the following installed:

*Python 3
*Python libraries: spotipy, requests, beautifulsoup4, dotenv

Additionally, you need to have a [Spotify Developer](https://developer.spotify.com/) account and create an application to obtain client ID and client secret. Also, create a .env file with these credentials and a redirect URL.
```
CLIENTID=your_client_id
CLIENTSECRET=your_client_secret
REDIRECT_URL=your_redirect_url
```
## Usage
Run the script main.py.
Enter the date you would like to create a playlist for in YYYY-MM-DD format when prompted.
The script will fetch Billboard Hot 100 songs for the given date, search for them on Spotify, and create a new private playlist with the retrieved songs.

## Additional Notes
### To Track Your Liked Songs
To track your currently liked songs, you need to change the scope to 'user-library-read'. Uncomment the following section in the code:
```
# TO TRACK YOUR CURRENT LIKED SONGS.  # NOTE: YOU HAVE TO CHANGE THE 'SCOPE' TO 'user-library-read'

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items'], 1):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
```
### Searching for Songs
If you want to search for specific songs, uncomment the following section in the code:
```
# SEARCH FOR THE SONGS.

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv('CLIENTID'),
                                                           client_secret=os.getenv('CLIENTSECRET')))

results = sp.search(q='tum hi ho', limit=50)
for idx, track in enumerate(results['tracks']['items'], 1):
    print(idx, track['name'])
```
This will search for the song 'tum hi ho', but you can replace it with any other song you want to search for.

### Here's the video that demonstrate the program:
https://github.com/AdityaPatadiya/spotify-playlist-create-using-python/assets/161931434/0c176071-bbe8-47d5-8255-8b3a1d0bba22




