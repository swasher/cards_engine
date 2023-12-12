"""
TESTING HAND CLASS
"""
import pytest
from classes import Suit, Rank, Card, Hand
from classes import SPADES, D_7, D_A, C10


def test_init_1():
    hand = Hand(D_A)
    assert type(hand) is Hand
    assert type(hand.cards) is set


def test_init_2():
    hand = Hand(SPADES)
    assert type(hand) is Hand
    assert type(hand.cards) is set


def test_init_3():
    hand = Hand(SPADES, D_7, D_A)
    assert type(hand) is Hand
    assert type(hand.cards) is set


def test_add_card_method_1():
    hand = Hand()
    card = Card(Rank.TWO, Suit.SPADES)
    hand.add_card(card)
    assert card in hand.cards
    assert type(hand.cards) is set


def test_add_card_method_2():
    hand = Hand()
    cards = SPADES
    with pytest.raises(TypeError):
        hand.add_card(cards)


def test_add_card_method_3():
    hand = Hand()
    cards = SPADES, D_7, D_A
    with pytest.raises(TypeError):
        hand.add_card(cards)


def test_discard_to_pile():
    hand = Hand()
    pile = Hand()

    card1 = D_7
    card2 = D_A
    card3 = C10

    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)

    hand.discard_to_pile()

    assert card1 not in hand.cards
    assert card2 not in hand.cards
    assert card3 not in hand.cards

    assert card1 in pile.cards
    assert card2 in pile.cards
    assert card3 in pile.cards