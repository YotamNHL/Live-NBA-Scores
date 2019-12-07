from pymongo import MongoClient
from datetime import datetime

# print('Connecting to database')
cluster = MongoClient("mongodb+srv://TalJG:SteveNash13@cluster0-zmj3y.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["NBA_games_results"]
collection = db["games_sessions"]


def get_games_from_db():
    print('Get last games')
    latest_games = collection.find({
        "game_time": {'$gte': datetime.timestamp(datetime.now()) - 86400},
        "away_score": {'$ne': "No score yet"}
    })
    return latest_games


documents = get_games_from_db()
for game in documents:
    print("game ID: " + game['_id'])
    print(game['home'] + ": " + game['home_score'])
    print(game['away'] + ": " + game['away_score'])


print("done")
