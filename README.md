# raspberrypi_spotipy
Meant for starting up with the raspberry pi to read from the database, play the song, and eventually handle image data.

["uri": "spotify: Lack:OfbR95FEaJUxiQYaqZZukv", "user AccessToken": "BQAnDPRKPKdGXKYDcKhZGa7SyxB85pHQUhz mBbqDtserJSg170brhNm29uFA7jKbvPObwZMNC_mt2W-MDuoYjogscSFLAUk-zp8Xe6p9Q35U2wrMNalZN8sINgnSu2vttvRm-vf6P3NtZTTXT2gYvIfpupYZADiKzU_XF__ObpOJjzbef-t-_osM8TXi47L","trackName"."WhitehouseRoad",'trackArtist":'Tyler
Childers", "trackCover":"https://i.scdn.co/image/ab67616d000062735a38bd36056b909ed607689d"},


import json

# Given data
data = {
    "uri": "spotify:track:OfbR95FEaJUxiQYaqZZukv",
    "user AccessToken": "BQAnDPRKPKdGXKYDcKhZGa7SyxB85pHQUhz mBbqDtserJSg170brhNm29uFA7jKbvPObwZMNC_mt2W-MDuoYjogscSFLAUk-zp8Xe6p9Q35U2wrMNalZN8sINgnSu2vttvRm-vf6P3NtZTTXT2gYvIfpupYZADiKzU_XF__ObpOJjzbef-t-_osM8TXi47L",
    "trackName": "WhitehouseRoad",
    "trackArtist": "Tyler Childers",
    "trackCover": "https://i.scdn.co/image/ab67616d000062735a38bd36056b909ed607689d"
}

# Convert data to JSON format
json_data = json.dumps(data, indent=2)

# Print the JSON data
print(json_data)
