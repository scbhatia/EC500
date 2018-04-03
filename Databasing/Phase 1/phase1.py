import json
import os
from pymongo import MongoClient

# Connect to Mongodb
def Create():
    client = MongoClient()

    fname = open("airports.json", 'r')
    data = json.load(fname.read())

    db = client.Airports
    db.Airports.insert_many(data)

    print("Database Updated")

def Find(field, val):
    client = MongoClient()
    db = client.Airports
    search = db.Airports.find_one({field: val})

    print("The 
    
if __name__ == "__main__":
    os.system("mongod")
    Create()
    
