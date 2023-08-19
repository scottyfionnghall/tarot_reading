import random


def three_spread(deck):
    situtation = input('Which spread would you like to receive?\n'
                       '1. Past, Present, Future\n'
                       '2. Situation, Obsticle, Advice\n'
                       '3. Mind, Body, Spirit\n')
    try:
        situtation = int(situtation)
    except ValueError:
        print('Invalid input')
    else:
        situtation = situtation-1
        type = [
            ['Past', 'Present', 'Future'],
            ['Situation', 'Obsticle', 'Advice'],
            ['Mind', 'Body', 'Spirit']
        ]
        for i in range(0, 3):
            card = random.choice(deck)
            print(f'{type[situtation][i]}\n')
            card.reading()
