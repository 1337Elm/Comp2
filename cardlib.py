from abc import ABC,abstractmethod
from enum import Enum
import random

class PlayingCard(ABC):
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
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


class Suit(Enum):
    Hearts = 0
    Spades = 1
    Clubs = 2
    Diamonds = 3


class Hand(PlayingCard):
    def __init__(self):
        super().__init__(self)

    def add_card():
        pass

    def drop_cards(self,indList):
        for i in range(indList):
            self.pop(i)

    def sort():
        pass

    def best_poker_hand(self,cards = []):
        pass

    def get_value():
        pass


class StandardDeck(PlayingCard):
    def __init__(self):
        pass

    def shuffle(self):
        random.shuffle(self)

    def draw(self,loc,num):
        pass 

    def get_value():
        pass


class PokerHand(PlayingCard):
    def __init__(self):
        pass

    def get_value():
        pass
