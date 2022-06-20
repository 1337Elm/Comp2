from abc import ABC,abstractmethod
from enum import Enum
import random

class PlayingCard(ABC):
    @abstractmethod
    def __init__(self,suit):
        pass

    @abstractmethod
    def get_value():
        pass

class NumberedCard(PlayingCard):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self):
        return self.value

    
class JackCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value():
        return 11


class QueenCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value():
        return 12


class KingCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value():
        return 13


class AceCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value():
        return 14


class Suit(Enum):
    Hearts = 0
    Spades = 1
    Clubs = 2
    Diamonds = 3


class Hand(list):
    def __init__(self,cards = []):
        self.cards = cards
        
    def add_card(self,CardsToAdd = []):
        for i in CardsToAdd:
            self.append(i)

    def drop_cards(self,indList):
        for i in range(indList):
            self.pop(i)

    def sort(self):
        self.sort()

    def best_poker_hand(self,cards = []):
        pass


class StandardDeck(list):
    def __init__(self):
        for i in range(13):
            for j in range(4):
                self.append(NumberedCard(i,j))

        for i in range(4):
            self.append(JackCard(i))
            self.append(QueenCard(i))
            self.append(KingCard(i))
            self.append(AceCard(i))
        
    def shuffle(self):
        random.shuffle(self)

    def draw(self,loc,num):
        pass 


class PokerHand(list):
    def __init__(self):
        pass


deck = StandardDeck()

for i in deck:
    print(i)