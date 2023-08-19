from random import choice


class Card:
    """A model of a Tarot card."""

    def __init__(self, name, upright, reversed):
        """
        Initialize name, upright and reversed keywords.
        """
        self.name = name
        self.upright = upright
        self.reversed = reversed

    def reading(self):
        """
        Function to print out a reading using card info.
        """
        print(f'\tCard name: {self.name}')
        state = choice([True, False])
        if state:
            print(f'\tUpright: {self.upright.title()}')
        else:
            print(f'\tReversed: {self.reversed.title()}')
