# Shivani Bhatia
# EC500 C1 Building Software
# Databasing Project - Main File
# phase2.py

import image_download as twit 
import video_converter as fmpg
import google_analysis as gimg
import mongo_database as mdb

#import google.cloud.vision
from bson.json_util import loads

def main():
    cparse = twit.config_parse("config.cfg")
    api = twit.authorization(cparse)
    vision_client = gimg.google.cloud.vision.ImageAnnotatorClient()

    for x in range(20):
        try:
            username = input("Please enter a twitter handle: ")
            output = input("What is the name of the folder you would like the files to be stored in? ")
            #tweet_count = int(input("How many images would you like in your video? "))

        except:
            print("Error. Invalid input. Please try again.")

        twit.downloadTweets(username, api, 10, output)
        twit.renameImages(output)
        gimg.doAnalysis(vision_client, output)
        fmpg.makeVideo(output)
    
        with open("descriptions.json", "r") as f:
            data = loads(f.read())
        
        mdb.Update(username, data)
    
    
if __name__ == '__main__':
    main()
