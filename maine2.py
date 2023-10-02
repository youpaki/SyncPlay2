import os

import spotipy
import logging
import time


from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyOAuth


print('launched')
os.environ["SPOTIPY_CLIENT_ID"] = "704398ed06514d55b8bfd53f88866807"
os.environ["SPOTIPY_CLIENT_SECRET"] = "bf34e920038540d19e8d88dbed012edd"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"

username = 'youpakikillllller' #placeholder value here
client_id = '704398ed06514d55b8bfd53f88866807' #placeholder value here
client_secret = 'bf34e920038540d19e8d88dbed012edd' #placeholder value here
redirect_uri = 'http://localhost:8888/callback/'

a= 0
while True:


    print('TRU')


    logger = logging.getLogger('examples.add_tracks_to_playlist')
    print(logger)
    logging.basicConfig()
    scope = 'playlist-modify-public'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    ytmusic = YTMusic('headers_auth.json')

    plSPO_id = 'spotify:playlist:0rihc5iMKzzaUUGHD4NtYY'
    plYTB_id = 'PLTLMSWccnLTC3UzHHJbbeVpZLM8Xue_dU'
    nombre_YTB = 0
    nombre_SPO = 0


    # get spotify full playlist
    spoplaylist = sp.playlist_items(plSPO_id, fields='total,items.track.name,items.track.artists.name')
    spoitemplaylist = spoplaylist["items"]
    print(spoplaylist)

    i=0

    # count wich playlist is bigger


    for items in spoitemplaylist:
        #print(items)
        nombre_SPO = nombre_SPO + 1




    # get youtube full playlist


    ytresp = ytmusic.get_playlist(playlistId=plYTB_id)
    ytitem = ytresp['tracks']
    ytitemtitle = []
    for items in ytitem:
        ytitemtitle = items['title']
    #print(ytitemtitle)
        nombre_YTB = nombre_YTB + 1
        #print(items)
    #print(ytitem)













    def ytbtospo(spoitemplaylist,ytitem):
        p = 0
        list_to_add = []
        artist_list_to_add = []
        for items in spoitemplaylist:
            itemstrack = items['track']['name']
            for items in ytitem:
                if itemstrack == items['title']:
                    print('ok donc cest pas lui a mettre')
                else:

                    if items['title'] in list_to_add:
                        print('')
                    else :
                        artist = items['artists'][0]['name']
                        list_to_add.append(items['title'])
                        artist_list_to_add.append(artist)
        for items in list_to_add:
            print('ITEMS IN LIST TO ADD     ' + items)
            if items in spoitemplaylist:
                print('already in the playlist')
            else :
                songnametoSPO = items
                print('items')
                artistnametoSPO = artist_list_to_add[p]
                p = p + 1
                SPOquery = artistnametoSPO + ' ' + songnametoSPO
                spoadd(SPOquery)







    def spotoytb(spoitemplaylist,ytitem):
        n = 0
        list_to_add = []
        artist_list_to_add = []
        for items in ytitem:
            itemstrack = items['title']
            for items in spoitemplaylist:
                if itemstrack == items['track']['name']:
                    print('')
                else:
                    #print(itemstrack + ' GROCACA ELSE  ' + items['track']['name'])
                    if items['track']['name'] in list_to_add:
                        print('')
                    else:
                        list_to_add.append(items['track']['name'])
                        track = items['track']
                        artist = track['artists'][0]
                        artist_list_to_add.append(artist['name'])
        print(list_to_add)
        print(artist_list_to_add)
        for items in list_to_add:
            if items in ytitem :
                print('already in the playlist')
            else:
                songnametoYTB = items
                artistnametoYTB = artist_list_to_add[n]
                n = n + 1
                YTBquery = artistnametoYTB + ' ' + songnametoYTB

                ytbadd(YTBquery)



    #search for a song and put it in the youtube playlist

    def ytbadd(YTBquery):
        video_ids = []
        search_results = ytmusic.search(query=YTBquery)
        print(search_results)
        video_result = search_results[0]
        video_ids.append(video_result['videoId'])
        ytmusic.add_playlist_items(playlistId=plYTB_id,videoIds=video_ids)
        print('add' + '  ' +'to' + '  ' +'Youtube' + '  ' +YTBquery)



    n=0


    # search for a song on spotify and add it to the playlist

    def spoadd(SPOquery):

        sposearch_results = sp.search(q=SPOquery,limit=1)
        spoidsearchresult = sposearch_results["tracks"]["items"][0]["id"]
        spoidadd_to_playlist = [spoidsearchresult]
        sp.playlist_add_items(playlist_id=plSPO_id,items=spoidadd_to_playlist)
        print('add'+ '  ' +'to' + '  ' +'Spotify' + '  ' + SPOquery)




    #print(nombre_YTB)
    #print(nombre_SPO)
    if nombre_YTB > nombre_SPO:
        print('nombre_YTB est plus grand')
        caca = ytbtospo(spoitemplaylist,ytitem)


    if nombre_YTB < nombre_SPO:
        print('nombre_SPO est plus grand')
        prout = spotoytb(spoitemplaylist,ytitem)

    print('done')
    a = a+1
    time.sleep(20)
    n=0
    list_to_add = []
    artist_list_to_add = []

