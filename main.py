#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import requests

MJ_URL = "http://the-modern-jukebox-react-app.vercel.app/api/messages"

DEVICE_ID="raspberryPi"
CLIENT_ID="5cb64b1dbd2f4306af892c8c367b4764"
CLIENT_SECRET="f074ffd4fb584cccb686e0aea131228f"

while True:
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Entering loop...\n")
            # error checking for http requests
            try:
                x = requests.get(MJ_URL) # Get the spotify uri from the front-end queue
                print(x.text)
                x.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print (e.response.text)
            
            # transfer playback device to the raspberry pi
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # start playing the uri that we got in x 
            sp.start_playback(device_id=DEVICE_ID, context_uri=x)
            
            # error checking for http requests
            try:
                x = requests.delete(MJ_URL)
                x.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(e.response.text)

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
