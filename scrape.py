import requests
from bs4 import BeautifulSoup


url = 'https://leagueoflegends.fandom.com/wiki/Tryndamere'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

champion_name = soup.select_one('.page-header__title').text.strip()
print(champion_name)
#soup = BeautifulSoup(r.content)

#print(soup.prettify())
#print(r.content[:100])
