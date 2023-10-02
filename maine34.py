import os
import spotipy
import logging
import json
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyOAuth


os.environ["SPOTIPY_CLIENT_ID"] = "704398ed06514d55b8bfd53f88866807"
os.environ["SPOTIPY_CLIENT_SECRET"] = "bf34e920038540d19e8d88dbed012edd"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"

logger = logging.getLogger('examples.add_tracks_to_playlist')
logging.basicConfig()
scope = 'playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope ))

ytmusic = YTMusic("oauth.json")

plSPO_id = 'spotify:playlist:6KLmpAvHfkxpQIhixFpCfp'
plYTB_id = 'PLuv156FW1MW6zRlfXJIvND9QUDqiumr4d'

#variables:

#lenght of current playlist (to store it)
l = 0

#ram variable
k=0


spotify_playlist_isrc = []
spotify_playlist_artist = []
spotify_playlist_track_name = []
youtube_playlist_isrc: []
youtube_playlist_artist: []
youtube_playlist_track_name: []


separator = '(feat'



def get_current_spotify():    #get current spotify

    spoplaylist = sp.playlist_items(plSPO_id)
    spoitemplaylist = spoplaylist["items"]


    for items in spoitemplaylist:
        l = l+1

    print(l)




    for items in spoitemplaylist:
        spotify_playlist_isrc.append(items['track']['external_ids']['isrc'])
        spotify_playlist_track_name.append(items['track']['name'])
        spotify_playlist_artist.append(items['track']['artists'][0]['name'])



    def comptespodbug():
        #DEBUG recomptage de toutes les listes
        k=0
        for items in spotify_playlist_isrc:
            k = k+1
        if k != l:
            print('ola ya un soucis isrcs')
        k = 0

        for items in spotify_playlist_track_name:
            k = k+1
        if k != l:
            print('ola ya un soucistrckn ame')
        k = 0
        for items in spotify_playlist_artist:
            k = k+1
        if k != l:
            print('ola ya un soucis sp artist')
        k = 0

    #comptespodbug()
def get_current_ytb():
    ytresp = ytmusic.get_playlist(playlistId=plYTB_id)
    ytitem = ytresp['tracks']
    k = 0
    youtube_playlist_track_name = []
    youtube_playlist_artist = []
    for items in ytitem:
        youtube_playlist_track_name.append(items['title'])
        youtube_playlist_artist.append(items['artists'][0]['name'])
        k = k+1






    for items in youtube_playlist_track_name:
        k=k-1
        artist = youtube_playlist_artist[k]
        artist = artist.replace(' ', '+')
        name = items.replace(' ', '+')
        spoisrcquery = name + '+' + artist + '&type=track&limit=1'
        search_results = sp.search(q=spoisrcquery)
        if search_results["tracks"]["items"] == []:
            print('Nothing found for ' + items)
        else:
            youtube_playlist_isrc = search_results['tracks']['items'][0]['external_ids']

print(spotify_playlist_isrc)
print(spotify_playlist_artist)
print(spotify_playlist_track_name)


get_current_ytb()

#Kinky+People&type=track&limit=1