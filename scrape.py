import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://leagueoflegends.fandom.com/wiki/Tryndamere'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

def scrapeWikis():
    jsond = {}

    championsfile = open('champions.txt', 'r')
    champions = [line.split(' ') for line in championsfile.readlines()]
    #print(champions)
    for champion in champions[0]:
        url = f'https://leagueoflegends.fandom.com/wiki/{champion}'

        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')

        c_title = soup.find('span', attrs = {"style": "font-weight:bold; text-transform:uppercase; font-size:16px; color:#dddddd;"}).text.strip()
        c_name = soup.select_one('.page-header__title').text.strip()

        c_icon_tag = soup.find(lambda tag: tag.name=="img" and tag.has_attr("height")
        and int(tag["height"]) is 50)
        c_icon = c_icon_tag["data-src"]
        add_json = { f"{c_name}": {
            "title": f"{c_title}",
            "icon": f"{c_icon}"
        }}
        jsond.update(add_json) 
        # print(c_name)
        # print(c_title)
        # print(c_icon)
    with open('data.txt', 'w') as outfile:
        json.dump(jsond, outfile)
    #print(json)

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
# c_health = soup.find_all('section', attrs={'style': ''}, limit = 1)
# a Selects the span with the type inside
    #a = soup.find('span', attrs = {"data-param": "Melee"})
# Then it filters through the span to single out the type
    #c_type = a.select_one('.mw-redirect').text.strip()
#print(table)
#child = table.find_next_sibling
#print(child)


table = soup.find('table', attrs={'class':'champion-header'})
table_body = table.find('tbody')
#print('table::::::::::', table)

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    print('Column:', cols)


#     #if sibling.has_attr("class"):
# all_tbody = soup.find_all('tr')
# for sibling in soup.tr.next_siblings:
#     #if sibling.has_attr("class"):
#     #print(sibling.find_next_sibling("tr"))
#     each_tr = sibling.find_next_sibling("tr")
#     for sibling in each_tr.next_siblings:
#         print(sibling)
    #print(repr(sibling))
# print(all_tbody)

print(c_name)
# print(c_type)
# print(c_role)
print(c_title)
print(c_icon)
# print(c_health)

#soup = BeautifulSoup(r.content)

#print(soup.prettify())
#print(r.content[:100])
#scrapeWikis()