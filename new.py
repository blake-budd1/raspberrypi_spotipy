#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import requests
import urllib.request
from PIL import Image
import cv2
#import screeninfo
#import pyautogui
import re
MJ_URL = "http://the-modern-jukebox-react-app.vercel.app/api/messages"

DEVICE_ID="9481c5394e791db42f0c8325eaf86efb1cf98d02"
CLIENT_ID="62d7db029474470d9910002d8e2c71fa"
CLIENT_SECRET="62d6fbba1a794b55a5be7e83216ddc5f"

x  = 'spotify:track:45vW6Apg3QwawKzBi03rgD'

while True:
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        
            # start playing the uri that we got in x 
        sp.start_playback(device_id=DEVICE_ID, context_uri=x)


    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")









