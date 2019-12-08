from espn_scraper import pull_from_db

# logo_url = pull_from_db.get_team_logo("76ers")
# print(logo_url)

all_games = pull_from_db.get_games_from_db()
for game in all_games:
    print(game)

logo_url = pull_from_db.get_team_logo('Heat')