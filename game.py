from player import Player
from deck import Deck

class Game():
    def __init__(self) -> None:
        self.players = []
        self.deck = Deck()

    def add_player(self, player: str) -> Player:
        player = Player(name = player)
        self.players.append(player)
        return player
    
    def get_card(self):
        return self.deck.pop_card()

    