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

    @abstractmethod
    def __gt__(self, other: object):
        pass


class NumberedCard(PlayingCard):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self):
        return self.value
    
    def __eq__(self, other: object):
        if self.get_value()==other.get_value():
            return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other: object):
        if self.get_value()>other.get_value():
            return True
        else:
            return False
    
class JackCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 11
    
    def __eq__(self, other: object):
        if self.get_value()==other.get_value():
            return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other: object):
        if self.get_value()>other.get_value():
            return True
        else:
            return False


class QueenCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 12

    def __eq__(self, other: object):
        if self.get_value()==other.get_value():
            return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other: object):
        if self.get_value()>other.get_value():
            return True
        else:
            return False


class KingCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 13

    def __eq__(self, other: object):
        if self.get_value()==other.get_value():
            return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other: object):
        if self.get_value()>other.get_value():
            return True
        else:
            return False


class AceCard(PlayingCard):
    def __init__(self, suit):
        self.suit = suit

    def get_value(self):
        return 14

    def __eq__(self, other: object):
        if self.get_value()==other.get_value():
            return True
        else:
            return False
    
    def __lt__(self,other: object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other: object):
        if self.get_value()>other.get_value():
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
        for i in range(2,11):
            for j in Suit:
                self.append(NumberedCard(j,i))

        for i in Suit:
            self.append(JackCard(i))
            self.append(QueenCard(i))
            self.append(KingCard(i))
            self.append(AceCard(i))

        self.sort()
  
    def shuffle(self):
        random.shuffle(self)

    def draw(self):
        self.pop(0)


class PokerHand(list):
    def __init__(self, cards = []):
        self.cards = cards

    def straight_flush(self,cards =  []):
        pass

    def fourKind(self,cards=[]):
        pass

    def full_house(self,cards = []):
        pass

    def flush(self,cards = []):
        pass

    def straight(self,cards = []):
        counter = 0
        for i in cards:
            for j in range(i+1,len(cards)):
                if i.suit == cards[j].suit:
                    counter += 1
            if counter == 5:
                return True
            else:
                counter = 0
        
        return False

    def threeKind(self,cards = []):
        counter = 0
        for i in cards:
            for j in range(i+1,len(cards)):
                if i.get_value() == cards[j].get_value():
                    counter += 1
        
        if counter == 3:
            return True
        else:
            return False

    def twoPair(self,cards = []):
        pairs = 0
        for i in cards:
            for j in range(i+1,len(cards)):
                if i.get_value()==cards[j].get_value():
                    pairs += 1
                    break
                break
        
        if pairs == 2:
            return True
        else:
            return False

    def Pair(self,cards = []):
        for i in cards:
            for j in range(i+1,len(cards)):
                if i.get_value()==cards[j].get_value():
                    return True
        
        return False
    