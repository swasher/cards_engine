"""
TESTING RANK CLASS
"""
from classes import Rank

def test_rank_str_method():
    assert str(Rank.TWO) == "2"
    assert str(Rank.JACK) == "J"
    assert str(Rank.QUEEN) == "Q"
    assert str(Rank.KING) == "K"
    assert str(Rank.ACE) == "A"

def test_rank_gt_method():
    assert Rank.TEN > Rank.NINE
    assert not Rank.JACK > Rank.KING

def test_rank_lt_method():
    assert Rank.SIX < Rank.SEVEN
    assert not Rank.QUEEN < Rank.JACK
