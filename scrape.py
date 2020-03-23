import requests
from bs4 import BeautifulSoup
import re
import json

# url = 'https://leagueoflegends.fandom.com/wiki/Tryndamere'
# url2 = 'https://leagueoflegends.fandom.com/wiki/Tryndamere/Abilities'

# r = requests.get(url)
# r2 = requests.get(url2)

# soup = BeautifulSoup(r.content, 'html.parser')
# soup2 = BeautifulSoup(r2.content, 'html.parser')

def scrapeWikis():
    jsond = {}

    championsfile = open('champions.txt', 'r')
    champions = [line.split(' ') for line in championsfile.readlines()]
    #print(champions)
    # titles = []
    for champion in champions[0]:
        url = f'https://leagueoflegends.fandom.com/wiki/{champion}'
        url2 = f'https://leagueoflegends.fandom.com/wiki/{champion}/Abilities'

        r = requests.get(url)
        r2 = requests.get(url2)

        soup = BeautifulSoup(r.content, 'html.parser')
        soup2 = BeautifulSoup(r2.content, 'html.parser')

        c_title = soup.find('span', attrs = {"style": "font-weight:bold; text-transform:uppercase; font-size:16px; color:#dddddd;"}).text.strip()
        c_name = soup.select_one('.page-header__title').text.strip()

        c_icon_tag = soup.find(lambda tag: tag.name=="img" and tag.has_attr("height")
        and int(tag["height"]) is 50)
        c_icon = c_icon_tag["data-src"]

        c_roles =''
        c_secondary =''
        c_price =''
        c_release =''
        c_last_changed =''
        cols1 = soup.find_all('tr')
        for i in range(1,6):
            #print(cols1[2 * i - 1].find('th').text)
            secondary_attributes = cols1[2 * i].find('td').find_all('a')
            for span in secondary_attributes:
                if not span.find('img'):
                    #print(span.text)
                    if i == 1:
                        c_roles += span.text + ' '
                    if i == 2:
                        c_secondary += span.text + ' '
                    if i == 3:
                        c_price += span.text + ' '
                    if i == 4:
                        c_release += span.text

                    if i == 5:
                        c_last_changed += span.text

                    
            #print('_________________________')
        c_released = c_release.replace('[1]', '')
        c_blue_essence = c_price.split()[0] + ' BE'
        c_riot_points = c_price.split()[1] + ' RP'
        c_resource_bar = c_secondary.split()[0]
        c_aa_type = c_secondary.split()[1]
        c_adaptive_force = c_secondary.split()[2]

        if "_" in champion:
            champion = champion.replace('_', '')
        if "%" in champion:
            champion = champion.replace('%', '')
        if "2" in champion:
            champion = champion.replace('2', '')
        if "7" in champion:
            champion = champion.replace('7', '')
        if "." in champion:
            champion = champion.replace('.', '')
        if "\'" in champion:
            champion = champion.replace('\'', '')
        if champion != 'DrMundo' and champion != 'JarvanIV' and champion != 'KogMaw' and champion != 'LeeSin' and champion != 'MasterYi' and champion != 'MissFortune' and champion != 'RekSai' and champion != 'TahmKench' and champion != 'AurelionSol' and champion != 'XinZhao' and champion != 'TwistedFate' and champion != 'Wukong' and champion != 'WarWick':
            champion = champion.title()
        if champion == 'Wukong':
            champion = 'MonkeyKing'
        if champion == 'Kled':
            champion = 'Kled1'
        print(champion)
        c_health = soup2.find('span', attrs={'id': f'Health_{champion}'}).text
        # c_health_per_lvl = soup2.find('span', attrs={'id': f'Health_{champion}_lvl'}).text

        c_healthregen = soup2.find('span', attrs={'id': f'HealthRegen_{champion}'}).text
        # c_healthregen_per_lvl = soup2.find('span', attrs={'id': f'HealthRegen_{champion}_lvl'}).text

        c_armor = soup2.find('span', attrs={'id': f'Armor_{champion}'}).text
        # c_armor_per_lvl = soup2.find('span', attrs={'id': f'Armor_{champion}_lvl'}).text

        c_magicresist = soup2.find('span', attrs={'id': f'MagicResist_{champion}'}).text
        # c_magicresist_per_lvl = soup2.find('span', attrs={'id': f'MagicResist_{champion}'}).text

        c_attackdamage = soup2.find('span', attrs={'id': f'AttackDamage_{champion}'}).text
        # c_attackdamage_per_lvl = soup2.find('span', attrs={'id': f'AttackDamage_{champion}'}).text

        c_ms = soup2.find('span', attrs={'id': f'MovementSpeed_{champion}'}).text

        c_ar = soup2.find('span', attrs={'id': f'AttackRange_{champion}'}).text

        c_base_as = soup2.find('div', attrs={'data-source': 'attack speed'}).text
        c_base_as = c_base_as.replace('Base AS', '')

        c_ratio_as = soup2.find('div', attrs={'data-source': 'as ratio'}).text
        c_ratio_as = c_ratio_as.replace('AS ratio', '')

        c_windup = soup2.find('div', attrs={'data-source': 'windup'}).text
        c_windup = c_windup.replace('Attack windup', '')

        if champion == 'Jhin':
            c_bonus_as = soup2.find('div', attrs={'data-source': 'bonus as'}).text
            c_bonus_as = c_bonus_as.replace('Bonus AS', '')

        else:
            c_bonus_as = soup2.find('span', attrs={'id': f'AttackSpeedBonus_{champion}_lvl'}).text

        c_gp_radius = soup2.find('div', attrs={'data-source': 'gameplay radius'}).text
        c_gp_radius = c_gp_radius.replace('Gameplay radius', '')
        c_gp_radius = str(c_gp_radius.strip())

        c_pathing_radius = soup2.find('div', attrs={'data-source': 'pathing radius radius'}).text
        c_pathing_radius = c_pathing_radius.replace('Pathing radius', '')
        c_pathing_radius = str(c_pathing_radius.strip())

        c_selection_radius = soup2.find('div', attrs={'data-source': 'selection radius'}).text
        c_selection_radius = c_selection_radius.replace('Selection radius', '')
        c_selection_radius = str(c_selection_radius.strip())

        c_acquisition_radius = soup2.find('div', attrs={'data-source': 'acquisition radius'}).text
        c_acquisition_radius = c_acquisition_radius.replace('Auto radius', '')
        c_acquisition_radius = str(c_acquisition_radius.strip())

        # titles.append(c_title)

        # print(c_name)
        # print(c_title)
        # print(c_icon)
        # print(c_adaptive_force)
        # print(c_aa_type)
        # print(c_resource_bar)
        # print(c_blue_essence)
        # print(c_riot_points)
        # print(c_roles)
        # print(c_secondary)
        # print(c_released)
        # print(c_last_changed)

        # print(c_health)
        # print(c_health_per_lvl)
        # print(c_healthregen)
        # print(c_healthregen_per_lvl)
        # print(c_armor)
        # print(c_armor_per_lvl)
        # print(c_attackdamage)
        # print(c_attackdamage_per_lvl)
        # print(c_magicresist)
        # print(c_magicresist_per_lvl)
        # print(c_ms)
        # print(c_ar)
        # print(c_base_as)
        # print(c_ratio_as)
        # print(c_windup)
        # print(c_bonus_as)

        # print(c_acquisition_radius)
        # print(c_gp_radius)
        # print(c_pathing_radius)
        # print(c_selection_radius)

        add_json = {
            "name": f"{c_name}",
            "title": f"{c_title}",
            "icon": f"{c_icon}",
            "roles": f"{c_roles}",
            "resource_bar": f"{c_resource_bar}",
            "aa_type": f"{c_aa_type}",
            "adaptive_type": f"{c_adaptive_force}",
            "price_be": f"{c_blue_essence}",
            "price_rp": f"{c_riot_points}",
            "release_date": f"{c_released}",
            "last_changed": f"{c_last_changed}",

            "starting_health": f"{c_health}",
            # "health_per_lvl": f"{c_health_per_lvl}",
            "starting_health_regen": f"{c_healthregen}",
            # "health_regen_per_lvl": f"{c_healthregen_per_lvl}",
            "starting_armor": f"{c_armor}",
            # "armor_per_lvl": f"{c_armor_per_lvl}",
            "starting_magic_resist": f"{c_magicresist}",
            # "magic_resist_per_lvl": f"{c_magicresist_per_lvl}",
            "starting_attack_damage": f"{c_attackdamage}",
            # "attack_damage_per_lvl": f"{c_attackdamage_per_lvl}",
            "movementspeed": f"{c_ms}",
            "attack_range": f"{c_ar}",
            "base_attack_speed": f"{c_base_as}",
            "attack_speed_ratio": f"{c_ratio_as}",
            "attack_windup": f"{c_windup}",
            "attack_speed_bonus": f"{c_bonus_as}",
            "gameplay_radius": f"{c_gp_radius}",
            "pathing_radius": f"{c_pathing_radius}",
            "selection_radius": f"{c_selection_radius}",
            "auto_attack_radius": f"{c_acquisition_radius}"
        }

        jsond.update(add_json) 
        # print(add_json)
        print(jsond)

    with open('data.txt', 'w') as outfile:
        json.dump(jsond, outfile)
    print(jsond)
    #print(json)
    # print(titles)
scrapeWikis()
