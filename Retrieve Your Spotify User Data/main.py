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
TOKEN = "BQCM_Fnc2NScw2uAJ3XyWL83IJSgTf3C5ExZRrV2Iidc53jB5FFyOs4AdwC1ml9c0uacywvGsEk3GCRWTGq5SA23Q7Oo3h7aD68irrEGdUC7bkp8_TjYMH-K-6_AqUPJ6u5er3CKYr2PFkptRbgnB23nU4YKOtZ2wG64CclS3k52QCKMsd-BLeA"
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
    #data = requests.get(url).json()
    # print(data)

    song_name = []
    artist_names = []
    played_at = []
    release_date = []
    available_markets = []


    for song in data["items"]:
        song_name.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        available_markets.append(song["track"]["available_markets"])
        #release_date.append(song["track"]["release_date"])

    song_dict = {
        "song_name" : song_name,
        "artist_names" : artist_names,
        #"release_date" : release_date,
        "available_markets" : available_markets
    }


    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_names", "available_markets" ])
    
    print(song_df)
