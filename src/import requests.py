import requests
import pandas as pd  # Import pandas for data manipulation

# Your existing code to retrieve upcoming odds
api_key = 'ab4925c6d41fc69f5087691d26ccc5ec'
sport_key = 'americanfootball_nfl'
odds_format = 'american'
region = 'us'

api_url_upcoming = f'https://api.the-odds-api.com/v4/sports/{sport_key}/odds?regions={region}&oddsFormat={odds_format}&apiKey={api_key}'

response_upcoming = requests.get(api_url_upcoming)

if response_upcoming.status_code == 200:
    upcoming_data = response_upcoming.json()
    
    # Assuming 'upcoming_data' is a list of dictionaries, you can access its elements using indices
    if len(upcoming_data) > 0:
        # Access the first element (index 0) in the list
        first_event = upcoming_data[0]
        
        # Now, 'first_event' is a dictionary representing data for the first event
        # You can access specific keys within 'first_event' to get information about the event.
        
        # For example, if 'home_team' and 'away_team' are keys within 'first_event':
        home_team = first_event.get('home_team', 'N/A')
        away_team = first_event.get('away_team', 'N/A')
        
        print(f"Home Team: {home_team}")
        print(f"Away Team: {away_team}")
        
    else:
        print("No upcoming events found.")
    
else:
    print(f"API request for upcoming odds failed with status code: {response_upcoming.status_code}")
