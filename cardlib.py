from abc import ABC,abstractmethod
from enum import Enum
import random

class PlayingCard(ABC):
    @abstractmethod
    def __init__(self,suit):
        self.suit = suit

    @abstractmethod
    def get_value():
        pass

class NumberedCard(PlayingCard):
    def __init__(self, suit, value):
        super().__init__(self,suit)
        self.value = value

    def get_value(self):
        return self.value

    
class JackCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(self,suit)

    def get_value():
        pass


class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value():
        pass


class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value():
        pass


class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(suit)

    def get_value():
        pass


class Suit(Enum):
    Hearts = 0
    Spades = 1
    Clubs = 2
    Diamonds = 3


class Hand(list):
    def __init__(self):
        super().__init__(self)

    def add_card(self,cards = []):
        for i in cards:
            self.append(i)

    def drop_cards(self,indList):
        for i in range(indList):
            self.pop(i)

    def sort(self):
        self.sort()

    def best_poker_hand(self,cards = []):
        pass

    def get_value():
        pass


class StandardDeck(list):
    def __init__(self):
        super().__init__()

    def shuffle(self):
        random.shuffle(self)

    def draw(self,loc,num):
        pass 


class PokerHand(list):
    def __init__(self):
        pass