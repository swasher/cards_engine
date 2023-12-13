from __future__ import annotations
import random
from enum import Enum
from typing import Tuple


class Suit(Enum):
    SPADES = "♠"
    CLUBS = "♣"
    DIAMONDS = "♢"
    HEARTS = "♡"

    def __str__(self) -> str:
        return self.value
    @property
    def index(self) -> int:
        """
        0 for firsst element (SPADES),
        1 for second element (CLUBS),
        etc.
        :return:
        """
        return self.__sort_order_

    def __gt__(self, other: Suit) -> bool:
        """
        нужно придумать механиз, как сравнить self масть и other масть и вернуть True, если self больше чем other
        :param other:
        :return:
        """
        return self.index > other.index

    def __lt__(self, other: Suit) -> bool:
        return self.index < other.index


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __str__(self) -> str:
        match self:
            case Rank.JACK:
                return "J"
            case Rank.QUEEN:
                return "Q"
            case Rank.KING:
                return "K"
            case Rank.ACE:
                return "A"
            case _:
                return str(self.value)

    def __gt__(self, other: Rank) -> bool:
        return self.value > other.value

    def __lt__(self, other: Rank) -> bool:
        return self.value < other.value


class Card:
    rank: Rank
    suit: Suit
    owner: AbstractPlayer | None

    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit
        self.owner = None

    @property
    def index(self) -> int:
        """
        Служит для сортировки всех карт в колоде
        :return:
        """
        return self.suit.index * self.rank.value

    # def __hash__(self):
    #     return hash((self.rank, self.suit))

    def __lt__(self, other: Card):
        return self.index > other.index

    def __gt__(self, other: Card):
        return self.index < other.index

    def __eq__(self, other: Card):
        return self.index == other.index

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def __repr__(self):
        return f'{self.rank}{self.suit}'


"""
CARD_SET - это глобальная переменная типа set, в ней содержится все карты, участвующие в игре.
Этот список является неизменным, в отличие от DECK - колоды, из которой карты раздаются играющим. 
"""
__CARD_SET: set[Card] | None = None




class AbstractPlayer:
    """
    От этого класса будут наследоваться Колода (Deck), Сброс(Pile) и Игрок(Player).
    """

    @property
    def cards(self) -> set:
        """
        Возвращает все карты, которые на руках у данного игрока (или колоды, или сброса)
        :return:
        """
        filtered = {obj for obj in get_table() if obj.owner == self}
        return filtered

    def __str__(self):
        sorted_objects = sorted(self.cards, key=lambda x: x.index)
        s = ' '.join(map(str, sorted_objects))
        return s if s else '-'


class Deck(AbstractPlayer):
    """
    Особенность этого класса в том, что колода создается в самом начале, и из нее карты могут
    только сдаваться игрокам. Возвращать карты в колоду нельзя.
    Колода инициализируется набором CardSet
    """

    def __init__(self) -> None:
        """
        :param args:
        """
        for c in get_table():
            c.owner = self

    def draw(self, player: AbstractPlayer):
        """
        Сдать случайную карту из колоды игроку player
        :return:
        """
        card = random.choice(tuple(self.cards))
        card.owner = player


class Pile(AbstractPlayer):
    """
    Особенность этого класса в том, что из сброса нельзя доставать карты.
    Их туда можно только помезать.
    Сброс инициализируется пустым набором.
    """
    ...


class Player(AbstractPlayer):
    """
    Карты могут перемещаться от колоды (Deck) к игроку и от игрока в сброс (Pile)
    """

    def discard_to_pile(self):
        """
        Выкинуть все карты с руки в сброс
        :return:
        """
        for card in self.__cards:
            self.__away(card)
            PILE.add_card(card)

    def discard_to_deck(self):
        """
        Вернуть все карты с руки в колоду
        :return:
        """
        for card in self.__cards:
            self.__away(card)
            DECK.add_card(card)

    def get_suit(self, suit: Suit) -> list[Card]:
        """
        Возвращает все карты выбранной масти в руке.
        :return:
        """
        return list(filter(lambda n: n.suit == suit, self.cards))

    def get_high_card(self, suit: Suit) -> Card:
        """
        Возвращает старшую карту в масти
        :param suit:
        :return:
        """
        if self.__cards:
            return max(self.get_suit(suit))
        else:
            return None

    def move(self, hand: "Hand", cards: Tuple[Card, ...] | Card):
        """
        Переместить из набора self в набор Hand список карт Tuple[Card] или одну карту Card.
        :param cards:
        :param hand:
        :return:
        """
        def __do_move(c: Card) -> None:
            self.away(c)
            hand.add_card(c)

        if type(cards) is Card:
            # значит в функцию передали одну карту, а не кортеж
            card = cards
            __do_move(card)
        else:
            for card in cards:
                __do_move(card)


class Table:
    """
    Представляет собой Игровой Стол.
    Инкапсулирует Карты, Колоду и Сброс, и Игроков
    """
    def __init__(self, card_set: tuple[Card | list[Card]], deck: AbstractPlayer, pile: AbstractPlayer, players: list[AbstractPlayer]):

        s = set()
        for item in card_set:
            if type(item) is Card:
                s.add(item)
            else:
                # item is a list
                s.update(item)
        self.card_set = s

        self.deck = deck
        self.pile = pile
        self.players = players

    def set_card_set(self):
        # сейчас это происходит в init
        pass

    def get_card_set(self) -> set[Card]:
        """
        Возвращает все карты, принимающие участие в игре.
        :return:
        """
        return self.card_set




"""
PREDEFINED VARIABLE FOR EVERY CARD
"""

# global SPADES, S_7, S_8, S_9, S10, S_J, S_Q, S_K, S_A
S = {}
S[2] = Card(Rank(Rank.TWO), Suit(Suit.SPADES))
S[3] = Card(Rank(Rank.THREE), Suit(Suit.SPADES))
S[4] = Card(Rank(Rank.FOUR), Suit(Suit.SPADES))
S[5] = Card(Rank(Rank.FIVE), Suit(Suit.SPADES))
S[6] = Card(Rank(Rank.SIX), Suit(Suit.SPADES))
S[7] = Card(Rank(Rank.SEVEN), Suit(Suit.SPADES))
S[8] = Card(Rank(Rank.EIGHT), Suit(Suit.SPADES))
S[9] = Card(Rank(Rank.NINE), Suit(Suit.SPADES))
S[10] = Card(Rank(Rank.TEN), Suit(Suit.SPADES))
S['J'] = Card(Rank(Rank.JACK), Suit(Suit.SPADES))
S['Q'] = Card(Rank(Rank.QUEEN), Suit(Suit.SPADES))
S['K'] = Card(Rank(Rank.KING), Suit(Suit.SPADES))
S['A'] = Card(Rank(Rank.ACE), Suit(Suit.SPADES))
SPADES = [S[2], S[3], S[4], S[5], S[6], S[7], S[8], S[9], S[10], S['J'], S['Q'], S['K'], S['A']]


# global CLUBS, C_7, C_8, C_9, C10, C_J, C_Q, C_K, C_A
C = {}
C[2] = Card(Rank(Rank.TWO), Suit(Suit.CLUBS))
C[3] = Card(Rank(Rank.THREE), Suit(Suit.CLUBS))
C[4] = Card(Rank(Rank.FOUR), Suit(Suit.CLUBS))
C[5] = Card(Rank(Rank.FIVE), Suit(Suit.CLUBS))
C[6] = Card(Rank(Rank.SIX), Suit(Suit.CLUBS))
C[7] = Card(Rank(Rank.SEVEN), Suit(Suit.CLUBS))
C[8] = Card(Rank(Rank.EIGHT), Suit(Suit.CLUBS))
C[9] = Card(Rank(Rank.NINE), Suit(Suit.CLUBS))
C[10]= Card(Rank(Rank.TEN), Suit(Suit.CLUBS))
C['J'] = Card(Rank(Rank.JACK), Suit(Suit.CLUBS))
C['Q'] = Card(Rank(Rank.QUEEN), Suit(Suit.CLUBS))
C['K'] = Card(Rank(Rank.KING), Suit(Suit.CLUBS))
C['A'] = Card(Rank(Rank.ACE), Suit(Suit.CLUBS))
CLUBS = [C[2], C[3], C[4], C[5], C[6], C[7], C[8], C[9], C[10], C['J'], C['Q'], C['K'], C['A']]


# global DIAMONDS, D_7, D_8, D_9, D10, D_J, D_Q, D_K, D_A
D = {}
D[2] = Card(Rank(Rank.TWO), Suit(Suit.DIAMONDS))
D[3] = Card(Rank(Rank.THREE), Suit(Suit.DIAMONDS))
D[4] = Card(Rank(Rank.FOUR), Suit(Suit.DIAMONDS))
D[5] = Card(Rank(Rank.FIVE), Suit(Suit.DIAMONDS))
D[6] = Card(Rank(Rank.SIX), Suit(Suit.DIAMONDS))
D[7] = Card(Rank(Rank.SEVEN), Suit(Suit.DIAMONDS))
D[8] = Card(Rank(Rank.EIGHT), Suit(Suit.DIAMONDS))
D[9] = Card(Rank(Rank.NINE), Suit(Suit.DIAMONDS))
D[10] = Card(Rank(Rank.TEN), Suit(Suit.DIAMONDS))
D['J'] = Card(Rank(Rank.JACK), Suit(Suit.DIAMONDS))
D['Q'] = Card(Rank(Rank.QUEEN), Suit(Suit.DIAMONDS))
D['K'] = Card(Rank(Rank.KING), Suit(Suit.DIAMONDS))
D['A'] = Card(Rank(Rank.ACE), Suit(Suit.DIAMONDS))
DIAMONDS = [D[2], D[3], D[4], D[5], D[6], D[7], D[8], D[9], D[10], D['J'], D['Q'], D['K'], D['A']]


# HEARTS - ЧЕРВИ
H = {}
H[2] = Card(Rank(Rank.TWO), Suit(Suit.HEARTS))
H[3] = Card(Rank(Rank.THREE), Suit(Suit.HEARTS))
H[4] = Card(Rank(Rank.FOUR), Suit(Suit.HEARTS))
H[5] = Card(Rank(Rank.FIVE), Suit(Suit.HEARTS))
H[6] = Card(Rank(Rank.SIX), Suit(Suit.HEARTS))
H[7] = Card(Rank(Rank.SEVEN), Suit(Suit.HEARTS))
H[8] = Card(Rank(Rank.EIGHT), Suit(Suit.HEARTS))
H[9] = Card(Rank(Rank.NINE), Suit(Suit.HEARTS))
H[10] = Card(Rank(Rank.TEN), Suit(Suit.HEARTS))
H['J'] = Card(Rank(Rank.JACK), Suit(Suit.HEARTS))
H['Q'] = Card(Rank(Rank.QUEEN), Suit(Suit.HEARTS))
H['K'] = Card(Rank(Rank.KING), Suit(Suit.HEARTS))
H['A'] = Card(Rank(Rank.ACE), Suit(Suit.HEARTS))
HEARTS = [H[2], H[3], H[4], H[5], H[6], H[7], H[8], H[9], H[10], H['J'], H['Q'], H['K'], H['A']]


# global FULL_SET
FULL_DECK = SPADES + CLUBS + DIAMONDS + HEARTS
