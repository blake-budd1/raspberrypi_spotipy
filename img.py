#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import requests
import urllib.request
import cv2
#import screeninfo
#import pyautogui
import re
MJ_URL = "http://the-modern-jukebox-react-app.vercel.app/api/messages"

DEVICE_ID="9481c5394e791db42f0c8325eaf86efb1cf98d02"
CLIENT_ID="62d7db029474470d9910002d8e2c71fa"
CLIENT_SECRET="62d6fbba1a794b55a5be7e83216ddc5f"



while True:
    try:
        get_list = requests.get(MJ_URL)
        print(get_list)
        get_list.raise_for_status()
        
        # handle data being returned in json format
        data = get_list.json()
        
    except requests.exceptions.HTTPError as e:
        print(e.response.text)
        
    while len(get_list) != 0:
        try:
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                        client_secret=CLIENT_SECRET,
                                                        redirect_uri="http://localhost:8080",
                                                        scope="user-read-playback-state,user-modify-playback-state"))
            
            
            
            # always using data[0], just removing after done with until list is empty
            # parse the current song in queue
            data_now = data.pop(0)
            uri = data_now[0]["uri"]
            user_access_token = data_now[0]["userAcessToken"]
            track_name = data_now[0]["trackName"]
            track_artist = data_now[0]["trackArtist"]
            track_cover = data_now[0]["trackCover"]
            
            print("uri: ", uri)
            print("user access: ", user_access_token)
            print("track name: ", track_name)
            print("track artist: ", track_artist)
            print("track cover ", track_cover)
            
            # deal with image processing:
            urllib.request.urlretrieve(track_cover, track_name)
            
            # load image
            im = cv2.imread(track_name)
            
            # improve image resolution
            hires = cv2.pyrUp(im)
            hires2 = cv2.pyrUp(hires)
            hires3 = cv2.pyrUp(hires2)
            
            # setting fullscreen
            cv2.namedWindow("Album", cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("Album", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            
            # show image
            cv2.imshow("Album", hires3)
            cv2.waitKey(0)
            
            
            sp.start_playback(device_id=DEVICE_ID, context_uri=uri)

            # destroy image
            cv2.destroyAllWindows()

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
        except Exception as e:
            print(e)
            pass

        finally:
            print("Cleaning  up...")
