import tweepy # pip3 install tweepy

# Create twitter account, if you don't have one
# Generate API & Access tokens from the link below
# https://developer.twitter.com/, Navigate to Apps and app name to generate all keys & secrets

API_KEY = 'bwEFzTsrqIQswrOahG5lUASeN'
API_SECRET = 'jZSM1qJfUvIKtctV6hOfdnWqpioGq3tCZt20dbsylZSaeK67ns'
ACCESS_TOKEN = '1189692749127258112-r7GpYp1ZXrSj0qip5vHPU2UrTdbuYG'
ACCESS_TOKEN_SECRET = '0Mepu7yIenuT79KboAY35sHaBvwTWSyYDVrlMPQd0PXfv'

# Authenticate and make sure your keys work
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Extract latest 100 tweets with hashtag Women's History Month
tweets = api.search(q="Women's History Month", lang="en", rpp=100)
for tweet in tweets:
    USER = tweet.user.name
    TEXT = tweet.text
    RETWEETS = str(tweet.retweet_count)
    LOCATION = tweet.geo
    LANGUAGE = tweet.lang
    CREATED = str(tweet.created_at)
    SOURCE = tweet.source
    print(USER, " | ", TEXT, " | ", RETWEETS, " | ", LOCATION, " | ", LANGUAGE, " | ", CREATED, " | ", SOURCE)

# Create a class that listens streaming tweets with hashtag Women's History Month", "#WHM", "Women in history", "WomenInTechHistory

class Tweet_Stream(tweepy.StreamListener):
    # Inherting tweepy.StreamListener class in to Tweet_Stream class
    def __init__(self, passed_api):
        self.api = passed_api
        self.me = api.me()

    # Extract, Transform & Loadt the data into a flatfile
    def on_status(self, tweet):
        USER = tweet.user.name
        TEXT = tweet.text
        RETWEETS = tweet.retweet_count
        CREATED = tweet.created_at
        SOURCE = tweet.source
        tfile = open("C:/Users/cynthiajuma/Desktop\PROGRAMMING/DATA_ENGINEERING/Twitter_Project/tweets_extract.csv", "a", encoding="utf-8")
        output = USER, " | ", TEXT, " | ", RETWEETS, " | ", LOCATION, " | ", LANGUAGE, " | ", CREATED, " | ", SOURCE, "\n"
        tfile.write(str(output))
        tfile.close()


# Run the background and observe updates in tfile. You can make a tweet with these hashtags to verify
tweets_listener = Tweet_Stream(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Women's History Month", "#WHM", "Women in history", "WomenInTechHistory"], languages=["en"])
