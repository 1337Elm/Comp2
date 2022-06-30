"""
Python library for a game of poker. Consists of Card-classes (NumberedCard, JackCard, QueenCard, KingCard and AceCard).
Aswell as a Enum Suit class, Hand class, StandardDeck class and finally a Pokerhand abstract class with subclasses for
all types of pokerhands available.

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
        self.cards = []
        if cards:
            self.cards.append(cards) 

    def add_card(self,CardsToAdd):
        self.cards.append(CardsToAdd)

    def drop_cards(self,indList):
        items = [] 
        for i in indList:
            items.append(self.cards[i])
        
        for i in items:
            self.cards.remove(i)

    def sort(self):
        self.cards.sort()

    def best_poker_hand(self,cards = []):
        for i in cards:
            self.cards.append(i)

        if Straight_flush(self.cards):
            return Straight_flush(self.cards)
        elif FourKind(self.cards):
            return FourKind(self.cards)
        elif FullHouse(self.cards):
            return FullHouse(self.cards)
        elif Flush(self.cards):
            return Flush(self.cards)
        elif Straight(self.cards):
            return Straight(self.cards)
        elif ThreeKind(self.cards):
            return ThreeKind(self.cards)
        elif TwoPair(self.cards):
            return TwoPair(self.cards)
        elif Pair(self.cards):
            return Pair(self.cards)
        else:
            return HighCard(self.cards)


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

        self.cards.sort()
        print(len(self.cards))
        counter = 0
        for i in cards:
            self.hand.append(i)
            for j in range(i,len(self.cards)-1):
                if cards[j].get_value() + 1 == cards[j+1].get_value():
                    counter += 1
                    self.hand.append(cards[j+1])
            if counter == 5:
                counter = 0
                for i in self.hand:
                    for j in range(i+1,len(cards)):
                        if i.suit == cards[j].suit:
                            counter += 1
                    if counter == 5:
                        return True
                    else:
                        counter = 0
            else:
                counter = 0
                self.hand.clear()
        
        return False
    
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

        cards.sort()
        counter = 0
        for i in cards:
            self.hand.append(i)
            for j in range(i,len(cards)-1):
                if cards[j].get_value() + 1 == cards[j+1].get_value():
                    counter += 1
                    self.hand.append(cards[j+1])
            if counter == 5:
                return True
            else:
                counter = 0
                self.hand.clear()
        
        return False

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