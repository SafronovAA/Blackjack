from tempfile import gettempdir
from card import Card


class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.points = 0
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    @property
    def add_points(self):
        return self.points

    @add_points.setter
    def add_points(self, points: int):
        self.points += int(points)

    def show_cards(self):
        return self.cards

    