import requests

def get_sports_data(api_key):
    endpoint_url = f'https://api.the-odds-api.com/v4/sports/?apiKey={api_key}'
    response = requests.get(endpoint_url)

    if response.status_code == 200:
        # Parse the JSON response and return the sports data
        return response.json()
    else:
        return None
