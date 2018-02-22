import tweepy
import os
from tweepy import OAuthHandler
import json
import wget
import argparse
import configparser
import io
import glob
import google.cloud.vision
import subprocess
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/shivanibhatia/EC500-google.json"

consumer_key = "i9KmpNAI22WYysSczCPievhln"
consumer_secret = "bnCJZIE9h8tE55KlnZjV48RvEdsNW4pdPSgl7ddroUSKTDvEXY"
access_key = "956290315689824256-Gv1H4JNuoWZPlBSDo6dp1ui0kOatK7h"
access_secret = "AxrmezyWatl68QWQ2nf6D3bULIe366aL4oHb3JUC8oQ8H"
# export GOOGLE_APPLICATION_CREDENTIALS = "/home/mjhuria/Desktop/google_key.json"
Link = []
# TODO: Limit by number of tweets?


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Download pictures from a Twitter feed.')
    parser.add_argument(
        'username', type=str, help='The twitter screen name from the account we want to retrieve all the pictures')
    parser.add_argument('--num', type=int, default=100,
                        help='Maximum number of tweets to be returned.')
    parser.add_argument('--output', default='pictures/', type=str,
                        help='folder where the pictures will be stored')
    parser.add_argument('--fps', type=int, default=20,
                        help='Frame rate per seconds for the video')

    args = parser.parse_args()
    return args


def parse_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


def init_tweepy():
    # Status() is the data model for a tweet
    tweepy.models.Status.first_parse = tweepy.models.Status.parse
    tweepy.models.Status.parse = parse
    # User() is the data model for a user profil
    tweepy.models.User.first_parse = tweepy.models.User.parse
    tweepy.models.User.parse = parse


def authorise_twitter_api():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth


def ConverttoVideo(output, frm_rate):
    ffmpeg_command = ["ffmpeg", "-y", "-framerate", str(frm_rate), "-i", output + '/' + "%d.jpg", "-vf",
                      "scale=w=1280:h=720:force_original_aspect_ratio=1,pad=1280:720:(ow-iw)/2:(oh-ih)/2", "-vcodec", "libx264", output + '/' + "TwitterVideo.mp4"]
    subprocess.call(ffmpeg_command)


def download_images(api, username, num_tweets, output_folder, frm_rate):
    tweets = api.user_timeline(screen_name=username, count=num_tweets)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    downloaded = 0
    while (len(tweets) != 0):
        last_id = tweets[-1].id

        for status in tweets:
            media = status.entities.get('media', [])
            if(len(media) > 0 and downloaded < num_tweets):
                Link = media[0]['media_url']
                wget.download(
                    media[0]['media_url'], out=output_folder + '/' + str(downloaded) + '.jpg')
                downloaded += 1
        tweets = api.user_timeline(
            screen_name=username, count=num_tweets, max_id=last_id - 1)
    ConverttoVideo(output_folder, frm_rate)


def doAnalysis(output):
    vision_client = google.cloud.vision.ImageAnnotatorClient()
    # print(output+'*.jpg')
    descp = []
    for files in glob.glob(output + '/' + '*.jpg'):
        img1 = files
        with io.open(img1, 'rb') as image_file:
            content = image_file.read()
        image = google.cloud.vision.types.Image(content=content)
        response = vision_client.label_detection(image=image)
        web_detect = vision_client.web_detection(image=image).web_detection
        for entity in web_detect.web_entities:
            descp.append(entity.description)
            print('Description: {}'.format(entity.description.encode("utf-8")))

    with open('labels.json', 'w') as outfile:
        json.dump(descp, outfile, indent=4, sort_keys=True)


def main():
    arguments = parse_arguments()
    username = arguments.username
    num_tweets = arguments.num
    output_folder = arguments.output
    frm_rate = arguments.fps
    auth = authorise_twitter_api()
    #wait rate limit to be set to true optherwise tweeter limits the number\
    #of tweets that can be checked.
    api = tweepy.API(auth, wait_on_rate_limit=True)
#call for download images
    download_images(api, username, num_tweets, output_folder, frm_rate)
    analysis = doAnalysis(output_folder)


if __name__ == '__main__':
    main()
