import csv
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com'
}

hockey_team = []

for page in range(1, 25):
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={page}'
    print(f"Data scrape start now... scraping page is : {url}")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print('Connecting page OK!')
        soup = BeautifulSoup(response.text, 'html.parser')
        teams = soup.find_all('tr', class_='team')

        for team in teams:
            name = team.find('td', class_='name').text.strip()
            year = team.find('td', class_='year').text.strip()
            wins = team.find('td', class_='wins').text.strip()
            losses = team.find('td', class_='losses').text.strip()
            win_percent = team.find('td', class_='pct').text.strip()
            goals_for = team.find('td', class_='gf').text.strip()
            goals_a = team.find('td', class_='ga').text.strip()
            plus_minus = team.find('td', class_='diff').text.strip()

            hockey_team.append({
                'Team Name': name,
                'Year': year,
                'Wins': wins,
                'Losses': losses,
                'Win %': win_percent,
                'Goals For (GF)': goals_for,
                'Goals Against (GA)': goals_a,
                '+ / -': plus_minus
            })

    else:
        print(f"Data not found! Error code is : {response.status_code}")
    time.sleep(1)

df = pd.DataFrame(hockey_team)
df.to_csv('Hockey_Teams.csv', index=False)
print(f"Data scraping completed! Summery is: {df.head()}")