# Shivani Bhatia
# EC500 C1 Building Software
# API Project - Twitter Image Downloader
# image_download.py

import configparser
import wget
import sys
import os

from tweepy import API, OAuthHandler, Stream

def config_parse(filename):
    cparse = configparser.ConfigParser()
    cparse.read(filename)
    return cparse

def authorization(cparse):
    auth = OAuthHandler(cparse['API']['consumerKey'], cparse['API']['consumerSecret'])
    auth.set_access_token(cparse['API']['accessToken'], cparse['API']['accessTokenSecret'])
    api = API(auth)
    return api

def downloadTweets(username, tweet_count, api, output_folder):

    #Gets tweets from specified user handle
    try:
        tweets = api.user_timeline(screen_name=username, include_rts=False, exclude_replies=True)

    except Exception as e:
        print(e)
        sys.exit()

    try:
        os.mkdir(output)
        os.chdir(output)
    except:
        os.chdir(output)

    saved = 0
    length = len(tweets)
    media_tweets = set()


    
    
