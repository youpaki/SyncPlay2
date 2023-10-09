import os
import spotipy
import logging
import json
import time
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
spotify_playlist_ytid = []

youtube_playlist_id = []
youtube_playlist_isrc = []
youtube_playlist_artist = []
youtube_playlist_track_name = []
youtube_playlist_ytid = []

diffs = []

spotify_playlist_isrc_loaded =[]
spotify_playlist_track_name_loaded =[]
spotify_playlist_artist_loaded =[]
spotify_playlist_id_loaded =[]

youtube_playlist_isrc_loaded =[]
youtube_playlist_track_name_loaded =[]
youtube_playlist_artist_loaded =[]
youtube_playlist_id_loaded =[]


final_playlist_track_name = []
final_playlist_artist = []
final_playlist_isrc = []
final_playlist_id = []
raw_ytb_pl = []
separator = '(feat'



def get_current_spotify():    #get current spotify
    get_current_spotify.spoplaylist = sp.playlist_items(plSPO_id)
    spoitemplaylist = get_current_spotify.spoplaylist["items"]
    get_current_spotify.spotify_playlist_id = []
    spotify_playlist_isrc = []
    spotify_playlist_artist = []
    spotify_playlist_track_name = []
    spotify_playlist_ytid = []

    if spoitemplaylist == []:
        pass
    else:
        for items in spoitemplaylist:
            spotify_playlist_isrc.append(items['track']['external_ids']['isrc'])
            spotify_playlist_track_name.append(items['track']['name'])
            spotify_playlist_artist.append(items['track']['artists'][0]['name'])
            get_current_spotify.spotify_playlist_id.append(items['track']['id'])
            spotify_playlist_ytid.append(get_yt_id(items['track']['name'],items['track']['artists'][0]['name']))
        a = [[spotify_playlist_track_name[i], spotify_playlist_artist[i], spotify_playlist_isrc[i],get_current_spotify.spotify_playlist_id[i], spotify_playlist_ytid[i]] for i in range(len(spotify_playlist_track_name))]
        return a




def get_current_ytb():
    get_current_ytb.ytresp = ytmusic.get_playlist(playlistId=plYTB_id)
    ytitem = get_current_ytb.ytresp['tracks']
    k = 0
    youtube_playlist_id = []
    youtube_playlist_isrc = []
    youtube_playlist_artist = []
    youtube_playlist_track_name = []
    youtube_playlist_ytid = []
    if ytitem == []:
        pass
    else:
        for items in ytitem:
            youtube_playlist_track_name.append(items['title'])
            youtube_playlist_artist.append(items['artists'][0]['name'])
            youtube_playlist_isrc.append(get_isrc_(items['title'],items['artists'][0]['name']))
            youtube_playlist_id.append(get_id(items['title'],items['artists'][0]['name']))
            youtube_playlist_ytid.append(items["videoId"])
            k = k+1

    return [[youtube_playlist_track_name[i], youtube_playlist_artist[i], youtube_playlist_isrc[i], youtube_playlist_id[i], youtube_playlist_ytid[i]]
         for i in range(len(youtube_playlist_track_name))]




def get_yt_id(track_name,artist):
    query = artist + " " + track_name
    search_results = ytmusic.search(query=query, filter= "songs",limit=1,ignore_spelling=True)
    a = search_results[0]['videoId']

    return a



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









def merde():

    current_spo = []


    spotify_playlist_track_name = current_spo[0]
    spotify_playlist_artist = current_spo[1]
    spotify_playlist_isrc = current_spo[2]
    spotify_playlist_id = current_spo[3]



def define_track(track_name,artist,isrc,id,pos,):
    track = []
    poc = str(pos)
    track.append(poc)
    track.append(track_name)
    track.append(artist)
    track.append(isrc)
    track.append(id)
    return(track)

def list_tracks(track_name,artist,isrc,id,ytid):
    k = 0
    for items in track_name:
        laliste = define_track(track_name[k],artist[k],isrc[k],id[k],ytid[k],k)
        k=k+1
    return(laliste)

#print(list_tracks(spotify_playlist_track_name,spotify_playlist_artist,spotify_playlist_isrc,spotify_playlist_id))
#ordre final = track_name artist isrc id





#def dump_final():






def savejson(pl):
    file = open("saved.json","w")
    json.dump(pl,file)
    file.close()



def get_saved():
    json_file = open("saved.json","r")
    saved = json.load(json_file)
    return saved


def compare(saved,youtube,spotify):
    if saved == youtube and saved == spotify:
        pass
    if saved != spotify:
        saved = spotify
        youtube = spotify
    if saved != youtube:
        saved = youtube
        spotify = youtube

    return saved,youtube,spotify



def erase(yt_id,spo_id):

    haha = []
    yt_id_list = []
    with open("saved.json", "w") as fp:
        json.dump(haha,fp)
        fp.close()


    if youtube_playlist != []:
        for items in youtube_playlist:
            yt_id_list.append(items[4])
        ytmusic.remove_playlist_items(yt_id,get_current_ytb.ytresp["tracks"])
    else:
        pass
    k=0
    if spotify_playlist != []:
        sp.playlist_remove_all_occurrences_of_items(playlist_id=plSPO_id, items=get_current_spotify.spotify_playlist_id)
    else:
        pass




def update(save_pl,yt_pl,sp_pl):
    erase(plYTB_id,plSPO_id)
    savejson(save_pl)
    dump_spo(sp_pl)
    dump_yt(yt_pl)
    print("updated")




def dump_spo(pl):
    ids = []
    for items in pl:
        ids.append(items[3])
    sp.playlist_add_items(plSPO_id, ids)




def dump_yt(pl):
    ids = []
    for items in pl:
        ids.append(items[4])
    ytmusic.add_playlist_items(plYTB_id,ids)




spotify_playlist = get_current_spotify()
youtube_playlist = get_current_ytb()
saved_playlist = get_saved()

compared  = compare(saved_playlist,youtube_playlist,spotify_playlist)
update(compared[0],compared[1],compared[2])




