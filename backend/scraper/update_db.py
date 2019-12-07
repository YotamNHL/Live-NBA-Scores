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

# Querying the games that are from the last 24 hours timeframe AND has already started.
def get_latest_games():
    latest_games = collection.find({
        "game_time": {'$gte': datetime.timestamp(datetime.now()) - 86400},
        # "away_score": {'$ne': "No score yet"}
    })
    return latest_games


# scrape all games of given date, and load them into the database.
# if scraped keys already in the db, then update the relevant values (scores, and time updated).
def scrape_and_load(date):
    previews_data = get_latest_games()
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
    new_data = get_latest_games()
    if previews_data == new_data:
        pass
    else:
        try:
            requests.post(url="http://127.0.0.1:5000", data={'has_been_updated': True})
            print("The data has been changed since the last scraping! the server has been notified.")
        except Exception:
            pass