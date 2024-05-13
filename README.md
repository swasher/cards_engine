OOP Classes for manage gaming cards and calculate preferance game probability
====================================

Preface
--------------------

Full deck contains four suits (Spades, Clubs, Diamonds, Hearts - Пики, Трефы, Бубны, Черви).  
Every suit contain 13 Rank (from 2 to Ace).  
Suits can be ordered.  
Rank can be ordered (i.e. Ace>King and 10<Queen).   

Cards
-------------------

Any card can be constructed by following maner:

```pycon
>>> from classes import Rank, Suit, Card
>>> card = Card(Rank.ACE, Suit.DIAMONDS)
>>> card
A♢
>>> card = Card(Rank.SEVEN, Suit.CLUBS)
>>> card
7♣
```

Each card has an `owner` - this is can be Player, Deck, or Pile.

Suits
-------------------------------

There is predefined suits as `list` or as `dictionary`:

As list:

```pycon
>>> from classes import HEARTS
>>> HEARTS
[2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♡]
```

And as `dictionary`:

```pycon
>>> from classes import S, C, D, H
>>> S[5]
5♠
>>> C['A']
A♣
```

Keys are `int` for 2-10 and `str` for J, Q, K, A.

Dictionary convenient for access individual cards, and list for slicing:

```pycon
>>> CLUBS[9:12]
[J♣, Q♣, K♣]
```


Table
-----------------------

Table - this is objaect that incapsulate:

- all cards that's we can manipulate during session
- `DECK` object
- `PILE` object
- few `PLAYER` object
  
Usually we don't want to use all available (`2`-`A`) cards for table. So we can choose what cards using on game table, for example,
for Preferance game - from 7 to Ace:

```pycon
>>> card_set = SPADES[5:], CLUBS[5:], DIAMONDS[5:], HEARTS[5:]
>>> Table(card_set=card_set)

>>> Table.total()
32

>>> Table.all_cards()
{10♣, 10♢, 7♡, 9♠, 7♢, J♠, 7♣, Q♠, A♠, 8♠, J♡, 9♡, 9♣, 9♢, J♢, Q♡, Q♢, K♠, J♣, A♡, Q♣, A♣, A♢, 8♡, 8♢, 8♣, 10♠, K♡, K♣, K♢, 7♠, 10♡}
```

You can mix single cards and lists:

```pycon
>>> card_set = SPADES[5:], C[4], H[A]
```


Deck, Pile and Hands
-------------------------

There is two predefined objects - DECK and PILE. This objects inherited from AbstractPlayer class.

Usuale, early in the session, DECK will contains all cards of Table, and PILE will be empty.

During game session, cards from DECK deals to HANDs, then perform a few tricks, and after each trick moved to PILE.



Создаем новую колоду, содержащую нужный набор карт. В качестве параметров можно передать:
- список карт (`list[Сard]`) - то есть список объектов Card, например, всю масть (константы SPADES, HEARTS, etc)
- одну карту (`Card`)
- карты и списки можно комбинировать

```python
>>> DECK = Hand(SPADES)
# or
>>> DECK = Hand(SPADES, CLUBS)
# or
>>> DECK = Hand(S_7, S_Q, D10, H_A)
# or
>>> DECK = Hand(SPADES, S_Q, D10, H_A)

>>> PILE = Hand()
```

По аналогии мы может сделать колоду из двух мастей, или из конкретных карт. Сброс у нас пустой.

```pycon
>>> print(type(DECK))
<class 'classes.Hand'>
>>> print(type(PILE))
<class 'classes.Hand'>
```


Далее создаем три руки

```python
left_hand = Hand()
right_hand = Hand()
player = Hand()
```

И наконец, мы можем перемещать карты из одной руки в друку, или же между руками, колодой и сбросом:

```python

```
Например, мы хотим подсчитать, с какой вероятностью в преферансе будут расклады 4-0, 3-1 и 2-2.
