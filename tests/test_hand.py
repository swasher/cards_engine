"""
TESTING HAND CLASS
"""
import pytest
from classes import *

def test_hand_init_1():
    hand = Hand(D_A)
    assert type(hand) is Hand
    assert type(hand.cards) is set
    assert hand.cards == {D_A}


def test_hand_init_2():
    hand = Hand(SPADES)
    assert type(hand) is Hand
    assert type(hand.cards) is set
    assert hand.cards == {S_7, S_8, S_9, S10, S_J, S_Q, S_K, S_A}


def test_hand_init_3():
    hand = Hand(SPADES, D_7, D_A)
    assert type(hand) is Hand
    assert type(hand.cards) is set
    assert hand.cards == {S_7, S_8, S_9, S10, S_J, S_Q, S_K, S_A, D_7, D_A}

def test_hand_add_method_1():
    hand = Hand()
    card = Card(Rank.TWO, Suit.SPADES)
    hand.add_card(card)
    assert card in hand.cards
    assert type(hand.cards) is set
    assert hand.cards == {card}


def test_hand_add_method_2():
    hand = Hand()
    cards = SPADES
    with pytest.raises(TypeError):
        hand.add_card(cards)


def test_hand_add_card_method_3():
    hand = Hand()
    cards = SPADES, D_7, D_A
    with pytest.raises(TypeError):
        hand.add_card(cards)


def test_hand_remove_card_method():
    hand = Hand(DIAMONDS)
    card1 = Card(Rank.EIGHT, Suit.DIAMONDS)
    card2 = Card(Rank.KING, Suit.DIAMONDS)
    hand.remove_card(card1)
    hand.remove_card(card2)
    assert hand.cards == {D_7, D_9, D10, D_J, D_Q, D_A}