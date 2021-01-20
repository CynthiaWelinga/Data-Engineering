import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime 
import sqlite3

DATABASE_LOCATION = "sqlite://my_played_tracks.sqlite"
USER_ID = "22hkkqxsnuncuzcgmwimr5mma"
TOKEN = "BQAlikcFA1Cl2mG-NPQYRFZ7Oavprwa1hiueQHJIIv2ZjhezKF9fwR7RWYIv6FVhVAf8vlAxUYRecf7vnz_tM3juIG8yZGFL8c6mcYTAXL4QtLjSaspbE89nnyPUxGvQBmoT_emg4G-X9oc946DHs9Q1c0iv0nOaQyR9axOAj4ueBVXf3jAEF18"
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
