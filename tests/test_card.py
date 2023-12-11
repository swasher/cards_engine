"""
TESTING CARD CLASS
"""
from classes import Card, Rank, Suit


def test_card_create():
    card = Card(Rank.ACE, Suit.DIAMONDS)
    assert type(card) is Card


def test_card_str_method():
    card = Card(Rank.TWO, Suit.SPADES)
    assert str(card) == "2♠"


def test_card_repr_method():
    card = Card(Rank.THREE, Suit.HEARTS)
    assert repr(card) == "3♡"
