from xmlrpc.client import Boolean
from player import Player
from deck import Deck


class Game():
    def __init__(self) -> None:
        self.player = Player(name = "Artyom")
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

    def ask_question(self,text: str):
        answer = input(text)
        if answer == "y":
            return True
        else:
            return False
    
    def add_card_to_player(self, answer: Boolean) -> None:
        if answer:
            card = self.get_card()
            self.player.add_card(card)
            self.player.add_points = card.points

    def add_card_to_dealer(self) -> None:
        card = self.get_card()
        self.dealer.add_card(card)
        self.dealer.add_points = card.points

    def start_game(self) -> None:
        answer = self.ask_question("Вы хотите начать игру?")
        self.add_card_to_player(answer)
        self.add_card_to_player(answer)
        cards = self.player.show_cards()
        for card in cards:
            print(card)
        print(f"Всего очков: {self.player.add_points}\n")
        
        answer = self.ask_question("Вы хотите взять еще карту?")
        while True:
            if answer:
                self.add_card_to_player(answer)
                cards = self.player.show_cards()
                for card in cards:
                    print(card)
                print(f"Всего очков: {self.player.add_points}\n")
                
                answer = self.ask_question("Вы хотите взять еще карту?")
            else:
                break

        self.add_card_to_dealer()
        self.add_card_to_dealer()
        cards_dealer = self.dealer.show_cards()
        for card in cards_dealer:
            print(card)
        print("\n")
        print(f"Всего очков у {self.player.name}: {self.player.add_points}")
        

        while self.dealer.add_points < 17:
            self.add_card_to_dealer()
        print(f"Всего очков у дилера: {self.dealer.add_points}")

        if self.dealer.add_points == 21 & self.player.add_points < 21:
            print(f"Выйграл дилер")
        if self.player.add_points == 21 & self.dealer.add_points < 21:
            print(f"Выйграл игрок 2 {self.player.name}")
        if self.player.add_points > self.dealer.add_points and self.player.add_points <= 21:
            print(f"Выйграл игрок  1 {self.player.name}")
        if self.player.add_points < self.dealer.add_points and self.dealer.add_points <= 21:
            print(f"Выйграл дилер")
        
    def end_game(self):
        answer = self.ask_question("Вы хотите сыграть еще игру?")
        return answer