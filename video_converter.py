# Shivani Bhatia
# EC500 C1 Building Software
# API Project - FFMPEG Video Converter
# video_converter.py

import subprocess
import os

def makeVideo(output):
    subprocess.call("ffmpeg -pattern_type glob -framerate 1/2 -i '*.jpg' -vf 'scale=w=1280:h=720:force_original_aspect_ratio=1,pad=1280:720:(ow-iw)/2:(oh-ih)/2' -vcodec libx264 TwitterVideo.mp4", shell=True)
