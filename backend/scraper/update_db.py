import pymongo
from pymongo import MongoClient
from datetime import datetime
from .scrape import nba_scores_scraper
import requests
import csv

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        mongoClientKey = line[0]

cluster = MongoClient(mongoClientKey)
db = cluster["NBA_games_results"]
collection = db["games_sessions"]


# scrape all games of given date, and load them into the database.
# if scraped keys already in the db, then update the relevant values (scores, and time updated).
def scrape_and_load(date):
    game_list = nba_scores_scraper(date)
    print("OK! I scraped that: ")
    for game in game_list:
        try:
            db.games_sessions.insert_one(game)
            print("Added new game session documents to the database. (" + date + ")")
        except pymongo.errors.DuplicateKeyError:
            db.games_sessions.update_one({"_id": game["_id"]},
                                         {"$set": {"away_score": game["away_score"],
                                                   "home_score": game['home_score'],
                                                   "time_of_update": datetime.strftime(datetime.now(),
                                                                                       '%Y-%m-%d %I:%M%p')
                                                   }})
            print("Updated the database. (" + date + ")")