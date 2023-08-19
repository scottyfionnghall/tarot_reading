import json
from scraper import scrape
from pathlib import Path
from card import Card
import spreads


# scrape cards into tarot.json file
# if file exists, skip this step
deck_file = Path('tarot.json')
if deck_file.exists():
    print('hey')
    pass
else:
    scrape()

cards = deck_file.read_text()
cards = json.loads(cards)
deck = []
for card in cards:
    # create Card objects for each card
    name = card['name']
    upright = card['upright']
    reversed = card['reversed']
    deck.append(Card(name, upright, reversed))

while True:
    user_input = input("Do you want to get a three card spread? Y\\N \n")
    if user_input.lower() == 'n':
        break
    elif user_input.lower() == 'y':
        spreads.three_spread(deck)
    else:
        continue
