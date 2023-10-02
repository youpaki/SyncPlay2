import os
import spotipy
import logging
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyOAuth

os.environ["SPOTIPY_CLIENT_ID"] = "704398ed06514d55b8bfd53f88866807"
os.environ["SPOTIPY_CLIENT_SECRET"] = "bf34e920038540d19e8d88dbed012edd"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"

logger = logging.getLogger('examples.add_tracks_to_playlist')
logging.basicConfig()
scope = 'playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope ))

ytmusic = YTMusic('headers_auth.json')

plSPO_id = 'spotify:playlist:0r29EyaaHRJ6ymPnk7m4bx'
plYTB_id = 'PLTgz9Y3b0ItJ2G0xAUPkrf6oOuA9h08ih'