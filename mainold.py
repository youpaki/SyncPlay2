import os
import spotipy
import logging
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

ytmusic = YTMusic('headers_auth.json')

plSPO_id = 'spotify:playlist:0r29EyaaHRJ6ymPnk7m4bx'
plYTB_id = 'PLTgz9Y3b0ItJ2G0xAUPkrf6oOuA9h08ih'
a=0
n=0
separator = '(feat'
old_youtube_playlist_track_name = []
old_spotify_playlist_isrc = []
spotify_playlist_isrc = []
spotify_playlist_artist = []
spotify_playlist_track_name = []
spotify_playlist_track_id = []
youtube_playlist_artist = []
youtube_playlist_track_name = []
print('caca ?')
# get spotify playlist
spoplaylist = sp.playlist_items(plSPO_id)
spoitemplaylist = spoplaylist["items"]

for items in spoitemplaylist:
    spotify_playlist_isrc.append(items['track']['external_ids']['isrc'])
    spotify_playlist_track_name.append(items['track']['name'])
    spotify_playlist_artist.append(items['track']['artists'][0]['name'])
    spotify_playlist_track_id.append(items['track']['id'])


# get youtube playlist


ytresp = ytmusic.get_playlist(playlistId=plYTB_id)
ytitem = ytresp['tracks']
for items in ytitem:
    youtube_playlist_track_name.append(items['title'])
    youtube_playlist_artist.append(items['artists'][0]['name'])


for items in spotify_playlist_isrc:
    k = 0
    b = 0
    actual_spotify_track_name = spotify_playlist_track_name[n]
    actual_spotify_track_name_without_feat = actual_spotify_track_name.rsplit(separator, 1)[0]
    for itemss in youtube_playlist_track_name:
        if actual_spotify_track_name_without_feat in itemss:
            # print(itemss + '  est  ' + actual_spotify_track_name_without_feat)
            a = a + 1
            b = b + 1
            k = k + 1
        else:
            # print(itemss + ' n_ est pas ' + actual_spotify_track_name_without_feat)
            a = a + 1
            k = k + 1
    if b > 0:
        # print('faut pas l_ajouter elle y est deja ')
        a = a + 1
    else:
        # print('go l_ajouter')
        video_ids = []
        search_results = ytmusic.search(query=items, filter='songs')

        if search_results == []:

            search_results = ytmusic.search(query=spotify_playlist_track_name[n] + spotify_playlist_artist[n],
                                            filter='songs')
            video_result = search_results[0]
            video_ids.append(video_result['videoId'])
            ytmusic.add_playlist_items(plYTB_id, videoIds=video_ids)
            print(actual_spotify_track_name_without_feat + '    To Youtube')
            if search_results == []:
                print('Nothing found on youtube for ' + items)
        else:
            video_result = search_results[0]
            video_ids.append(video_result['videoId'])
            ytmusic.add_playlist_items(plYTB_id, videoIds=video_ids)
            print(actual_spotify_track_name_without_feat + '    To Youtube')
    if b >= 2:
        # print(actual_spotify_track_name_without_feat + ' Est en plusieurs exemplaires !!')
        a = a + +1
    n = n + 1
    n = 0
for items in youtube_playlist_track_name:
    artist = youtube_playlist_artist[n]
    caca = items
    name = caca.rsplit(separator, 1)[0]
    spoquery = name + ' ' + artist
    search_results = sp.search(q=spoquery)
    if search_results["tracks"]["items"] == []:
        print('Nothing found for ' + items)
    else:

        spoidsearchresult = search_results["tracks"]["items"][0]["id"]
        if spoidsearchresult in spotify_playlist_track_id:
            a = a + 1
            # print('Already in spoityf playlist')
        else:
            spoidadd_to_playlist = [spoidsearchresult]
            sp.playlist_add_items(plSPO_id, spoidadd_to_playlist)
            print(spoquery + '    To Spotify')
    n = n + 1











while True:
    n= 0


    #get spotify playlist
    spoplaylist = sp.playlist_items(plSPO_id)
    spoitemplaylist = spoplaylist["items"]



    for items in spoitemplaylist:
        spotify_playlist_isrc.append(items['track']['external_ids']['isrc'])
        spotify_playlist_track_name.append(items['track']['name'])
        spotify_playlist_artist.append(items['track']['artists'][0]['name'])
        spotify_playlist_track_id.append(items['track']['id'])


    #get youtube playlist




    ytresp = ytmusic.get_playlist(playlistId=plYTB_id)
    ytitem = ytresp['tracks']
    for items in ytitem:
        youtube_playlist_track_name.append(items['title'])
        youtube_playlist_artist.append(items['artists'][0]['name'])


    b = 0
    if not old_spotify_playlist_isrc:
        print('Old Spotify Playlist is Empty')
        a = a + 1
        n= 0
    if spotify_playlist_isrc in old_spotify_playlist_isrc :
        print('Spotify Playlist hasnt changed')
        a = a + 1
    else:

        for items in spotify_playlist_isrc:
            k = 0
            b=0
            actual_spotify_track_name = spotify_playlist_track_name[n]
            actual_spotify_track_name_without_feat = actual_spotify_track_name.rsplit(separator, 1)[0]
            for itemss in youtube_playlist_track_name:
                if actual_spotify_track_name_without_feat in itemss:
                    #print(itemss + '  est  ' + actual_spotify_track_name_without_feat)
                    a = a + 1
                    b = b+1
                    k=k+1
                else:
                    #print(itemss + ' n_ est pas ' + actual_spotify_track_name_without_feat)
                    a = a + 1
                    k=k+1
            if b > 0:
                #print('faut pas l_ajouter elle y est deja ')
                a = a +1
            else :
                #print('go l_ajouter')
                video_ids = []
                search_results = ytmusic.search(query=items,filter='songs')

                if search_results == []:

                    search_results = ytmusic.search(query=spotify_playlist_track_name[n] + spotify_playlist_artist[n],filter='songs')
                    video_result = search_results[0]
                    video_ids.append(video_result['videoId'])
                    ytmusic.add_playlist_items(plYTB_id,videoIds=video_ids)
                    print(actual_spotify_track_name_without_feat + '    To Youtube')
                    if search_results == []:
                        print('Nothing found on youtube for ' + items)
                else:
                    video_result = search_results[0]
                    video_ids.append(video_result['videoId'])
                    ytmusic.add_playlist_items(plYTB_id,videoIds=video_ids)
                    print(actual_spotify_track_name_without_feat + '    To Youtube')
            if b >= 2:
                #print(actual_spotify_track_name_without_feat + ' Est en plusieurs exemplaires !!')
                a = a + 1
            n = n + 1


    n=0


    if not old_youtube_playlist_track_name :
        print('Old Youtube Playlist is Empty')
        a = a + 1
        n= 0
    if youtube_playlist_track_name in old_youtube_playlist_track_name:
        print('Youtube Playlist Hasnt changed')
        a = a + 1
    else:
        for items in youtube_playlist_track_name:
            artist = youtube_playlist_artist[n]
            caca = items
            name = caca.rsplit(separator, 1)[0]
            spoquery = name +' '+ artist
            search_results = sp.search(q=spoquery)
            if search_results["tracks"]["items"] == []:
                print('Nothing found for ' + items )
            else :

                spoidsearchresult = search_results["tracks"]["items"][0]["id"]
                if spoidsearchresult in spotify_playlist_track_id :
                    a= a+1
                    #print('Already in spoityf playlist')
                else:
                    spoidadd_to_playlist = [spoidsearchresult]
                    sp.playlist_add_items(plSPO_id,spoidadd_to_playlist)
                    print(spoquery + '    To Spotify')
            n = n + 1

    old_youtube_playlist_track_name = []
    old_youtube_playlist_track_name = youtube_playlist_track_name
    old_spotify_playlist_isrc = []
    old_spotify_playlist_isrc = spotify_playlist_isrc

    print('done')
    print(a)
    time.sleep(30)