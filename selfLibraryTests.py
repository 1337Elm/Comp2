from cardlib import *
import test_cardlib as tcard
from enum import Enum


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
    cl = [NumberedCard(10,Suit.Clubs),AceCard(Suit.Clubs),AceCard(Suit.Diamonds)]

    ph4 = h4.best_poker_hand(cl)
    assert isinstance(ph4,TwoPair)

    h5 = Hand()
    h5.add_card(JackCard(Suit.Clubs))
    h5.add_card(JackCard(Suit.Diamonds))
    ph5 = h5.best_poker_hand(cl)
    assert ph5 < ph4

    

def main():
    list = [tcard.test_cards(),tcard.test_deck(),tcard.test_hand(),tcard.test_pokerhands()]
    for i in range(1,len(list)+2):
        print(f"Test passed ({i}/{len(list)+1})")
    


if __name__ == '__main__':
    main()