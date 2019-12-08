import flask
from flask_cors import CORS
from espn_scraper import pull_from_db

app = flask.Flask(__name__, static_folder='../react-frontend/build/static', template_folder='../react-frontend/build')
CORS(app)

# Route for the main page, only has GET method.
@app.route('/', methods=['GET'])
def index():
    return flask.render_template("index.html")


@app.route('/games', methods=['GET'])
def games():
    latest_games = pull_from_db.get_games_from_db()
    print("latest games has been requested from the REST api!")
    output = []
    for game in latest_games:
        print("home team name from data is: " + game['home'])
        print("away team name from data is: " + game['away'])
        home = game['home']
        away = game['away']
        homeImg = pull_from_db.get_team_logo(home)
        print("home image: " + homeImg)
        awayImg = pull_from_db.get_team_logo(away)
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


if __name__ == "__main__":
    app.run(debug=False)
