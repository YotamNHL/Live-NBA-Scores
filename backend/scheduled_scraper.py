from datetime import datetime, timedelta
from time import sleep
import schedule
from espn_scraper import scrape_and_load


today = (datetime.strftime(datetime.now(), "%Y%m%d"))
yesterday = (datetime.strftime((datetime.now() - timedelta(days=1)), "%Y%m%d"))

schedule.every(30).seconds.do(lambda: scrape_and_load(today))
schedule.every(30).seconds.do(lambda: scrape_and_load(yesterday))

while 1:
    schedule.run_pending()
    sleep(1)
