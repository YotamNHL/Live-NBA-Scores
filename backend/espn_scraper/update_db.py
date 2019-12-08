import pymongo
from datetime import datetime
from espn_scraper.scrape import nba_scores_scraper
from espn_scraper import connect_to_db

# Connecting to db and specifically to the games sessions collection.
db = connect_to_db.connect_db()
games_sessions = db['games_sessions']


# scrape all games of given date, and load them into the database.
def scrape_and_load(date):
    game_list = nba_scores_scraper(date)
    print("OK! I scraped that: ")
    for game in game_list:
        try:
            games_sessions.insert_one(game)
            print("Added new game session documents to the database. (" + date + ")")
        # if scraped keys already in the db, then update the relevant values (scores, and time updated).
        except pymongo.errors.DuplicateKeyError:
            games_sessions.update_one({"_id": game["_id"]},
                                         {"$set": {"away_score": game["away_score"],
                                                   "home_score": game['home_score'],
                                                   "time_of_update": datetime.strftime(datetime.now(),
                                                                                       '%Y-%m-%d %I:%M%p')
                                                   }})
            print("Updated the database. (" + date + ")")

