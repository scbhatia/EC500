# Shivani Bhatia
# EC500 C1 Building Software
# Databasing Project - Database File
# database.py

import json
import os
from pymongo import MongoClient

#Connect to Mongodb
def Update(username, data):
    client = MongoClient()

    db = client.Descriptions
    entry = {"handle": username,
             "descriptions": data
             }
    
    db.Descriptions.insert(entry)

    print("Database updated")
