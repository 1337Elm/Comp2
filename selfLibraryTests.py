from unicodedata import name
from cardlib import *
import test_cardlib as tcard
import pytest


def Cardstest():
    if tcard.test_cards() != False:
        print("Numbered and KingCard tests passed")


    if tcard.test_deck() != False:
        print("Standardeck test passed")

    
    if tcard.test_hand() != False:
        print("Hand tests passed")

    if tcard.test_pokerhands() != False:
        print("Best Pokerhand method test passed and Highcard, Pair and Fullhouse classes test passed")



def main():
    Cardstest()


if __name__ == '__main__':
    main()