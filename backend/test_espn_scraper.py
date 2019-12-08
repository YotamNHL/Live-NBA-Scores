import unittest
import espn_scraper


class TestScrape(unittest.TestCase):

    # Test Purpose: to see that the scraping process itself pulls the exact right data in the right order without
    # any miss-matches.
    def test_scrape(self):
        scrape_result = espn_scraper.scrape.nba_scores_scraper(20190101)
        # By definition of the scrape method, we will receive an argument of 'time of update'.
        # for the sake of the test we simply compare it to itself.
        update_time = scrape_result[0]['time_of_update']
        true_result = [{'_id': '401071225', 'game_time': 1546293600.0, 'away': 'Jazz',
                        'home': 'Raptors', 'away_score': '116', 'home_score': '122',
                        'time_of_update': update_time},
                       {'_id': '401071226', 'game_time': 1546293600.0,
                        'away': 'Pistons', 'home': 'Bucks', 'away_score': '98',
                        'home_score': '121', 'time_of_update': update_time},
                       {'_id': '401071228', 'game_time': 1546293600.0, 'away': 'Trail Blazers', 'home': 'Kings',
                        'away_score': '113', 'home_score': '108', 'time_of_update': update_time},
                       {'_id': '401071227', 'game_time':
                        1546293600.0, 'away': 'Knicks', 'home': 'Nuggets', 'away_score': '108',
                        'home_score': '115', 'time_of_update': update_time},
                       {'_id': '401071229', 'game_time': 1546293600.0, 'away': '76ers',
                        'home': 'Clippers', 'away_score': '119', 'home_score': '113',
                        'time_of_update': update_time}]
        self.assertEqual(scrape_result, true_result)

    # Test Purpose: to see verify that we're able to pull the right logo image from our database.
    def test_logo_pulling(self):
        test_result = espn_scraper.pull_from_db.get_team_logo("Mavericks")
        true_result = "http://content.sportslogos.net/logos/6/228/thumbs/22834632018.gif"
        self.assertEqual(test_result, true_result)

    # Test Purpose: to assert that if we request a logo for a team that's not in our data base for some reason,
    # we get the default logo instead of crashing the pulling method.
    def test_logo_not_found(self):
        test_result = espn_scraper.pull_from_db.get_team_logo("Hapoel Holon")
        true_result = "https://theundefeated.com/wp-content/uploads/2017/06/nbalogo.jpg"
        self.assertEqual(test_result, true_result)


if __name__ == '__main__':
    unittest.main()
