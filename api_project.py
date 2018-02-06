# Shivani Bhatia
# EC500 C1 Building Software
# API Project - Main File
# api_project.py

import image_download as twit 
import video_converter as fmpg
import google_analysis as gimg


    
def main():
    cparse = twit.config_parse("config.cfg")
    api = twit.authorization(cparse) 

    try:
        username = input("Please enter a twitter handle: ")
        output = input("What is the name of the folder you would like the files to be stored in? ")
        tweet_count = int(input("How many images would you like in your video? "))

    except:
        print("Error. Invalid input. Please try again.")
        sys.exit(1)

    twit.downloadTweets(username, api, tweet_count, output)
    twit.renameImages(output)
    

if __name__ == '__main__':
    main()
