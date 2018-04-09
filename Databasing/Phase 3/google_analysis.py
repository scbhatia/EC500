# Shivani Bhatia
# EC500 C1 Building Software
# API Project - Google Vision Analysis
# google_analysis.py

import os
import io
import json

import google.cloud.vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/shivanibhatia/EC500-google.json"


def doAnalysis(vision_client, output):
    descp = []
    
    os.chdir(output)
    for filename in os.listdir('.'):
        #print(filename)
        with io.open(filename, 'rb') as image_file:
            content = image_file.read()

        image = google.cloud.vision.types.Image(content=content)

        response = vision_client.label_detection(image=image)
        
        for label in response.label_annotations:
            features = {}
            if (label.score > 0.9):
                features['description'] = label.description
                features['score'] = str(round(label.score * 100,2))
                descp.append(features)

        with open('descriptions.json', 'w') as outfile:
            json.dump(descp, outfile, indent=4, sort_keys=True)

