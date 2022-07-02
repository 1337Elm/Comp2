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
    
    @abstractmethod
    def __repr__(self):
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
    
    def __repr__(self):
        if self.suit.value == 0:
            return f"{self.value} of Hearts"
        elif self.suit.value == 1:
            return f"{self.value} of Spades"
        elif self.suit.value == 2:
            return f"{self.value} of Clubs"
        elif self.suit.value == 3:
            return f"{self.value} of Diamonds"
        

    
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
    
    def __repr__(self):
        if self.suit.value == 0:
            return "Jack of Hearts"
        elif self.suit.value == 1:
            return "Jack of Spades"
        elif self.suit.value == 2:
            return "Jack of Clubs"
        elif self.suit.value == 3:
            return "Jack of Diamonds"


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

    def __repr__(self):
        if self.suit.value == 0:
            return "Queen of Hearts"
        elif self.suit.value == 1:
            return "Queen of Spades"
        elif self.suit.value == 2:
            return "Queen of Clubs"
        elif self.suit.value == 3:
            return "Queen of Diamonds"


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
    
    def __repr__(self):
        if self.suit.value == 0:
            return "King of Hearts"
        elif self.suit.value == 1:
            return "King of Spades"
        elif self.suit.value == 2:
            return "King of Clubs"
        elif self.suit.value == 3:
            return "King of Diamonds"


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

    def __repr__(self):
        if self.suit.value == 0:
            return "Ace of Hearts"
        elif self.suit.value == 1:
            return "Ace of Spades"
        elif self.suit.value == 2:
            return "Ace of Clubs"
        elif self.suit.value == 3:
            return "Ace of Diamonds"

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
        list = []
        for i in self.cards:
            list.append(i)
        for i in cards:
            list.append(i)

        Sf = Straight_flush(list)
        Fk = FourKind(list)
        Fh = FullHouse(list)
        Fl = Flush(list)
        St = Straight(list)
        Tk = ThreeKind(list)
        Tp = TwoPair(list)
        Pa = Pair(list)

        if Sf.is_True() != False:
            SF = Straight_flush(list)
            return SF

        elif Fk.is_True() != False:
            FK = FourKind(list)
            return FK
        
        elif Fh.is_True() != False:
            FH = FullHouse(list)
            return FH
        
        elif Fl.is_True() != False:
            FL = Flush(list)
            return FL
        
        elif St.is_True() != False:
            ST = Straight(list)
            return ST
        
        elif Tk.is_True() != False:
            TK = ThreeKind(list)
            return TK
        
        elif Tp.is_True() != False:
            TP = TwoPair(list)
            return TP
        
        elif Pa.is_True() != False:
            PA = Pair(list)
            return PA
        
        else:
            return HighCard(list)
    
    def __repr__(self):
        return f"Hand containing {self.cards}"


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

    def __repr__(self):
        return "Deck of cards"


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
    
    @abstractmethod
    def __repr__(self):
        pass


class Straight_flush(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

    def is_True(self):  
        self.cards.sort()
        counter = 1
        for i in range(len(self.cards)-1):
            self.hand.append(self.cards[i])
            for j in range(i,len(self.cards)-1):
                if self.cards[j].get_value() + 1 == self.cards[j+1].get_value():
                    counter += 1
                    self.hand.append(self.cards[j+1])
            if counter == 5:
                counter = 1
                for i in range(len(self.cards)):
                    self.hand.append(self.cards[i])
                    for j in range(i+1,len(self.cards)):
                        if self.cards[i].suit == self.cards[j].suit:
                            counter += 1
                            self.hand.append(self.cards[j])
                    if counter == 5:
                        return self.hand
                    else:
                        counter = 1
                        self.hand.clear()
            else:
                counter = 1
                self.hand.clear()
        
        return False    
  
    def get_value(self):
        return 9

    def eigen_value(self):
        self.is_True()
        self.hand.sort()
        return self.hand[-1].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            elif self.eigen_value() == other.eigen_value():
                self.is_True()
                self.hand.sort()

                other.is_True()
                other.hand.sort()
                if self.hand[-1].suit.value > other.hand[-1].suit.value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f"Straight flush, {self.is_True()}"


class FourKind(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

    def is_True(self):
        for i in range(len(self.cards)):
            self.hand.append(self.cards[i])
            for j in range(i+1,len(self.cards)):
                if self.hand[0].get_value() == self.cards[j].get_value():
                    self.hand.append(self.cards[j])
                    if len(self.hand) == 4:
                        return self.hand
            if len(self.hand) != 4:
                self.hand.clear()
        
        return False       

    def get_value(self):
        return 8

    def eigen_value(self):
        self.is_True()
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

    def __repr__(self):
        return f"Four of a Kind, {self.is_True()}"   


class FullHouse(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []
    
    def is_True(self):
        self.cards.sort()
        self.cards.reverse()
        for i in range(len(self.cards)-1):
            self.hand.append(self.cards[i])
            for j in range(i+1,len(self.cards)):
                if self.hand[0].get_value() == self.cards[j].get_value():
                    self.hand.append(self.cards[j])
            if len(self.hand) == 3:
                for i in self.hand:
                    self.cards.remove(i)
        
                for i in range(len(self.cards)):
                    for j in range(i+1,len(self.cards)):
                        if self.cards[i].get_value() == self.cards[j].get_value():
                            return self.hand
            else:
                self.hand.clear()
        
        return False

    def get_value(self):
        return 7

    def eigen_value(self):
        self.is_True()
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

    def __repr__(self):
        return f"Full House, {self.is_True()}"   


class Flush(PokerHand):
    def __init__(self,cards =[]):
        self.cards = cards
        self.hand = []

    def is_True(self):
        counter = 1
        for i in range(len(self.cards)):
            self.hand.append(self.cards[i])
            for j in range(i+1,len(self.cards)):
                if self.cards[i].suit == self.cards[j].suit:
                    counter += 1
                    self.hand.append(self.cards[j])
            if counter == 5:
                return self.hand
            else:
                counter = 1
                self.hand.clear()
        
        return False

    def get_value(self):
        return 5

    def eigen_value(self):
        self.is_True()
        return self.hand[0].suit.value

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            elif self.eigen_value() == other.eigen_value():
                self.is_True()
                self.hand.sort()

                other.is_True()
                other.hand.sort()
                if self.hand[-1].suit.value > other.hand[-1].suit.value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __repr__(self):
        return f"Flush, {self.is_True()}"  


class Straight(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

    def is_True(self):
        self.cards.sort()
        counter = 1
        for i in range(len(self.cards)-1):
            self.hand.append(self.cards[i])
            for j in range(i,len(self.cards)-1):
                if self.cards[j].get_value() + 1 == self.cards[j+1].get_value():
                    counter += 1
                    self.hand.append(self.cards[j+1])
            if counter == 5:
                return self.hand
            else:
                counter = 1
                self.hand.clear()
        
        return False

    def get_value(self):
        return 6

    def eigen_value(self):
        self.is_True()
        return self.hand[-1].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            elif self.eigen_value() == other.eigen_value():
                self.is_True()
                self.hand.sort()

                other.is_True()
                other.hand.sort()
                if self.hand[-1].suit.value > other.hand[-1].suit.value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f"Straight, {self.is_True()}"  


class ThreeKind(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

    def is_True(self):
        for i in range(len(self.cards)):
            self.hand.append(self.cards[i])
            for j in range(i+1,len(self.cards)):
                if self.hand[0].get_value() == self.cards[j].get_value():
                    self.hand.append(self.cards[j])       
            if len(self.hand) == 3:
                return self.hand
            else:
                self.hand.clear()
        
        return False

    def get_value(self):
        return 4

    def eigen_value(self):
        self.is_True()
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

    def __repr__(self):
        return f"Three of a Kind, {self.is_True()}"  

class TwoPair(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []

    def is_True(self):
        self.cards.sort()
        self.cards.reverse()
        for i in range(len(self.cards)-1):
            self.hand.append(self.cards[i])
            for j in range(i+1,len(self.cards)):
                if self.cards[i].get_value() == self.cards[j].get_value():
                    self.hand.append(self.cards[j])
                    nextPair = []
                    for u in self.cards:
                        if u != self.hand[0]:
                            nextPair.append(u)

                    for i in range(len(nextPair)-1):
                        self.hand.append(nextPair[i])
                        for j in range(i+1,len(nextPair)):
                            if nextPair[i].get_value() == nextPair[j].get_value():
                                self.hand.append(nextPair[j])
                                return self.hand
                        self.hand.clear()
                    return False
            self.hand.clear()
        return False

    def get_value(self):
        return 3

    def eigen_value(self):
        self.is_True()
        return self.hand[0].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            elif self.eigen_value() == other.eigen_value():
                self.is_True()
                self.hand.sort()

                other.is_True()
                other.hand.sort()
                if self.hand[0].get_value() < other.hand[0].get_value():
                    return True
                elif self.hand[0].get_value() == other.hand[0].get_value():
                    if self.hand[-1].suit.value > other.hand[-1].suit.value:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    def __repr__(self):
        return f"Two Pairs, {self.is_True()}"  


class Pair(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        self.hand = []
        self.cards.sort()

    def is_True(self):
        self.cards.reverse()
        for i in range(len(self.cards)-1):
            self.hand.append(self.cards[i])
            for j in range(i+1,len(self.cards)):
                if self.cards[i].get_value() == self.cards[j].get_value():
                    self.hand.append(self.cards[j])
                    return self.hand  
            self.hand.clear()
                
        return False

    def get_value(self):
        return 2

    def eigen_value(self):
        self.is_True()
        return self.hand[0].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            elif self.eigen_value() == other.eigen_value():
                self.is_True()
                self.hand.sort()

                other.is_True()
                other.hand.sort()

                listself = []
                listother = []
                for i in range(len(self.cards)):
                    if self.cards[i] not in self.hand:
                        listself.append(self.cards[i])
                    if other.cards[i] not in other.hand:
                        listother.append(other.cards[i])

                listself.sort()
                listother.sort()
                for i in range(len(listself)):
                    if listself[i] < listother[i]:
                        return True
                    elif listself[i] == listother[i]:
                        if listself[i].suit.value > listother[i].suit.value:
                            return True
                return False
            else:    
                return False
        else:
            return False

    def __repr__(self):
        return f"Pair, {self.is_True()}"  


class HighCard(PokerHand):
    def __init__(self,cards = []):
        self.cards = cards
        cards.sort()
    
    def get_value(self):
        return 1

    def eigen_value(self):
        return self.cards[-1].get_value()

    def __lt__(self,other: object):
        if self.get_value() < other.get_value():
            return True
        elif self.get_value() == other.get_value():
            if self.eigen_value() < other.eigen_value():
                return True
            elif self.eigen_value() == other.eigen_value():
                if self.cards[-1].suit.value > other.cards[-1].suit.value:
                    return True
            else:
                return False
        else:
            return False
    def __repr__(self):
        return f"Highcard, {self.cards[-1]}"  