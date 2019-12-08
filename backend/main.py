import flask
from flask_cors import CORS
from espn_scraper import pull_from_db
import logging

logging.basicConfig(filename='log_file.log', level=logging.WARNING,
                    format='%(asctime)s: %(levelname)s: %(processName)s :%(message)s:')
app = flask.Flask(__name__, static_folder='../react-frontend/build/static',
                    template_folder='../react-frontend/build')
CORS(app)

# Route for the main page, only has GET method.
@app.route('/', methods=['GET'])
def index():
    return flask.render_template("index.html")

# Route for the client to pull the most updated data from the db.
# It's of-course already filters to send only games from the last 24 hours that has already started.
@app.route('/games', methods=['GET'])
def games():
    logging.debug('latest games has been requested from the REST api.')
    latest_games = pull_from_db.get_games_from_db()
    output = []
    for game in latest_games:
        logging.debug('Output for client: added data about game {}, which is a match between {} and {}'
                      .format(game['_id'], game['away'], game['home']))
        home = game['home']
        away = game['away']
        homeImg = pull_from_db.get_team_logo(home)
        awayImg = pull_from_db.get_team_logo(away)
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
