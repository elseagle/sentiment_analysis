import flask
from flask import request, jsonify
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob as tb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

consumerKey = 'SV8UUKCsWGbHB0fBG9xEWdDDl'
consumerSecret = 'gu7fZc75qzoZ20Cf1Y4FDSBGiX40H5L5dlMhmVqFecMZzUzBuo'
accessToken = '1074255938-ea90Lx6fUeZ6MW780cHpmmozr4XDmC47VH4cKpM'
accessTokenSecret = 'Npsz59fFPutq2aCbdfO6l0ylYjHZAgZxkojUoWHV8gsIh'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
def scrape_tweet(searchTweet, tweet_num):
    tweets = tweepy.Cursor(api.search, q=searchTweet).items(tweet_num)
    data=[]

    for tweet in tweets:
        text=tweet.text
        tweet_time = tweet.created_at
        textWords=text
        
        analysis = tb(textWords)
        polarity = 'Positive'
        if(analysis.sentiment.polarity < 0):
            polarity = 'Negative'
        if(0<=analysis.sentiment.polarity <=0.2):
            polarity = 'Neutral'
    
        dic={}
        dic['Sentiment']=polarity
        dic['Tweet'] = textWords
        dic['Tweettime'] = tweet_time
        data.append(dic)
    df=pd.DataFrame(data)
    df.to_csv('devclan.csv')

    train = pd.read_csv('devclan.csv',index_col=0)
    train = train['Sentiment']
    train.to_json('devclan.json')
    return jsonify(train_json)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Twitter sentiment Analysis API</h1>
<p>A prototype API for checking people's sentiment against keywords inputed</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/sentiment/all', methods=['GET'])
def api_all():
    try:
        scrape_tweet(name, num_of_tweet)
    except TypeError:
        pass
    return "Up and running"
    
app.run()