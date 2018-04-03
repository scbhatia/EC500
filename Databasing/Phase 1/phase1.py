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

    print("Below is the information for the requested airport: \n")
    for item in search:
        pprint.pprint(search)

def Add(code, latitude, longitude, name, city, state, country, woeid, tz, phone, email, url, runway, elevation, icao, flights, carriers):
    client = MongoClient()
    db = client.Airports

    entry = {"code": code,
             "lat": latitude,
             "lon": longitude,
             "name": name,
             "city": city,
             "state": state,
             "country": country,
             "woeid": woeid,
             "tz": tz,
             "phone": phone,
             "email": email,
             "url": url,
             "runway_length": runway,
             "elev": elevation,
             "icao": icao,
             "direct_flights": flights,
             "carriers": carriers
             }
    
    db.Airports.insert(entry)

    
    
if __name__ == "__main__":
    os.system("mongod")
    Create()
    action = raw_input("Would you like to search (S) or insert (I) into the database? ")
    
    if action == 'S':
        field = raw_input("Please enter the field you are looking for: ")
        val = raw_input("Please enter a keyword: ")
        Find(field, val)
    else if action == 'I':
        code = raw_input("Please enter an airport code: ")
        latitude = raw_input("Please enter a latitude coordinate: ")
        longitude = raw_input("Please enter a longitude coordinate: ")
        name = raw_input("Please enter the airport name: ")
        city = raw_input("Please enter the name of the city: ")
        state = raw_input("Please enter the name of the state: ")
        country = raw_input("Please enter the name of the country: ")
        woeid = raw_input("Please enter the woeid: ")
        tz = raw_input("Please enter the tz: ")
        phone = raw_input("Please enter the phone number: ")
        email = raw_input("Please enter the email address: ")
        url = raw_input("Please enter the url: ")
        runway = raw_input("Please enter the runway length: ")
        elevation = raw_input("Please enter the elevation: ")
        icao = raw_input("Please enter the icao: ")
        flights = raw_input("Please enter the direct flights to the airport: ")
        carriers = raw_input("Please enter the carriers at the airport: ")
        Add(code, latitude, longitude, name, city, state, country, woeid, tz, phone, email, url, runway, elevation, icao, flights, carriers)
    else:
        print("Please enter a valid input.")
