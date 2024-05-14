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


Suits and Ranks
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
>>> from classes import J, Q, K, A
>>> S
[2♠️, 3♠️, 4♠️, 5♠️, 6♠️, 7♠️, 8♠️, 9♠️, 10♠️, J♠️, Q♠️, K♠️, A♠️]
>>> S[5]
5♠
>>> C['A']
A♣
>>> C[A]
A♣
```

Keys (ranks) are `int` for 2-10 and `str` for `J`, `Q`, `K`, `A`. Also, as you can see, there is predefined constants for `J`, `Q`, `K`, `A`,
so it can be possible use `C['A']` or `C[A]`.

Dictionary convenient for access individual cards, and list for slicing:

```pycon
>>> CLUBS[9:12]
[J♣, Q♣, K♣]
```

#### Suits Order

Suits order is: Spades Clubs Diamonds Hearts

#### Compare Cards

Any two cards can be compared taking into account their Suit and Ranks.
For example,Seven Club lesser than Diamond Ace, but greater than Spades Ace.

```pycon
>>> C[7] < D[A]
True
>>> C[7] < S[A]
False
```


Deck, Pile and Hands
-------------------------

First, we must define two instance for Deck (колода) and Pile (сброс)

```pycon
from classes import Deck, Pile

deck = Deck()
pile = Pile()
```

Then create three hands - for three players  (or other amount): 

```pycon
from classes import Player

left_hand = Player()
right_hand = Player()
my_hand = Player()
```


Table
-----------------------

Table - this object perform incapsulating for:

- all cards that's we can manipulate during session
- `DECK` object
- `PILE` object
- few `PLAYER` objects
  
Usually, we don't want to use all available cards (`2`-`A`) for the table. So we can choose what cards using on 
the game table, for example, for Preferance game - from 7 to Ace:

```pycon
>>> card_set = SPADES[5:], CLUBS[5:], DIAMONDS[5:], HEARTS[5:]
```

You can mix single cards and lists:

```pycon
>>> card_set = SPADES[5:], C[4], H[A]
```

Now we can initialize the Table:


```pycon

>>> table = Table(card_set, deck, pile, [left_hand, right_hand, my_hand])

>>> table.total
32

>>> table.cards
{10♣, 10♢, 7♡, 9♠, 7♢, J♠, 7♣, Q♠, A♠, 8♠, J♡, 9♡, 9♣, 9♢, J♢, Q♡, Q♢, K♠, J♣, A♡, Q♣, A♣, A♢, 8♡, 8♢, 8♣, 10♠, K♡, K♣, K♢, 7♠, 10♡}
```

Card's Moves
------------------------

Usually, early in the game session, DECK will contains all cards of Table, and PILE will be empty.

During game session, cards moves from the DECK to the HANDs, and then perform a few tricks, after that each trick moved to PILE.


Надо как-то унифицировать перемещение карт.
Наверное, нужно метод `draw` переименовать в `move` и переместить в `AbstractPlayer`.
Так же нужно придумать, как делать взятки.




Рассчеты
-------------------------

Например, мы хотим подсчитать, с какой вероятностью в преферансе будут расклады 4-0, 3-1, 2-2, голые король и туз
и другие типичные ситуации. Эти возможности уже реализованы в функции analyze(). Можно адаптировать эту
функцию для других игр и других ситуаций.

Предположим, игроку сдали 4 карты с марьяжем - 9, 10, Д, К

Проверим вероятности раскладов:

```pycon
"""
PREPARE
"""

card_set = SPADES[5:]  # анализирем только расклад одной масти

left_hand = Player()
right_hand = Player()
my_hand = Player()
deck = Deck()
pile = Pile()

table = Table(card_set=card_set, deck=deck, pile=pile, players=[left_hand, right_hand, my_hand])
table.reset()

"""
LET'S PLAY
"""

total_try = 10000  # кол-во раздач для анализа
stat.total_try = total_try

for i in range(total_try):
    deck.draw(player, (S[9], S[10], S[Q], S[K]))

    for card in deck.cards:
        random_opponent = random.choice([right_hand, left_hand])
        deck.draw(random_opponent, card)

    # print(f'Try {i}: RIGHT {right_hand} \t LEFT {left_hand}'.expandtabs(40), end="\r")  # вывод в консоль каждой раздачи
    analyze(right_hand, left_hand)
    table.reset()

stat.printing()
```

Результат:
```shell
Result:
Расклад 4-0:     12.38%
Расклад 3-1:     49.94%
Расклад 2-2:     37.68%
Голый туз:       12.84%
```

Проверим расклады, если на руках четвертый валет:

```pycon
deck.draw(player, (S[7], S[8], S[9], S[J]))
```

Мы опасаемся третьей дамы:
```pycon
deck.draw(my_hand, (S[7], S[J], S[K], S[A]))

Result:
Расклад 4-0:	 12.84%
Расклад 3-1:	 50.30%
Расклад 2-2:	 36.86%
Дама бланк или вторая дама:	 49.71%
Третья дама:	 50.29%
```