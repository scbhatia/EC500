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

    file = open("image_analysis.txt", "a")
    
    os.chdir(output)
    for filename in os.listdir('.'):
        #print(filename)
        with io.open(filename, 'rb') as image_file:
            content = image_file.read()

        image = google.cloud.vision.types.Image(content=content)

        response = vision_client.label_detection(image=image)

        file.write(filename + ' Labels: ')
        file.write('\n')
        
        for label in response.label_annotations:
            if (label.score > 0.9):
                file.write(label.description + " " + str(round(label.score * 100,2)))
                file.write('\n')

        file.write('\n')
        
def main():
    vision_client = google.cloud.vision.ImageAnnotatorClient()
    doAnalysis(vision_client, 'ImgVal')

if __name__ == '__main__':
    main()

