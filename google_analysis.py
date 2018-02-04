# Shivani Bhatia
# EC500 C1 Building Software
# API Project - Google Vision Analysis
# google_analysis.py

import os
import io

import google.cloud.vision

def __init__(vision_client, output):
    vision_client = google.cloud.vision.ImageAnnotatorClient()

def doAnalysis(vision_client, output):

    with io.open(output, 'rb') as image_file:
        content = image_file.read()

    image = google.cloud.vision.types.Image(content=content)

    response = vision_client.label_detection(image=image)

    print('Labels: ')
        
    for label in response.label_annotations:
        print(label.description)
