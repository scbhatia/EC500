# Shivani Bhatia
# EC500 C1 Building Software
# Databasing Project - Using MySQL
# sql.py

import sqlite3
import json

con = sqlite3.connect("airportsql.db")
p = con.cursor()

p.execute('''CREATE TABLE airport_data(code text, lat text, lon text, name text, city text, state text, country text, woeid text, tz text, phone text, email text, url text, runway_length text, elev text, icao text, direct_flights text, carriers text)''')

with open('airports.json') as f:
    new_file = json.load(f.read())
    for info in new_file:
        arr = []
        a = info.values()

        for i in a:
            arr.append()

        c.execute("INSERT INTO airport_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], arr[15], arr[16], arr[17]))

con.commit()
p.close()
con.close()
