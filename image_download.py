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

def downloadTweets(username, tweet_count, api):

    #Gets tweets from specified user handle
    try:
        tweets = api.user_timeline(screen_name=username,
                                   count = tweet_count,
                                   include_rts=False,
                                   exclude_replies=True)

    except Exception as e:
        print(e)
        sys.exit()

    # Creates new folder for output
    if not os.path.exists('TwitterImg'):
        os.makedirs('TwitterImg')

    saved = 0
    media_tweets = set()

    for post in tweets:
        media = post.entities.get('media', [])
        if (len(media) > 0):
            media_tweets.add(media[0]['media_url'])
        #if (post.entities['media'][0]['type'] == 'photo'):
            #media_tweets.add(post.entities['media'][0]['media_url'])
#            saved = saved + 1;

    for files in media_tweets:
        wget.download(files, out='TwitterImg/')
        saved = saved + 1

        
def main():
    cparse = config_parse("config.cfg")
    api = authorization(cparse) 
    
#    username = input("\nPlease enter a twitter handle: ")
#    output = input("\What is the name of the folder you would like the files to be stored in? ")
#    tweet_count = input("\How many images would you like in your video?")

    posts = downloadTweets('BU_Tweets', 100, api)
    #analysis = doAnalysis(output)    


if __name__ == '__main__':
    main()
            


    
    
