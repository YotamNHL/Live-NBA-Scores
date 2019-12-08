from pymongo import MongoClient
import csv
import logging

logging.basicConfig(filename='log_file.log', level=logging.WARNING,
                    format='%(asctime)s: %(levelname)s: %(processName)s :%(message)s:')

# Opens the csv sheet that contains the client key.
with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        mongoClientKey = line[0]


# Connects to the MongoDB.
def connect_db():
    try:
        cluster = MongoClient(mongoClientKey)
        db = cluster["NBA_games_results"]
        logging.debug('Connected to the data base successfully.')
        return db
    except Exception as e:
        print("main.py -" + e)
        return -1
