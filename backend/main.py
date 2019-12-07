import flask
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import csv

app = flask.Flask(__name__, static_folder='../react-frontend/build/static', template_folder='../react-frontend/build')
CORS(app)

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        mongoClientKey = line[0]

try:
    print('Connecting to database')
    cluster = MongoClient(mongoClientKey)
    db = cluster["NBA_games_results"]
    collection = db["games_sessions"]
    logos_collection = db["Teams_Logos"]
    print("Connected successfully.")
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
    print("latest games has been requested from the REST api!")
    output = []
    for game in latest_games:
        print("home team name from data is: " + game['home'])
        print("away team name from data is: " + game['away'])
        home = game['home']
        away = game['away']
        homeImg = logos_collection.find_one({'name': home})['url']
        print("home image: " + homeImg)
        awayImg = logos_collection.find_one({'name': away})['url']
        print("away image: " + awayImg)
        output.append({'id': game['_id'],
                       'home': game['home'],
                       'away': game['away'],
                       'home_score': game['home_score'],
                       'away_score': game['away_score'],
                       'homeImg': homeImg,
                       'awayImg': awayImg
                       })
    return flask.jsonify(output)


@app.route('/testingpage', methods=['GET'])
def testingpage():
    testjson = {'test': "succeeded"}
    return testjson


if __name__ == "__main__":
    app.run(debug=False)
