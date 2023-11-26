#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import requests
import urllib.request
import cv2
import json
#import screeninfo
#import pyautogui
import re
import os
# Current issue is this is empty, returning 200 code but still has nothing in it
MJ_URL = "http://the-modern-jukebox-react-app.vercel.app/api/queue"

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca" # raspodify device ID (works on hotspot right now)
CLIENT_ID="62d7db029474470d9910002d8e2c71fa"
CLIENT_SECRET="62d6fbba1a794b55a5be7e83216ddc5f"



temp_data = {"uri": "spotify:track:45vW6Apg3QwawKzBi03rgD", "user AccessToken": "BQAnDPRKPKdGXKYDcKhZGa7SyxB85pHQUhz mBbqDtserJSg170brhNm29uFA7jKbvPObwZMNC_mt2W-MDuoYjogscSFLAUk-zp8Xe6p9Q35U2wrMNalZN8sINgnSu2vttvRm-vf6P3NtZTTXT2gYvIfpupYZADiKzU_XF__ObpOJjzbef-t-_osM8TXi47L", "trackName": "WhitehouseRoad", "trackArtist": "Tyler Childers", "trackCover": "https://i.scdn.co/image/ab67616d000062735a38bd36056b909ed607689d" }
# json_data = json.dumps(temp_data, indent=2)
json_data = temp_data
print("data: ", json_data)



print("entering spotify\n")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                            client_secret=CLIENT_SECRET,
                                            redirect_uri="http://localhost:8080",
                                            scope="user-read-playback-state,user-modify-playback-state"))


print("Transfering playback...\n")
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# always using data[0], just removing after done with until list is empty
# parse the current song in queue
# data_now = json_data.pop(0)
print("printing data \n")
uri = json_data["uri"]
user_access_token = json_data["user AccessToken"]
track_name = json_data["trackName"]
track_artist = json_data["trackArtist"]
track_cover = json_data["trackCover"]

print("uri: ", uri)
print("user access: ", user_access_token)
print("track name: ", track_name)
print("track artist: ", track_artist)
print("track cover ", track_cover)

# deal with image processing:
# get image name
#     image = re.findall("[^/]+(?=/$|$)", track_cover)[0]
#     
#     urllib.request.urlretrieve(image, track_name)
#     
#     # load image
#     im = cv2.imread(track_name)
#     
#     # improve image resolution
#     hires = cv2.pyrUp(im)
#     hires2 = cv2.pyrUp(hires)
#     hires3 = cv2.pyrUp(hires2)
#     
#     # setting fullscreen
#     cv2.namedWindow("Album", cv2.WINDOW_NORMAL)
#     cv2.setWindowProperty("Album", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#     
#     # show image
#     cv2.imshow("Album", hires3)
print("starting playback ... \n")


# destroy image
#    cv2.destroyAllWindows()
#    os.remove(image)
print("uri :", [uri])
sp.start_playback(device_id=DEVICE_ID, uris=[uri])
# if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)


