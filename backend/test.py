from requests_html import HTMLSession

url = "https://www.espn.com/nba/scoreboard/_/date/20191204"
session = HTMLSession()
r = session.get(url)

while r.html.find("td.total") is None:
    r.html.render(timeout=60)
    print(r.html.find("td.total"))
