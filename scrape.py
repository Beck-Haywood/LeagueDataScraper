import requests
from bs4 import BeautifulSoup
import re

url = 'https://leagueoflegends.fandom.com/wiki/Tryndamere'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
# Should work on all wikis
c_title = soup.find('span', attrs = {"style": "font-weight:bold; text-transform:uppercase; font-size:16px; color:#dddddd;"}).text.strip()
# Should work on all wikis
c_name = soup.select_one('.page-header__title').text.strip()

#c_icon = soup.select_one('img', attrs = {"height": "50", "width": "50"})
c_icon_tag = soup.find(lambda tag: tag.name=="img" and tag.has_attr("height")
and int(tag["height"]) is 50)
c_icon = c_icon_tag["data-src"]

    #roles = soup.find('span', attrs = {"data-param": "Skirmisher"})
    #c_role = roles.select_one('.mw-redirect').text.strip()

# a Selects the span with the type inside
    #a = soup.find('span', attrs = {"data-param": "Melee"})
# Then it filters through the span to single out the type
    #c_type = a.select_one('.mw-redirect').text.strip()
print(c_name)
# print(c_type)
# print(c_role)
print(c_title)
print(c_icon)

#soup = BeautifulSoup(r.content)

#print(soup.prettify())
#print(r.content[:100])
