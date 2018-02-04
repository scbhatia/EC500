# Shivani Bhatia
# EC500 C1 Building Software
# API Project

import configparser
import wget
import sys
import os
from tweepy import API, OAuthHandler, Stream

import json

import io
import google.cloud.vision

def config_parse(filename):
    cparse = configparser.ConfigParser()
    cparse.read(filename)
    return cparse

def authorization(cparse):
    auth = OAuthHandler(cparse['API']['consumerKey'], cparse['API']['consumerSecret'])
    auth.set_access_token(cparse['API']['accessToken'], cparse['API']['accessTokenSecret'])
    api = API(auth)
    return api

#Retrieves tweets from given twitter handle and downloads images to a specified folder 
def downloadTweets(username, tweet_count, api, output):
    try:
        tweets = api.user_timeline(screen_name=username, count=300, include_rts=False, exclude_replies=True)

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
    
    while (length > 0):
        last_post = tweets[-1].id - 1

        for post in tweets:
            if hasattr(post, 'extended_entities'):
                images = post.extended_entities.get('media',[])
                image_len = len(images)

                if (image_len != 0):
                    if 'media' in post.extended_entities:
                        for media_files in tweet.extended_entities['media']:
                            if not 'video_info' in media_files:
                                for image_media in tweet.extended_entities['media']:
                                    media_tweets.add(image_media['media_url'])

    for links in media_tweets:
        wget.download(links, out=output)
                                    

#ffmpeg compiles all of the images into a video file
def makeVideo():



    
def main():
    cparse = config_parse("config.cfg")
    api = authorization(cparse)
    
    proxy = cparse['PROXY']['http_proxy']
    os.environ['http_proxy'] = proxy
    os.environ['https_proxy'] = proxy
    
    username = input("\nPlease enter a twitter handle: ")
    output = input("\What is the name of the folder you would like the files to be stored in? ")
    tweet_count = input("\How many images would you like in your video?")

    posts = downloadTweets(username, tweet_count, api, output)
    analysis = doAnalysis(output)
    
