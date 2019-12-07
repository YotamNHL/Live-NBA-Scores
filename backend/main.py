import flask
from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import csv

app = flask.Flask(__name__, static_folder='../react-frontend/build/static', template_folder='../react-frontend/build')

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        mongoClientKey = line[0]

cluster = MongoClient(mongoClientKey)
db = cluster["NBA_games_results"]
collection = db["games_sessions"]


@app.route('/', methods=['GET'])
def get_all_latest_games():
    print("before getting the collection")
    latest_games = collection.find({
        "game_time": {'$gte': datetime.timestamp(datetime.now()) - 86400},
        # "away_score": {'$ne': "No score yet"}
    })
    print("after getting the collection")
    output = []
    for game in latest_games:
        output.append(game)
    return flask.render_template("index.html", token=output)


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
