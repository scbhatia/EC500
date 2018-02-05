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

def downloadTweets(username, api, max_img, output):

    media_tweets = set()
    downloaded =  0
    back_count = max_img

    
    try:
        tweets = api.user_timeline(screen_name=username,
                                   include_rts=False,
                                   exclude_replies=True)

    except Exception as e:
        print(e)
        sys.exit()

    for posts in tweets:
        media = posts.entities.get('media', [])
        if (len(media) > 0):
            if (media[0]['type'] == 'photo'):
                media_tweets.add(media[0]['media_url'])
                downloaded = downloaded + 1
                if (downloaded == max_img):
                    break

    if not os.path.exists(output):
        os.makedirs(output)
        
    last_id = int(tweets[-1].id - 1)
    
    while (downloaded < max_img):
        temp_tweets = api.user_timeline(screen_name=username,
                                        max_id=last_id,
                                        include_rts = False,
                                        exclude_replies = True)

        if len(temp_tweets) == 0:
            break
        else:
            for posts in temp_tweets:
                media = posts.entities.get('media', [])
                if (len(media) > 0):
                    if (media[0]['type'] == 'photo'):
                        media_tweets.add(media[0]['media_url'])
                        downloaded = downloaded + 1
                        if (downloaded == max_img):
                            break

            last_id = int(temp_tweets[-1].id - 1)

    for files in media_tweets:
        if (back_count != 0):
            wget.download(files,out=output)
            back_count = back_count - 1

            
def main():
    cparse = config_parse("config.cfg")
    api = authorization(cparse) 

    try:
        username = input("Please enter a twitter handle: ")
        output = input("What is the name of the folder you would like the files to be stored in? ")
        tweet_count = int(input("How many images would you like in your video? "))

    except:
        print("Error. Invalid input. Please try again.")
        sys.exit(1)

    downloadTweets(username, api, tweet_count, output)       


if __name__ == '__main__':
    main()
            


    
    
