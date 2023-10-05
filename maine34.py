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

spotify_playlist_id = []
spotify_playlist_isrc = []
spotify_playlist_artist = []
spotify_playlist_track_name = []

youtube_playlist_id = []
youtube_playlist_isrc = []
youtube_playlist_artist = []
youtube_playlist_track_name = []
diffs = []

separator = '(feat'



def get_current_spotify():    #get current spotify

    spoplaylist = sp.playlist_items(plSPO_id)
    spoitemplaylist = spoplaylist["items"]

    for items in spoitemplaylist:
        spotify_playlist_isrc.append(items['track']['external_ids']['isrc'])
        spotify_playlist_track_name.append(items['track']['name'])
        spotify_playlist_artist.append(items['track']['artists'][0]['name'])
        spotify_playlist_id.append(get_id(items['track']['name'],items['track']['artists'][0]['name']))

    return(spotify_playlist_track_name,spotify_playlist_artist,spotify_playlist_isrc,spotify_playlist_id)


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




def get_current_ytb():
    ytresp = ytmusic.get_playlist(playlistId=plYTB_id)
    ytitem = ytresp['tracks']
    k = 0
    for items in ytitem:
        youtube_playlist_track_name.append(items['title'])
        youtube_playlist_artist.append(items['artists'][0]['name'])
        youtube_playlist_isrc.append(get_isrc_(items['title'],items['artists'][0]['name']))
        youtube_playlist_id.append(get_id(items['title'],items['artists'][0]['name']))
        k = k+1
    return(youtube_playlist_track_name,youtube_playlist_artist,youtube_playlist_isrc,youtube_playlist_id)








def get_isrc_(track_name,artist):
    artist = artist.replace(' ', '+')
    name = track_name.replace(' ', '+')
    spoisrcquery = name + "%20artist:" +  artist
    search_results = sp.search(q=spoisrcquery,limit=1,type="track")
    if search_results["tracks"]["items"] == []:
        print('Nothing found for ' + track_name + artist)
    else:
        return(search_results['tracks']['items'][0]['external_ids']['isrc'])

def get_id(track_name,artist):
    query = track_name + "%20artist:" +  artist + '&type=track&limit=1'
    search_results = sp.search(q=query)
    id = search_results['tracks']['items'][0]['id']
    return(id)


def compare_isrc(youtube_isrc,spotify_isrc):
    if spotify_isrc == youtube_isrc :
        return(0)
    else:
        return(youtube_isrc,spotify_isrc)


def compare (ytb_input,spo_input):
    k=0
    diffs = []
    add_ytb = []
    add_spo = []
    for items in ytb_input:
        diffs.append(compare_isrc(ytb_input[k],spo_input[k]))
        k=k+1
    for items in diffs:
        if check_ytb(items,ytb_input) == False:
            add_ytb.append(items)
        else:
            print("boah")
        if check_spo(items,spo_input) == False:
            add_spo.append(items)
        else:
            print("boba")
    return(add_ytb,add_spo)



def check_ytb(isrc,ytb):
    if isrc in ytb:
        return(True)
    else:
        return(False)

def check_spo(isrc,spo):
    if isrc in spo:
        return(True)
    else:
        return(False)


def add_spo(id):
    le_id = [id]
    sp.playlist_add_items(plSPO_id,le_id)



#print(get_isrc_("Doja","Central Cee"))
#print(convert_isrc_id())


#print(get_current_ytb())
#print(get_current_spotify())

#print(compare(get_current_spotify(),get_current_ytb()))
#print(get_current_spotify())
#print(get_current_ytb())


def display_playlists():

    k = 0
    for items in spotify_playlist_id:
        print(spotify_playlist_id[k])
        print(spotify_playlist_track_name[k])
        print(spotify_playlist_artist[k])
        print(spotify_playlist_isrc[k])
        k= k + 1
    k = 0
    for items in youtube_playlist_id:
        print(youtube_playlist_id[k])
        print(youtube_playlist_track_name[k])
        print(youtube_playlist_artist[k])
        print(youtube_playlist_isrc[k])
        k= k + 1
    k = 0
    for items in youtube_playlist_id:
        print(items[k])
        k = k + 1




def save_spo():
    with open("spo_isrc.txt", "w") as file:
        file.truncate()
        for items in spotify_playlist_isrc:
            file.write(items)
    with open("spo_track_name.txt", "w") as file:
        file.truncate()
        for items in spotify_playlist_track_name:
            file.write(items)
    with open("spo_id.txt", "w") as file:
        file.truncate()
        for items in spotify_playlist_id:
            file.write(items)
    with open("spo_artist.txt", "w") as file:
        file.truncate()
        for items in spotify_playlist_artist:
            file.write(items)

def save_ytb():

    with open("ytb_isrc.txt", "w") as file:
        file.truncate()
        for items in youtube_playlist_isrc:
            file.write(items)
    with open("ytb_track_name.txt", "w") as file:
        file.truncate()
        for items in youtube_playlist_track_name:
            file.write(items)
    with open("ytb_id.txt", "w") as file:
        file.truncate()
        for items in youtube_playlist_id:
            file.write(items)
    with open("ytb_artist.txt", "w") as file:
        file.truncate()
        for items in youtube_playlist_artist:
            file.write(items)




spotify_playlist_isrc_loaded =[]
spotify_playlist_track_name_loaded =[]
spotify_playlist_artist_loaded =[]
spotify_playlist_id_loaded =[]

youtube_playlist_isrc_loaded =[]
youtube_playlist_track_name_loaded =[]
youtube_playlist_artist_loaded =[]
youtube_playlist_id_loaded =[]


def load_spo():
    with open("spo_isrc.txt", "r") as file:
        for line in file:
            spotify_playlist_isrc_loaded.append(line)
    with open("spo_track_name.txt", "r") as file:
        for line in file:
            spotify_playlist_track_name_loaded.append(line)
    with open("spo_id.txt", "r") as file:
        for line in file:
            spotify_playlist_id_loaded.append(line)
    with open("spo_artist.txt", "r") as file:
        for line in file:
            spotify_playlist_artist_loaded.append(line)
    return(spotify_playlist_track_name_loaded,spotify_playlist_artist_loaded,spotify_playlist_isrc_loaded,spotify_playlist_id_loaded)

def load_ytb():
    with open("ytb_isrc.txt", "r") as file:
        for line in file:
            youtube_playlist_isrc_loaded.append(line)
    with open("ytb_track_name.txt", "r") as file:
        for line in file:
            youtube_playlist_track_name_loaded.append(line)
    with open("ytb_id.txt", "r") as file:
        for line in file:
            youtube_playlist_id_loaded.append(line)
    with open("ytb_artist.txt", "r") as file:
        for line in file:
            youtube_playlist_artist_loaded.append(line)
    return(youtube_playlist_track_name_loaded,youtube_playlist_artist_loaded,youtube_playlist_isrc_loaded,youtube_playlist_id_loaded)


