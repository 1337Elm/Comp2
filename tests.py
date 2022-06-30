import test_cardlib as test
import cardlib

def main():
    if test.test_cards():
        print("Testing of the cards passed")
    
    if test.test_deck():
        print("Testing of the deck passed")

    if test.test_hand():
        print("Testing of the hand passed")

    if test.test_pokerhands():
        print("Testing of the pokerhands passed")












if __name__ == '__main__':
    main()