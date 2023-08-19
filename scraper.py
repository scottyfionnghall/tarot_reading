import requests
from pathlib import Path
from bs4 import BeautifulSoup
import json


def scrape():
    """
    Scrapes cards from Labyrinthos.co, takes their name and keywords
    and creates a json file
    """

    URL = "https://labyrinthos.co/blogs/tarot-card-meanings-list"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    cards = soup.find_all("div", class_="card")
    keywords = soup.find_all("div", class_="keywords")
    card_names = []
    card_meanings = []
    tarot = []

    for card in cards:
        title = card.find("h3")
        title = str(title.get_text())[:-9]
        card_names.append(title)

    for card_keywords in keywords:
        keywords = card_keywords.find('p')
        keywords = str(keywords.get_text())
        keywords = keywords.split('\n')
        upright = keywords[2]
        reversed = keywords[-3].strip('      ')
        card_meanings.append([upright, reversed])

    for i in range(len(card_names)):
        name = card_names[i]
        upright = card_meanings[i][0][8:]
        upright = ''.join(upright.lstrip())
        reversed = card_meanings[i][1][9:]
        reversed = ''.join(reversed.lstrip())
        tarot.append({
            'name': name,
            'upright': upright,
            'reversed': reversed
        })
    file = Path('tarot.json')
    tarot = json.dumps(tarot)
    file.write_text(tarot)


scrape()
