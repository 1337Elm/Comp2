from abc import ABC,abstractmethod
import enum

class PlayingCard(ABC):
    def __init__(self,Suit):
        self.Suit = Suit
    
    def JackCard(Suit):
        pass

    def QueenCard(Suit):
        pass

    def KingCard(Suit):
        pass

    def AceCard(Suit):
        pass

    @abstractmethod
    def get_value():
        pass


class Suit(enum.Enum):
    Hearts = 1
    Spades = 2
    Clubs = 3
    Diamonds = 4
