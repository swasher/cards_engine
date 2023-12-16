from __future__ import annotations
from enum import Enum
from typing import Tuple


class Suit(Enum):
    SPADES = "♠"
    CLUBS = "♣"
    DIAMONDS = "♢"
    HEARTS = "♡"

    def __str__(self) -> str:
        return self.value


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

    def __gt__(self, other: "Rank") -> bool:
        return self.value > other.value

    def __lt__(self, other: "Rank") -> bool:
        return self.value < other.value


class Card:
    rank: Rank
    suit: Suit

    # def __hash__(self):
    #     return hash((self.rank, self.suit))

    # def __lt__(self, other: "Card"):
    #     return self.rank > other.rank and self.suit == other.suit

    # def __gt__(self, other: "Card"):
    #     return self.rank < other.rank and self.suit == other.suit
    #
    # def __eq__(self, other: "Card"):
    #     return self.rank == other.rank and self.suit == other.suit

    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def __repr__(self):
        return f'{self.rank}{self.suit}'


class Hand:
    _cards: set

    def __init__(self, *args: Card | list[Card]) -> None:
        self._cards = set()
        if args:
            for arg in args:
                if type(arg) is Card:
                    self._cards.add(arg)
                else:
                    self._cards.update(arg)

    @property
    def cards(self):
        return self._cards
    #
    # @cards.setter
    # def cards(self, value):
    #     self._cards = value

    def add_card(self, card: Card) -> None:
        self._cards.update([card])

    def remove_card(self, card: Card) -> None:
        """
        Это приватный метод, потому что карта не может просто "исчезнуть", ее нельзя "выкинуть".
        Карты можно только переность между руками.
        :param card:
        :return:
        """
        pass
        self._cards.remove(card)

    def move_all_to(self, hand: Hand):
        """
        Переместить все карты с руки в другую руку (или вернуть в колоду DECK или в сброс PILE)
        :return:
        """
        if self.__cards:
            for c in self.__cards:
                hand.add_card(c)
                self.remove_card(c)

    def get_suit(self, suit: Suit) -> list[Card]:
        """
        Возвращает все карты выбранной масти в руке.
        :return:
        """
        return list(filter(lambda n: n.suit == suit, self.__cards))

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
            self.__away(c)
            hand.add_card(c)

        if type(cards) is Card:
            # значит в функцию передали одну карту, а не кортеж
            card = cards
            __do_move(card)
        else:
            for card in cards:
                __do_move(card)

    def __str__(self):
        return ' '.join(map(str, self.__cards))


DECK = Hand()
PILE = Hand()

# global SPADES, S_7, S_8, S_9, S10, S_J, S_Q, S_K, S_A
S_7 = Card(Rank(Rank.SEVEN), Suit(Suit.SPADES))
S_8 = Card(Rank(Rank.EIGHT), Suit(Suit.SPADES))
S_9 = Card(Rank(Rank.NINE), Suit(Suit.SPADES))
S10 = Card(Rank(Rank.TEN), Suit(Suit.SPADES))
S_J = Card(Rank(Rank.JACK), Suit(Suit.SPADES))
S_Q = Card(Rank(Rank.QUEEN), Suit(Suit.SPADES))
S_K = Card(Rank(Rank.KING), Suit(Suit.SPADES))
S_A = Card(Rank(Rank.ACE), Suit(Suit.SPADES))
SPADES = [S_7, S_8, S_9, S10, S_J, S_Q, S_K, S_A]

# global CLUBS, C_7, C_8, C_9, C10, C_J, C_Q, C_K, C_A
C_7 = Card(Rank(Rank.SEVEN), Suit(Suit.CLUBS))
C_8 = Card(Rank(Rank.EIGHT), Suit(Suit.CLUBS))
C_9 = Card(Rank(Rank.NINE), Suit(Suit.CLUBS))
C10 = Card(Rank(Rank.TEN), Suit(Suit.CLUBS))
C_J = Card(Rank(Rank.JACK), Suit(Suit.CLUBS))
C_Q = Card(Rank(Rank.QUEEN), Suit(Suit.CLUBS))
C_K = Card(Rank(Rank.KING), Suit(Suit.CLUBS))
C_A = Card(Rank(Rank.ACE), Suit(Suit.CLUBS))
CLUBS = [C_7, C_8, C_9, C10, C_J, C_Q, C_K, C_A]

# global DIAMONDS, D_7, D_8, D_9, D10, D_J, D_Q, D_K, D_A
D_7 = Card(Rank(Rank.SEVEN), Suit(Suit.DIAMONDS))
D_8 = Card(Rank(Rank.EIGHT), Suit(Suit.DIAMONDS))
D_9 = Card(Rank(Rank.NINE), Suit(Suit.DIAMONDS))
D10 = Card(Rank(Rank.TEN), Suit(Suit.DIAMONDS))
D_J = Card(Rank(Rank.JACK), Suit(Suit.DIAMONDS))
D_Q = Card(Rank(Rank.QUEEN), Suit(Suit.DIAMONDS))
D_K = Card(Rank(Rank.KING), Suit(Suit.DIAMONDS))
D_A = Card(Rank(Rank.ACE), Suit(Suit.DIAMONDS))
DIAMONDS = [D_7, D_8, D_9, D10, D_J, D_Q, D_K, D_A]

# global HEARTS, H_7, H_8, H_9, H10, H_J, H_Q, H_K, H_A
H_7 = Card(Rank(Rank.SEVEN), Suit(Suit.HEARTS))
H_8 = Card(Rank(Rank.EIGHT), Suit(Suit.HEARTS))
H_9 = Card(Rank(Rank.NINE), Suit(Suit.HEARTS))
H10 = Card(Rank(Rank.TEN), Suit(Suit.HEARTS))
H_J = Card(Rank(Rank.JACK), Suit(Suit.HEARTS))
H_Q = Card(Rank(Rank.QUEEN), Suit(Suit.HEARTS))
H_K = Card(Rank(Rank.KING), Suit(Suit.HEARTS))
H_A = Card(Rank(Rank.ACE), Suit(Suit.HEARTS))
HEARTS = [H_7, H_8, H_9, H10, H_J, H_Q, H_K, H_A]

# global FULL_SET
FULL_DECK = SPADES + CLUBS + DIAMONDS + HEARTS