import datetime
import json
import sqlite3
from datetime import datetime

import pandas as pd
import requests
import sqlalchemy
from sqlalchemy.orm import sessionmaker

DATABASE_LOCATION = "sqlite://my_played_tracks.sqlite"
USER_ID = "22hkkqxsnuncuzcgmwimr5mma"
TOKEN = "BQD4JV-QS4XE2LAjoKeXCS5ceeN7q2982UwR7E8D7ENT0EQ8iZ_h1O5avoGflSVUSbjRARA8Ido3ijxCJ3TM6L0bbGzDhbrtzct62_wrUv-gSYdzAv14gVPLDzcnvXEk1_hP8JQXrC0H6x97qNKwD8c7F9FVN4p8GqsAq4NKGan_zJpGzxnCcI1wrijz58UDRpHRTQfdrcCe"
if __name__ == "__main__":
    headers = {
        "Accept" :  "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days = 60)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    req = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)
    data = req.json()
    print(data)
    
    song_name = []
    artist_names = []
    played_at = []
    release_date = []
    available_markets = []


    for song in data["items"]:
        song_name.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        available_markets.append(song["track"]["available_markets"])
        release_date.append(song["track"]["name"])

    song_dict = {
        "song_name" : song_name,
        "artist_names" : artist_names,
        "release_date" : release_date,
        "available_markets" : available_markets
    }


    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_names", "available_markets", "release_date"])
    
    print(song_df)
