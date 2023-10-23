from api_requests import get_sports_data

api_key = 'ab4925c6d41fc69f5087691d26ccc5ec'

if __name__ == "__main__":
    sports_data = get_sports_data(api_key)

    if sports_data is not None:
        # Process and use the sports data as needed
        for sport in sports_data:
            print(f"Sport: {sport['title']}, Sport Key: {sport['key']}")
    else:
        print("Failed to retrieve sports data.")