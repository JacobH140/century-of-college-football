import requests
import pandas as pd
from datetime import datetime
import time

API_KEY = "(api key)"
BASE_URL = "https://api.collegefootballdata.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def get_games_for_year(year):
    url = f"{BASE_URL}/games"
    params = {
        "year": year,
        "division": "fbs"
    }
    
    response = requests.get(url, headers=HEADERS, params=params)
    
    if response.status_code != 200:
        print(f"Failed to fetch data for {year}. Status code: {response.status_code}")
        return []
    
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Error decoding JSON response for {year}")
        return []

def create_historical_games_csv(start_year, end_year, output_file):
    all_data = []
    
    for year in range(start_year, end_year + 1):
        print(f"Fetching data for {year}...")
        games = get_games_for_year(year)
        
        for game in games:
            if 'start_date' in game and game['start_date']:
                try:
                    game_date = datetime.strptime(game['start_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
                    unix_timestamp = int(time.mktime(game_date.timetuple()))
                except ValueError as e:
                    print(f"Date parsing error in {year}: {e} for date {game['start_date']}")
                    continue
                
                data_row= {
                    'timestamp': unix_timestamp,
                    'Team1': game['home_team'],
                    'Team2': game['away_team'],
                    'Conf1': game.get('home_conference', 'Unknown'),
                    'Conf2': game.get('away_conference', 'Unknown')
                }
                all_data.append(data_row)
    
    df = pd.DataFrame(all_data)
    df = df.sort_values('timestamp')
    df.to_csv(output_file, index=False)
    print(f"Data from {start_year} to {end_year} saved to {output_file}")

if __name__ == "__main__":
    start_year = 1924
    end_year = 2024
    create_historical_games_csv(start_year, end_year, f'all_cfb_games_{start_year}_{end_year}.csv')