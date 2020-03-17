import requests
from bs4 import BeautifulSoup


url = 'https://leagueoflegends.fandom.com/wiki/Tryndamere'

r = requests.get(url)

soup = BeautifulSoup(r.content)

print(soup.prettify())
print(r.content[:100])
