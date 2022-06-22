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
    
    def __eq__(self, other: object):
        if self.get_value()==other.get_value():
            return True
        else:
            return False
    
    def __lt__(self,other:object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other:object):
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
    
    def __lt__(self,other:object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other:object):
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
    
    def __lt__(self,other:object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other:object):
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
    
    def __lt__(self,other:object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other:object):
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
    
    def __lt__(self,other:object):
        if self.get_value()<other.get_value():
            return True
        else:
            return False

    def __gt__(self,other:object):
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
    def __init__(self):
        pass

deck = StandardDeck()

for card in deck:
    print(f"{card.get_value()} of {card.suit}")