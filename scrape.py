import requests
from bs4 import BeautifulSoup
import re



url = 'https://leagueoflegends.fandom.com/wiki/Tryndamere'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

c_name = soup.select_one('.page-header__title').text.strip()
#c_type = soup.select('.mw-redirect')
roles = soup.find('span', attrs = {"data-param": "Skirmisher"})
c_role = roles.select_one('.mw-redirect').text.strip()

# a Selects the span with the type inside
a = soup.find('span', attrs = {"data-param": "Melee"})
# Then it filters through the span to single out the type
c_type = a.select_one('.mw-redirect').text.strip()
print(c_name)
print(c_type)
print(c_role)

#soup = BeautifulSoup(r.content)

#print(soup.prettify())
#print(r.content[:100])
