from tkinter import Y
from unicodedata import name
from game import Game


if __name__ == '__main__':
    start_game = True
    while start_game:
        game = Game()
        game.start_game()
        start_game = game.end_game()