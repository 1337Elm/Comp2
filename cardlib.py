"""
Python library for a game of poker. Consists of Card-classes (NumberedCard, JackCard, QueenCard, KingCard and AceCard).
Aswell as a Enum Suit class, Hand class, StandardDeck class and finally a Pokerhand class.

Author: Benjamin Elm Jonsson 2022, benjamin.elmjonsson@gmail.com
"""
from abc import ABC,abstractmethod
from cgitb import handler
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
        self.cards.sort()

    def best_poker_hand(self,cards = []):
        if Straight_flush(cards):
            return Straight_flush(cards)
        elif FourKind(cards):
            return FourKind(cards)
        elif FullHouse(cards):
            return FullHouse(cards)
        elif Flush(cards):
            return Flush(cards)
        elif Straight(cards):
            return Straight(cards)
        elif ThreeKind(cards):
            return ThreeKind(cards)
        elif TwoPair(cards):
            return TwoPair(cards)
        elif Pair(cards):
            return Pair(cards)
        else:
            return HighCard(cards)


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


class PokerHand(ABC):
    @abstractmethod
    def __init__(self, cards = []):
        self.cards = cards

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def eigen_value(self):
        pass
    
    @abstractmethod
    def __lt__(self,other: object):
        pass


class Straight_flush(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []


        #Condition for Straight_flush. if true return true
    
    def get_value(self):
        return 9

    def eigen_value(self):
        self.hand.sort()
        return self.hand[-1].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False


class FourKind(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

        counter = 0
        for i in cards:
            self.hand.append(i)
            for j in range(i+1,len(cards)):
                if i.get_value() == cards[j].get_value():
                    counter += 1
                    self.hand.append(cards[j])
            if counter != 4:
                counter = 0
                self.hand.clear()
        
        if counter == 4:
            return True
        else:
            return False

    def get_value(self):
        return 8

    def eigen_value(self):
        return self.hand[0].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False     


class FullHouse(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

        counterTripple = 0
        counterPair = 0
        for i in cards:
            self.hand.append(i)
            for j in range(i+1,len(cards)):
                if i.get_value() == cards[j].get_value():
                    counterTripple +=1
                    self.hand.append(cards[j])
            if counterTripple == 3:
                for i in self.hand:
                    cards.pop(i)
        
                for i in cards:
                    for j in range(i+1,len(cards)):
                        if i.get_value() == cards[j].get_value():
                            counterPair += 1
                    
                if counterPair == 1:
                    return True
            else:
                counterTripple = 0
                self.hand.clear()

    def get_value(self):
        return 7

    def eigen_value(self):
        return self.hand[0].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False  


class Flush(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

        #Condition for Flush return true, define hand for eigen_value()

    def get_value(self):
        return 6

    def eigen_value(self):
        self.hand.sort()
        return self.hand[-1].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False


class Straight(PokerHand):
    def __init__(self,cards =[]):
        self.cards = cards
        self.hand = []

        counter = 0
        for i in cards:
            self.hand.append(i)
            for j in range(i+1,len(cards)):
                if i.suit == cards[j].suit:
                    counter += 1
                    self.hand.append(cards[j])
            if counter == 5:
                return True
            else:
                counter = 0
                self.hand.clear()
        
        return False

    def get_value(self):
        return 5

    def eigen_value(self):
        return self.hand[0].suit.value

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False


class ThreeKind(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

        counter = 0
        for i in cards:
            self.hand.append(i)
            for j in range(i+1,len(cards)):
                if i.get_value() == cards[j].get_value():
                    counter += 1
                    self.hand.append(cards[j])
                    break        
            if counter == 3:
                return True
            else:
                counter = 0
                self.hand.clear()
        
        return False

    def get_value(self):
        return 4

    def eigen_value(self):
        return self.hand[0].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False


class TwoPair(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

        pairs = 0
        for i in cards:
            self.hand.append(i)
            for j in range(i+1,len(cards)):
                if i.get_value()==cards[j].get_value():
                    pairs += 1
                    self.hand.append(cards[j])
                else:
                    self.hand.pop(i)
        
        if pairs == 2:
            return True
        else:
            pairs = 0
            self.hand.clear()
        
        return False

    def get_value(self):
        return 3

    def eigen_value(self):
        self.hand.sort()
        return self.hand[-1].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False


class Pair(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

        for i in cards:
            self.hand.append(i)
            for j in range(i+1,len(cards)):
                if i.get_value()==cards[j].get_value():
                    self.hand.append(cards[j])
                    return True
            self.hand.clear()
        return False

    def get_value(self):
        return 2

    def eigen_value(self):
        return self.hand[0].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False


class HighCard(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards

        cards.sort()
    
    def get_value(self):
        return 1

    def eigen_value(self,cards):
        return cards[-1].get_value

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            else:
                return False
        else:
            return False