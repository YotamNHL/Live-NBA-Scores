from datetime import datetime, timedelta
from time import sleep
from espn_scraper import scrape_and_load
import schedule
from art import tprint

# Textual intro
tprint("Yotam's   Scraper")
print("Starting scheduled scraping now!")

# Init dates
today = ""
yesterday = ""


# Getting the exact date format (i.e. - 20191126) for the scraping method that uses the espn url structure.
# We do it every day because we want to keep track of the right dates even if the scraper is working for over 24 hours.
def get_dates():
    global today
    global yesterday
    today = (datetime.strftime(datetime.now(), "%Y%m%d"))
    yesterday = (datetime.strftime((datetime.now() - timedelta(days=1)), "%Y%m%d"))


# Every 30 seconds, scrape today's results and yesterday's. the reason for scraping yesterday's results as well is
# to avoid edge case in which a game has started a day prior, but is still in play. Or, to avoid edge cases that are
# involving the difference in time-zones.
schedule.every(30).seconds.do(lambda: scrape_and_load(today))
schedule.every(30).seconds.do(lambda: scrape_and_load(yesterday))
schedule.every().day.do(lambda: get_dates(today, yesterday))

# Get dates for the first time.
get_dates()

# Infinite loop that run all the scheduled operations.
while 1:
    schedule.run_pending()
    sleep(10)
