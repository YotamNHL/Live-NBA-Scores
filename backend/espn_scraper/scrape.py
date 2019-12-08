from requests_html import HTMLSession
from datetime import datetime


# This scraper will scrape the following data: Games IDs, date and time of game session,
# teams that played, each team's total score in the game, and the time of update (of the scrape method called).
def nba_scores_scraper(given_date):
    given_date_str = str(given_date)
    # request and render the page (including js elements), notice that the games are divided by their calender date,
    # which means we'll also need to scrape each game's exact time of beginning, in order to eventually filter the
    # relevant games to show in our app (games from the last 24 hours).
    url = "https://www.espn.com/nba/scoreboard/_/date/" + given_date_str
    session = HTMLSession()
    r = session.get(url)

    # Repeats initial rendering until it succeeds.
    # I preferred it skipping and trying to render again on the next call instead of just putting
    # a higher timeout value. The reason is that after testing it, it seems like in most cases that it fails to load,
    # the quickest solution is simply to stop and retry - instead of wait longer for it to render.
    try:
        r.html.render(timeout=20)
    except Exception:
        pass

    # scraping the raw elements for each important feature: teams, scores, and ids, and times.
    # ids are extremely important in order to update the game's document with a unique reference value
    # for each game session.
    total_scores = r.html.find("td.total")
    total_teams = r.html.find("span.sb-team-short")
    urls_for_ids = r.html.find("a.mobileScoreboardLink")
    total_times = r.html.find("th.date-time")

    # init the lists prior to pulling the data, in order to append each chunk in it's relevant list.
    games_ids = []
    games_times = []
    scores = []
    teams = []

    # iterate through the links in order to slice the unique ids of the games sessions from them.
    for url in urls_for_ids:
        for val in url.links:
            games_ids.append([val[17::]])

    # iterate through the total_times element to append all game times into one list.
    for time in total_times:
        try:
            games_times.append(datetime.timestamp(datetime.strptime(
                (time.attrs['data-date'].replace('T', ' ').replace('Z', 'am')),
                '%Y-%m-%d %H:%M%p')))
        # if (for any reason) we will scrape an older date, the game's date and time data
        # won't be reachable via the espn dashboard, hence I've added this workaround in that case.
        except Exception:
            games_times.append(datetime.timestamp(datetime.strptime(
                (given_date_str[0:4] + "-" + given_date_str[4:6] + "-" + given_date_str[6:8] + " 00:00am"),
                '%Y-%m-%d %H:%M%p')))

    # iterate through the total_scores element to append all scores into one list.
    for score in total_scores:
        scores.append(score.text)

    # iterate through the total_teams element to append all teams into one list.
    for team in total_teams:
        teams.append(team.text)

    # for games that don't have the score element on site (game has yet to begin), we append 'no score yet'.
    # it's a workaround to avoid having miss-matched data later on, and also to have a placeholder for a game
    # that has yet to begin.
    if len(teams) != len(scores):
        for i in range(len(scores), len(teams)):
            scores.append('No score yet')

    # After gathering and attaching all the corresponding fields, we will now create the
    # final document that is meant to be updated into our database.
    list_of_all_games = []
    num_of_games = len(games_ids)
    for i in range(num_of_games):
        temp_dict = dict()
        temp_dict['_id'] = games_ids.pop(0)[0]
        temp_dict['game_time'] = games_times.pop(0)
        temp_dict['away'] = teams.pop(0)
        temp_dict['home'] = teams.pop(0)
        temp_dict['away_score'] = scores.pop(0)
        temp_dict['home_score'] = scores.pop(0)
        temp_dict['time_of_update'] = datetime.strftime(datetime.now(), '%Y-%m-%d %I:%M%p')
        list_of_all_games.append(temp_dict)

    return list_of_all_games
