# ETL:
- ETL stands for extract, transform and load
- The process is used to blend data from multiple sources to build a data warehouse or other unified data repository
- During this process, data is taken (extracted) from a source system, converted (transformed) into a format that can be analyzed, and stored (loaded) into a data warehouse or other system

## Constant variables:
- DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
- USER_ID: your Spotify UserId
- TOKEN: Generate this from <a href="https://developer.spotify.com/console/get-recently-played/?limit=50&after=&before=">here</a> 
## Dependency Installation:
- Download or upgrade pip: python get-pip.py/python -m pip install --upgrade pip
- Use pip to install dependencies: 
  - pip3 install DateTime
  - pip3 install pandas
  - pip3 install requests
  - pip3 install SQLAlchemy
- sqlite3: included in the standard library
- json: built-in module

# Extract

# Transform

# Load
- The load stage uses the SQlite which is a relational SQL database. 
- sqlalchemy has an ORM library used to query the data from main.py
- The ORM(Object Relational Marker) library allows you to query databases directly in python, without SQL.
