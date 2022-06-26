"""
Python library for a game of poker. Consists of Card-classes (NumberedCard, JackCard, QueenCard, KingCard and AceCard).
Aswell as a Enum Suit class, Hand class, StandardDeck class and finally a Pokerhand class.

Author: Benjamin Elm Jonsson 2022, benjamin.elmjonsson@gmail.com
"""
from abc import ABC,abstractmethod
from enum import Enum
import random

class PlayingCard(ABC):
    @abstractmethod
    def __init__(self,suit):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def __eq__(self, other: object):
        pass

    @abstractmethod
    def __lt__(self, other: object):
        pass


class PokerHand(ABC):
    @abstractmethod
    def __init__(self,cards = []):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def __lt__(self,other: object):
        pass


class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        self.value = value 
        self.suit = suit

    def get_value(self):
        return self.value
    
    def __eq__(self, other: object):
        if self.get_value() == other.get_value():
            if self.suit == other.suit:
                return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.suit.value < other.suit.value:
                return True
        else:
            return False

    
class JackCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 11
    
    def __eq__(self, other: object):
        if self.get_value() == other.get_value():
            if self.suit == other.suit:
                return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.suit.value < other.suit.value:
                return True
        else:
            return False


class QueenCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 12

    def __eq__(self, other: object):
        if self.get_value() == other.get_value():
            if self.suit == other.suit:
                return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.suit.value < other.suit.value:
                return True
        else:
            return False


class KingCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 13

    def __eq__(self, other: object):
        if self.get_value() == other.get_value():
            if self.suit == other.suit:
                return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.suit.value < other.suit.value:
                return True
        else:
            return False


class AceCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 14

    def __eq__(self, other: object):
        if self.get_value() == other.get_value():
            if self.suit == other.suit:
                return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.suit.value < other.suit.value:
                return True
        else:
            return False


class Suit(Enum):
    Hearts = 0
    Spades = 1
    Clubs = 2
    Diamonds = 3


class Hand(list):
    def __init__(self,cards = []):
        self.cards = cards
        
    def add_card(self,CardsToAdd):
        self.append(CardsToAdd)

    def drop_cards(self,indList):
        for i in indList:
            self.pop(i)

    def sort(self):
        self.sort()

    def best_poker_hand(self,cards = []):
       pass


class StandardDeck(list):
    def __init__(self):
        for i in range(2,11):
            for j in Suit:
                self.append(NumberedCard(i,j))

        for i in Suit:
            self.append(JackCard(i))
            self.append(QueenCard(i))
            self.append(KingCard(i))
            self.append(AceCard(i))

        self.sort()
  
    def shuffle(self):
        random.shuffle(self)

    def draw(self):
        return(self.pop(0))


class HighCard(PokerHand):
    def __init__(self, cards=[]):
        self.cards = cards

    def get_value(self):
        return 1

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False


class Pair(PokerHand):
    def __init__(self, cards=[]):
        self.cards = cards

    def get_value(self):
        return 2

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False


class TwoPair(PokerHand):
    def __init__(self, cards=[]):
        self.cards = cards

    def get_value():
        return 3

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False
    

class ThreeOfaKind(PokerHand):
    def __init__(self, cards=[]):
        self.cards = cards

    def get_value():
        return 4

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False


class Straight(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards

    def get_value(self):
        return 5

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False


class Flush(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards

    def get_value(self):
        return 6

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False


class FullHouse(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards

    def get_value(self):
        return 7

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False


class FourOfaKind(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards

    def get_value(self):
        return 8

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False


class StraightFlush(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards

    def get_value(self):
        return 9

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        else:
            return False