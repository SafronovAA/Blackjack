from itertools import product
from random import shuffle

from const import SUITS, RANKS
from card import Card


class Deck():
    def __init__(self) -> None:
        self.cards = self.create_deck()
        shuffle(self.cards)

    def create_deck(self):
        cards = []
        points = 0
        for suit, rank in product(SUITS, RANKS):
            if rank == 'валет':
                    points = 2
            elif rank == 'дама':
                    points = 3
            elif rank == 'король':
                    points = 4
            elif rank == 'туз':
                    points = 10
            else:
                point= int(rank)
            cards.append(Card(suit=suit, rank=rank, points=points))
        return cards
    
    def pop_card(self):
        return self.cards.pop()