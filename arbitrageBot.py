import requests

class ArbitrageBot:
    def __init__(self):
        self.bookmakers = {
            'Bookmaker1':'https://api.bookmaker1.com/odds',
            'Bookmaker2':'https:apo.bookmaker2.com/odds',
            'Bookmaker3':'https://api.bookmaker3.com/odds'
        }

        def find_arbitrage(self):
            for bookmaker, url in self.bookmakers.items():
                odds = requests.get(url).json()
                for event, event_odds in odds.items():
                    for team, team_odds in event_odds.items():
                        for other_bookmaker, other_url in self.bookmakers.items():
                            if bookmaker == other_bookmaker:
                                continue
                            other_odds = requests.get(other_url).json()
                            other_team_odds = other_odds[event][team]
                            if team_odds['win'] > other_team_odds['win']:
                                print(f'Arbitrage opportunity found: Bet on {team} to win with {bookmaker} at odds {team_odds["win"]} and lay with {other_bookmaker} at odds {other_team_odds["win"]}')
arbitrage_bot = ArbitrageBot
arbitrage_bot.find_arbitrage()                


                    