from pymongo import MongoClient
import csv

# Opens the csv sheet that contains the client key.
with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        mongoClientKey = line[0]


# Connects the MongoDB.
def connect_db():
    try:
        print('Connecting to database')
        cluster = MongoClient(mongoClientKey)
        db = cluster["NBA_games_results"]
        print("Connected successfully.")
        return db
    except Exception as e:
        print("main.py -" + e)
        return -1
