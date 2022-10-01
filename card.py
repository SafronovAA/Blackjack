class Card():

    def __init__(self, suit, rank, points) -> None:
        self.suit = suit
        self.rank = rank
        self.points = points

    def __str__(self) -> str:
        return f"Карта: {self.suit} {self.rank} - {self.points} очка(-ов)"