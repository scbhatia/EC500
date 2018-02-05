# Shivani Bhatia
# EC500 C1 Building Software
# API Project - Twitter Image Downloader
# image_download.py

import configparser
import wget
import sys
import os
import json
import tweepy

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

def downloadTweets(username, tweet_count, api, output):

    #Gets tweets from specified user handle
    try:
        tweets = api.user_timeline(screen_name=username,
                                   count = 3200,
                                   include_rts=False,
                                   exclude_replies=True)

    except Exception as e:
        print(e)
        sys.exit()

    # Creates new folder for output
    if not os.path.exists(output):
        os.makedirs(output)

    saved = 0
    media_tweets = set()

    for post in tweets:
        media = post.entities.get('media', [])
        if (len(media) > 0):
            if (media[0]['type'] == 'photo'):
                media_tweets.add(media[0]['media_url'])

    for files in media_tweets:
        if (saved < tweet_count):
            wget.download(files, out=output)
            saved = saved + 1

        
def main():
    cparse = config_parse("config.cfg")
    api = authorization(cparse) 

    try:
        username = input("\nPlease enter a twitter handle: ")
        output = input("\nWhat is the name of the folder you would like the files to be stored in? ")
        tweet_count = int(input("\nHow many images would you like in your video?"))

    except:
        print("Error. Invalid input. Please try again.")
        sys.exit(1)
        
    posts = downloadTweets('asdfgytfghnjikjht', 200, api, 'ImageComics')
    #analysis = doAnalysis(output)    


if __name__ == '__main__':
    main()
            


    
    
