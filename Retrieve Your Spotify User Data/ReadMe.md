# Extract
Variables:
  - USER_ID: <your Spotify UserId>
  - TOKEN: Generate this from <a href="https://developer.spotify.com/console/get-recently-played/?limit=50&after=&before=">here</a> 
# Transform

# Load
- The load stage uses the SQlite which is a relational SQL database. 
- sqlalchemy has an ORM library used to query the data from main.py
- The ORM(Object Relational Marker) library allows you to query databases directly in python, without SQL.
