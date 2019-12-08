import espn_scraper

connect_result = espn_scraper.pull_from_db.get_team_logo("Hapoel")
print(connect_result)