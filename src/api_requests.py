import requests

# Replace 'YOUR_API_KEY' with your actual API key
apiKey = 'ab4925c6d41fc69f5087691d26ccc5ec'
sport = 'americanfootball_nfl'
regions = 'us'
markets = 'h2h'
date = '2023-10-22T12:00:00Z'

# Define the API endpoint for historical NFL odds
url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds-history/?apiKey={apiKey}&regions={regions}&markets={markets}&date={date}"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    historical_odds_data = response.json()
    # Process and store the data as needed
else:
    print("Error: Unable to retrieve historical odds data")

