# Shivani Bhatia
# EC500 C1 Building Software
# Databasing Project - Database File
# database.py

import json
import os
import datetime
from pymongo import MongoClient

#Connect to Mongodb
def Update(username, data):
    client = MongoClient()

    db = client.Descriptions
    date = datetime.datetime.now()
    newdate = str(now)
    
    entry = {"handle": username,
             "descriptions": data,
             "Date": newdate
             }
    
    db.Descriptions.insert(entry)

    print("Database updated")
