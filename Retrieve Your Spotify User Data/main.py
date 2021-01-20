import datetime as dt
import json
import sqlite3
from datetime import datetime, timedelta

import pandas as pd
import requests
import sqlalchemy
from sqlalchemy.orm import sessionmaker

DATABASE_LOCATION = "sqlite://my_played_tracks.sqlite"
USER_ID = "22hkkqxsnuncuzcgmwimr5mma"
TOKEN = "BQBsEqe5DgFYeJ403S_MXK7GwdFtaAFoPezl7hwyUDkg0X95CMZzBuhpMZVRw01R071eJumMXoENz1slr3kxUlbJ65AbXh2y36ZcJSx2gkFk5hFdBnPkhjEAmJ4XivYySwENLR9a2W38SXQowBWT7ODk0SROC3EXtgGn0pKGjcx8FfxJNpgbwMQghsBQWv3AzODxyS5SANzc"
if __name__ == "__main__":
    headers = {
        "Accept" :  "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    today = dt.datetime.now()
    yesterday = today - dt.timedelta(days = 60)
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
        release_date.append(song["track"]["album"]["release_date"])

    song_dict = {
        "song_name" : song_name,
        "artist_names" : artist_names,
        "release_date" : release_date,
        "available_markets" : available_markets
    }


    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_names", "available_markets", "release_date"])
    
    print(song_df)
