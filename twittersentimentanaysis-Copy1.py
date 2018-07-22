# coding: utf-8

import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob as tb
import pandas as pd

consumerKey = 'SV8UUKCsWGbHB0fBG9xEWdDDl'
consumerSecret = 'gu7fZc75qzoZ20Cf1Y4FDSBGiX40H5L5dlMhmVqFecMZzUzBuo'
accessToken = '1074255938-ea90Lx6fUeZ6MW780cHpmmozr4XDmC47VH4cKpM'
accessTokenSecret = 'Npsz59fFPutq2aCbdfO6l0ylYjHZAgZxkojUoWHV8gsIh'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

def scrape_tweet(searchTweet):
    tweets = tweepy.Cursor(api.search, q=searchTweet).items(100)
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
    train_json = pd.read_json('devclan.json')
    positive = train['Sentiment'] == 'Positive'
    negative = train['Sentiment'] == 'Negative'
    neutral = train['Sentiment'] == 'Neutral'
    time = train['Tweettime']
    Sentiment = train['Sentiment']

    size = train['Sentiment'].value_counts().tolist()
    sice = Sentiment.tolist()
    labels = list(set(sice))

    colors = ['yellow', 'blue', 'red']
    explode = (0.1, 0.1, 0.1)
    explode_list = list(explode)
    if len(labels) == 2:
        colors = colors[:2]
        explode = explode[:2]
    elif len(labels) == 3:
        colors = colors
        explode = explode
    elif len(labels) == 1:
        colors = colors[:1]
        explode = explode[:1]

    plt.pie(size, colors=colors, labels=labels, shadow=True, startangle= 90, autopct='%1.1f%%', explode = explode)
    plt.legend(labels)
    return plt.show()
    #return train_json

