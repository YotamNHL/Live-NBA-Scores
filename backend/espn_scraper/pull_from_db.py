from datetime import datetime
from espn_scraper.connect_to_db import connect_db

db = connect_db()
games_sessions = db['games_sessions']
logos_collection = db['Teams_logos']


# a method for querying the games that are from the last 24 hours timeframe AND has already started.
def get_games_from_db():
    print('Get last games')
    latest_games = db.games_sessions.find({
        "game_time": {'$gte': datetime.timestamp(datetime.now()) - 86400},
        "away_score": {'$ne': "No score yet"}
    })
    return latest_games


# a method for pulling a teams image for the UI (notice we keep a different
# collection named "teams_logos" for those images).
def get_team_logo(team_name):
    try:
        teamImg = db.Teams_Logos.find_one({'name': team_name})
        return teamImg['url']
    except Exception:
        teamImg = db.Teams_Logos.find_one({'name': "logo_not_found"})
        return teamImg['url']
    return teamImg
