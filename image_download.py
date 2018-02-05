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

def getTweets(username, api):
    try:
        tweets = api.user_timeline(screen_name=username,
                                   count = 3200,
                                   include_rts=False,
                                   exclude_replies=True)

    except Exception as e:
        print(e)
        sys.exit()

    last_id = int(tweets[-1].id - 1)

    downloaded =  0
    
    while True:
        temp_tweets = api.user_timeline(screen_name=username,
                                        max_id=last_id,
                                        include_rts = False,
                                        exclude_replies = True)

        if len(temp_tweets) == 0:
            break
        else:
            last_id = int(temp_tweets[-1].id - 1)
            tweets = tweets + temp_tweets

    return tweets

def downloadTweets(tweets, max_img, output):

    saved = 0
    media_tweets = set()

    if not os.path.exists(output):
        os.makedirs(output)
        
    for posts in tweets:
        media = posts.entities.get('media', [])
        if (len(media) > 0):
            if (media[0]['type'] == 'photo'):
                media_tweets.add(media[0]['media_url'])

    for files in media_tweets:
        if (saved < max_img):
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
            


    
    
