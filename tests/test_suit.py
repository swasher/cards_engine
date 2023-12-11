"""
TESTING SUIT CLASS
"""
from classes import Suit


def test_suit_str_method():
    assert str(Suit.SPADES) == "♠"
    assert str(Suit.CLUBS) == "♣"
    assert str(Suit.DIAMONDS) == "♢"
    assert str(Suit.HEARTS) == "♡"


def test_create_suit():
    suit = Suit.SPADES
    assert type(suit) is Suit