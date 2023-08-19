import random


def three_spread(deck):
    """
    Function to do three-card spread
    """
    situtation = input('Which spread would you like to receive?\n'
                       '1. Past, Present, Future\n'
                       '2. Situation, Obsticle, Advice\n'
                       '3. Mind, Body, Spirit\n')
    type = [
            ['Past', 'Present', 'Future'],
            ['Situation', 'Obsticle', 'Advice'],
            ['Mind', 'Body', 'Spirit']
        ]
    try:
        situtation = int(situtation)
    except ValueError:
        print('Invalid input')
    else:
        situtation = situtation-1
        for i in range(0, 3):
            card = random.choice(deck)
            print(f'{type[situtation][i]}\n')
            card.reading()
