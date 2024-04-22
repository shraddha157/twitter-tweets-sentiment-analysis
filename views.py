from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse

# Create your views here.

def button(request):
    return render(request,'TWEETAPP/hi.html')

def twt(request):
    import os

    import tweepy as tw
    if request.method == 'POST':
        Htag = request.POST.get('Htag')
        numb = int(request.POST.get('numb'))
        request.session['number'] = numb
        request.session['hashtag'] = Htag


    # import pandas as pd

    # communication with twitter api

    # const express = require('express');
    # const Twitter = require('twit');
    # const app = express();

    # app.listen(3000, () => console.log('Server running'))

    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    OAUTH_TOKEN = ""
    OAUTH_TOKEN_SECRET = ""

    auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    api = tw.API(auth, wait_on_rate_limit=True)

    # Define the search term and the date_since date as variables
    search_words = Htag
    date_since = "2020-08-01"

    '''Below you use .Cursor() to search twitter for tweets containing the search term #wildfires. You can restrict the number of tweets returned by specifying a number in the .items() method.
     .items(5) will return 5 of the most recent tweets.
    '''

    # Collect tweets
    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(numb)

    '''.Cursor() returns an object that you can iterate or loop over to access the data collected. Each item in the iterator has various attributes that you can access to get information about
     each tweet including:'''
    mylist=[]
    # Iterate and print tweets
    for tweet in tweets:
        print(tweet.text)
        mylist.append(tweet.text)
    return render(request, 'TWEETAPP/twt.html',{'content':mylist,'gvalue':Htag})
def value(request):
    if request.method == 'POST':
        Htag = request.POST.get('Htag')
    return HttpResponse(Htag)
def sa(request):
    import re
    import tweepy
    from tweepy import OAuthHandler
    from textblob import TextBlob

    class TwitterClient(object):

        def __init__(self):

            consumer_key = ''
            consumer_secret = ''
            access_token = ''
            access_token_secret = ''

            try:

                self.auth = OAuthHandler(consumer_key, consumer_secret)

                self.auth.set_access_token(access_token, access_token_secret)

                self.api = tweepy.API(self.auth)
            except:
                print("Error: Authentication Failed")

        def clean_tweet(self, tweet):

            return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

        def get_tweet_sentiment(self, tweet):

            analysis = TextBlob(self.clean_tweet(tweet))

            if analysis.sentiment.polarity > 0:
                return 'positive'
            elif analysis.sentiment.polarity == 0:
                return 'neutral'
            else:
                return 'negative'

        num = request.session['number']
        def get_tweets(self, query, count=num):

            tweets = []

            try:

                fetched_tweets = self.api.search(q=query, count=count)

                for tweet in fetched_tweets:

                    parsed_tweet = {}

                    parsed_tweet['text'] = tweet.text

                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                    if tweet.retweet_count > 0:

                        if parsed_tweet not in tweets:
                            tweets.append(parsed_tweet)
                    else:
                        tweets.append(parsed_tweet)

                return tweets

            except tweepy.TweepError as e:

                print("Error : " + str(e))


    def main():

        api = TwitterClient()
        tag=request.session['hashtag']

        tweets = api.get_tweets(query=tag, count=200)

        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

        mylist=[]
        mylist1=[]
        mylist2=[]
        #print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
        p=100 * len(ptweets) / len(tweets)
        mylist.append(p)

        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']


        #print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
        n=100 * len(ntweets) / len(tweets)
        mylist.append(n)


        #print("Neutral tweets percentage: {} % \ ".format(100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)))
        nt=100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)
        mylist.append(nt)


        print("\n\nPositive tweets:")
        for tweet in ptweets[:20]:
            print(tweet['text'])
            mylist1.append(tweet['text'])

        print("\n\nNegative tweets:")
        for tweet in ntweets[:20]:
            print(tweet['text'])
            mylist2.append(tweet['text'])
        return mylist,mylist1,mylist2

    var=main()
    print(var[0][0])
    data1=var[0][0]
    print(var[0][1])
    data2=var[0][1]
    print(var[0][2])
    data3=var[0][2]
    data4=var[1]
    data5=var[2]



    return  render(request,'TWEETAPP/sa.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})


