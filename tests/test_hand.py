"""
TESTING HAND CLASS
"""
from classes import Suit, Rank, Card, Hand
from classes import SPADES, D_7, D_A


def test_hand_init_1():
    hand = Hand(D_A)
    assert type(hand) is Hand
    assert type(hand.card_set) is set


def test_hand_init_2():
    hand = Hand(SPADES)
    assert type(hand) is Hand
    assert type(hand.card_set) is set


def test_hand_init_3():
    hand = Hand(SPADES, D_7, D_A)
    assert type(hand) is Hand
    assert type(hand.card_set) is set


def test_hand_add_method_1():
    hand = Hand()
    card = Card(Rank.TWO, Suit.SPADES)
    hand.add_card(card)
    assert card in hand.card_set
    assert type(hand.card_set) is set


def test_hand_add_method_2():
    hand = Hand()
    cards = SPADES
    hand.add_card(cards)
    assert cards in hand.cards


def test_hand_add_method_3():
    hand = Hand()
    cards = SPADES, D_7, D_A
    hand.add_card(cards)
    assert type(hand.cards) is set
