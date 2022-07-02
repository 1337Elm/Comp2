from cardlib import *
import test_cardlib as tcard
from enum import Enum


def StandTest():
    if tcard.test_cards() != False:
        if tcard.test_deck() != False:   
            if tcard.test_hand() != False:
                if tcard.test_pokerhands() != False:
                    print("All standard tests passed")

#Testa JackCard, QueenCard,AceCard R
#Testa Straight flush R, straight R, flush R, fourkind R,twopair
#Testa jämföra olika typer av händer och 2 av samma

def OwnTests():
    jS = JackCard(Suit.Spades)
    qD = QueenCard(Suit.Diamonds)
    aH = AceCard(Suit.Hearts)

    assert isinstance(jS.suit,Enum)
    assert qD.get_value() == 12
    assert aH > qD

    h1 = Hand()
    h1.add_card(AceCard(Suit.Diamonds))
    h1.add_card(KingCard(Suit.Diamonds))

    h2 = Hand()
    h2.add_card(AceCard(Suit.Clubs))
    h2.add_card(KingCard(Suit.Diamonds))

    cl = [QueenCard(Suit.Diamonds),JackCard(Suit.Diamonds),NumberedCard(10,Suit.Diamonds),NumberedCard(5,Suit.Spades),NumberedCard(3,Suit.Clubs)]
    ph1 = h1.best_poker_hand(cl)
    ph2 = h2.best_poker_hand(cl)

    assert isinstance(ph1,Straight_flush)
    assert isinstance(ph2,Straight)
    assert ph2 < ph1

    h3 = Hand()
    h3.add_card(KingCard(Suit.Clubs))
    h3.add_card(KingCard(Suit.Diamonds))
    cl = [KingCard(Suit.Hearts),KingCard(Suit.Spades),NumberedCard(10,Suit.Clubs),AceCard(Suit.Clubs),AceCard(Suit.Diamonds)]

    ph3 = h3.best_poker_hand(cl)
    assert isinstance(ph3,FourKind)

    h4 = Hand()
    h4.add_card(QueenCard(Suit.Clubs))
    h4.add_card(QueenCard(Suit.Diamonds))
    cl = [KingCard(Suit.Hearts),KingCard(Suit.Spades),NumberedCard(10,Suit.Clubs),AceCard(Suit.Clubs),AceCard(Suit.Diamonds)]

    ph4 = h4.best_poker_hand(cl)
    assert isinstance(ph4,TwoPair)

    

def main():
    StandTest()
    OwnTests()


if __name__ == '__main__':
    main()