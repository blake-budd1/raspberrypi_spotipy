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
                # need to figure out which uri we are working with depending on what the queue holds:
                
                x.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print (e.response.text)
            
            # transfer playback device to the raspberry pi
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

            # deal with changing the image that is being displayed (update the album cover)
            
            #getting image; This will be the album cover that the uri provides
            url = "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228" #"https://img2.goodfon.com/wallpaper/nbig/1/e9/cat-kot-koshka-trava-chernyy.jpg"

            #get image name
            image = re.findall("[^/]+(?=/$|$)", url)[0]
            
            # start playing the uri that we got in x 
            sp.start_playback(device_id=DEVICE_ID, context_uri=x)

            urllib.request.urlretrieve(url, image) #"cat-kot-koshka-trava-chernyy.jpg")

            #load image
            im = cv2.imread(image) #r"cat-kot-koshka-trava-chernyy.jpg")
            
            # improving resolution of image
            hires = cv2.pyrUp(im)
            hires2 = cv2.pyrUp(hires)
            hires3 = cv2.pyrUp(hires2)
            
            #setting full screen
            cv2.namedWindow("Album", cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("Album", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            
            #show image
            cv2.imshow("Album", hires3)
            
            #show title bar
            #cv2.setWindowTitle("Album", "Call Me Maybe")
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
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









