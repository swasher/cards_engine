OOP Classes for manage gaming cards and calculate preferance game probability
====================================

How it works
--------------------

Сначала нам нужно импортировать классы таким образом:
```python
from classes import *
```

Потому что в `classes.py` есть много предустановленных объектов. Эти объекты:

- отдельные карты (от 7 до туза, но легко можно добавить до двойки):

```python
>>> print(S_7, C_A)
7♠ A♣
```
- масти

```python
>>> print(SPADES)
(7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♠)

>>> print(DIAMONDS)
(7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, A♢)
```

- вся колода

```python
>>> print(FULL_DECK)
(7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♠, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♣, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, A♢, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♡)
```

- два пустые объекта - DECK и PILE. Это объекты типа Hand (рука), представляющие собой Колоду и Сброс (выкинутые из игры карты)

```python
>>> print(type(DECK))
<class 'classes.Hand'>
>>> print(type(PILE))
<class 'classes.Hand'>
```

Создаем новую колоду, содержащую нужный набор карт. В качестве параметров можно пердать:
- список карт (list[Сard]) - то есть список объектов Card, например, всю масть (константы SPADES, HEARTS, etc)
- одну карту (Card)
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
