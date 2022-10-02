class Card():

    def __init__(self, suit: str, rank: str, points: int) -> None:
        self.suit = suit
        self.rank = rank
        self.points = points

    def __str__(self) -> str:
        return f"Карта: {self.suit} {self.rank} - {self.points} очка(-ов)"