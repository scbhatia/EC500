# Shivani Bhatia
# EC500 C1 Building Software
# API Project - FFMPEG Video Converter
# video_converter.py

import subprocess

def makeVideo(output):
    subprocess.call(["ffmpeg", "-framerate", "1/3","-i", output + "/image%d.jpg", "-c:v", 'libx264', "-r", "10", "-s", "vga", "-pix_fmt", "yuv420p", "video.mp4"])
