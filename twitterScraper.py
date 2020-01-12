import tweepy
from textblob import TextBlob

consumer_key = 'rGYSFadfjnwpIe2sAejjOamHU'
consumer_secret = 'WuumWTuYovyn4SvtE4SjtGyUo5zV6frmgAxX7da1YoZugAtri5'

access_token = '10274632-DoZYno3D6AvCYX3BtRaLwiE6BK7FWvryW5npSJagE'
access_token_secret = 'jffzlghvMNwVWAmB6RE7bYBaTPfTvlyuTygYueX77NGuK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)