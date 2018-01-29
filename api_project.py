# Shivani Bhatia
# EC500 C1 Building Software
# API Project

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

def downloadTweets(username, tweet_count, api, output):
    try:
        tweets = api.user_timeline(screen_name=username, count=300, include_rts=False, exclude_replies=True)
        saved = 0
        
        
    except Exception as e:
        print(e)
        sys.exit()

    try:
        os.mkdir(output)
        os.chdir(output)
    except:
        os.chdir(output)

    try:
        os.mkdir(username)
        os.chdir(username)
    except:
        os.chdir(username)

    if not 
    
    
def main():
    cparse = config_parse("config.cfg")
    api = authorization(cparse)
    
    proxy = cparse['PROXY']['http_proxy']
    os.environ['http_proxy'] = proxy
    os.environ['https_proxy'] = proxy
    
    username = input("\nPlease enter a twitter handle: ")
    output = input("\What is the name of the folder you would like the files to be stored in? ")
    tweet_count = 50;

    posts = getTweets(username, tweet_count, api, output)
    
