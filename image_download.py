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
        tweets = api.user_timeline(screen_name=username,
                                   include_rts=False,
                                   exclude_replies=True)

    except Exception as e:
        print(e)
        sys.exit()

    # Creates new folder for output
    try:
        os.mkdir(output)
        os.chdir(output)
    except:
        os.chdir(output)


    saved = 0
    length = len(tweets)
    media_tweets = set()

    for post in tweets:
        if (post.entities['media'][0]['type'] == 'photo' && saved < tweet_count):
            media_tweets.add(post.entities['media'][0]['media_url'])
            saved += 1;

    for files in media_tweets:
        wget.download(files, out=output_folder)

def main():
    cparse = config_parse("config.cfg")
    api = authorization(cparse) 
    
    username = input("\nPlease enter a twitter handle: ")
    output = input("\What is the name of the folder you would like the files to be stored in? ")
    tweet_count = input("\How many images would you like in your video?")

    posts = downloadTweets(username, tweet_count, api, output)
    #analysis = doAnalysis(output)    

    
            
            


    
    
