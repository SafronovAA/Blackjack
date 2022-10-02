from player import Player
from deck import Deck

class Game():
    def __init__(self) -> None:
        self.player = self.add_player()
        self.deck = Deck()
        self.dealer = self.add_dealer()

    def add_player(self, player: str) -> Player:
        player = Player(name = player)
        return player

    def add_dealer(self):
        dealer = Player(name = "Дилер")
        return dealer
    
    def get_card(self):
        return self.deck.pop_card()

    def ask_question(text: str):
        answer = input(text)
        if answer == "y":
            return True
        else:
            return False
    
    def start_game(self):
        answer = self.ask_question("Вы хотите начать игру?")
        if answer:
            self.player.add_card(self.deck.pop_card())
            


