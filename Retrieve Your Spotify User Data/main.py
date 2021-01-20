import datetime as dt
import json
import sqlite3
from datetime import datetime, timedelta

import pandas as pd
import requests
import sqlalchemy
from sqlalchemy.orm import sessionmaker

DATABASE_LOCATION = "sqlite://my_played_tracks.sqlite"
USER_ID = # Spotify Username
TOKEN = # Spotify generated token from https://developer.spotify.com/console/get-recently-played/

if __name__ == "__main__":
    # ETL Extraction
    headers = {
        "Accept" :  "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    today = dt.datetime.now()
    yesterday = today - dt.timedelta(days = 60) # 60 because I haven't used Spotify in two months. You can use 1 day difference to get most recent data
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    
    # Download all songs you've listened to
    req = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)
    data = req.json()
    
    song_name = []
    artist_names = []
    played_at = []
    release_date = []
    available_markets = []
    
    # Extract the data you want from the json object
    for song in data["items"]:
        song_name.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        available_markets.append(song["track"]["available_markets"])
        release_date.append(song["track"]["album"]["release_date"])
        
    # Put extracted data in a dictionary 
    song_dict = {
        "song_name" : song_name,
        "artist_names" : artist_names,
        "release_date" : release_date,
        "available_markets" : available_markets
    }
    # Return the data in a pandas dataframe
    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_names", "available_markets", "release_date"])
    
    print(song_df)
