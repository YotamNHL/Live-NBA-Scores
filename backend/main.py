import flask
from flask_cors import CORS
from flask import request, jsonify
import pymongo
from pymongo import MongoClient
from datetime import datetime
import csv

# with open('credentials.csv', 'r') as input:
#     next(input)
#     reader = csv.reader(input)
#     for line in reader:
#         mongoClientKey = line[0]


app = flask.Flask(__name__, static_folder='../react-frontend/build/static', template_folder='../react-frontend/build')
CORS(app)

try:
    print('Connecting to database')
    cluster = MongoClient("mongodb+srv://TalJG:SteveNash13@cluster0-zmj3y.mongodb.net/test?retryWrites=true&w=majority")
    db = cluster["NBA_games_results"]
    collection = db["games_sessions"]
except Exception as e:
    print("main.py -" + e)


# Querying the games that are from the last 24 hours timeframe AND has already started.
def get_games_from_db():
    print('Get last games')
    latest_games = collection.find({
        "game_time": {'$gte': datetime.timestamp(datetime.now()) - 86400},
        "away_score": {'$ne': "No score yet"}
    })
    return latest_games



@app.route('/', methods=['GET'])
def index():
    return flask.render_template("index.html")


@app.route('/games', methods=['GET'])
def games():
    latest_games = get_games_from_db()
    print(latest_games)
    output = []
    for game in latest_games:
        output.append({'home': game['home'],
                      'away': game['away'],
                      'home_score': game['home_score'],
                      'away_score': game['away_score']
                      })
    return jsonify(output)


@app.route('/updated', methods=['POST'])
def reload_page():
    has_been_updated = request.json['has_been_updated']
    if has_been_updated:
        latest_games = collection.find({
            "game_time": {'$gte': datetime.timestamp(datetime.now()) - 86400},
            # "away_score": {'$ne': "No score yet"}
        })
        output = []
        for game in latest_games:
            output.append(game)
        return flask.render_template("index.html", token=output)


app.run(debug=True)
