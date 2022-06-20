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


class Hand(object):
    def __init__(self):
        pass

    def add_card():
        pass

    def drop_cards():
        pass

    def sort():
        pass

    def best_poker_hand(self,cards = []):
        pass


class StandardDeck(object):
    def __init__(self):
        pass


class PokerHand(object):
    def __init__(self):
        pass
