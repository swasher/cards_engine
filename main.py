"""
Deck - колода
Trick - взятка
[to] Deal - сдать карты,
Deal - "раздача" (игровая сессия)
Dealer - раздающий
Whist - Вист
Безкозырка (No-trump)
Козырь (Trump)
Обязательства (Contracts)
Bids - ставки (торговля)
Discard - сброс (взяток) - это Действие
Pile, или "discard pile" или "discard heap" - Сброс (место для сброшенных карт)
Shuffle - тусовать
"""
import random
import sys
from classes import S, C, D, H, J, Q, K, A
from classes import Rank, Suit
from classes import Player, Pile, Deck, Table
from classes import SPADES, CLUBS, DIAMONDS, HEARTS


def show(paramname, param):
    if param:
        print(f'{paramname}:\t {param / total_try:.2%}')



class Igra:
    gora: int = 0  # сколько пишется в гору при проигрыше
    vist: int = 0  # сколько вистов пишется за взятку


class Statistic:
    total_try = 0
    tretya_dama = 0
    dama_blank_OR_vtoraya_dama = 0

    rasklad_4_0 = 0
    rasklad_3_1 = 0
    rasklad_2_2 = 0

    rasklad_5_0 = 0
    rasklad_4_1 = 0
    rasklad_3_2 = 0

    goliy_tuz = 0

    def printing(self):
        print('\nResult:')
        show('Расклад 4-0', self.rasklad_4_0)
        show('Расклад 3-1', self.rasklad_3_1)
        show('Расклад 2-2', self.rasklad_2_2)
        show('Расклад 5-2', self.rasklad_5_0)
        show('Расклад 4-1', self.rasklad_4_1)
        show('Расклад 3-2', self.rasklad_3_2)
        show('Дама бланк или вторая дама', self.dama_blank_OR_vtoraya_dama)
        show('Третья дама', self.tretya_dama)
        show('Голый туз', self.goliy_tuz)


stat = Statistic()


def analyze(right_hand: Player, left_hand: Player):

    suit = Suit.SPADES
    # todo тут гвоздями прибито, что мы тестируем именно на Пиках

    def tretya_dama(hand):
        if len(hand.get_suit(suit)) >= 3:
            if hand.get_high_card(suit).rank == Rank.QUEEN:
                return True

    def dama_blank_OR_vtoraya_dama(hand):
        if len(hand.get_suit(suit)) in [1, 2]:
            if hand.get_high_card(suit).rank == Rank.QUEEN:
                return True

    def goliy_tuz(hand: Player):
        if hand.number_of_cards == 1:
            c, = hand.cards  # unpack set
            if c.rank == Rank.ACE:
                return True

    if tretya_dama(left_hand) or tretya_dama(right_hand):
        stat.tretya_dama += 1

    if goliy_tuz(left_hand) or goliy_tuz(right_hand):
        stat.goliy_tuz += 1

    if dama_blank_OR_vtoraya_dama(left_hand) or dama_blank_OR_vtoraya_dama(right_hand):
        stat.dama_blank_OR_vtoraya_dama += 1

    if right_hand.number_of_cards + left_hand.number_of_cards == 4:
        match right_hand.number_of_cards:
            case 0:
                stat.rasklad_4_0 += 1
            case 1:
                stat.rasklad_3_1 += 1
            case 2:
                stat.rasklad_2_2 += 1
            case 3:
                stat.rasklad_3_1 += 1
            case 4:
                stat.rasklad_4_0 += 1

    if right_hand.number_of_cards + left_hand.number_of_cards == 5:
        match right_hand.number_of_cards:
            case 0:
                stat.rasklad_5_0 += 1
            case 1:
                stat.rasklad_4_1 += 1
            case 2:
                stat.rasklad_3_2 += 1
            case 3:
                stat.rasklad_3_2 += 1
            case 4:
                stat.rasklad_4_1 += 1
            case 5:
                stat.rasklad_5_0 += 1


if __name__ == "__main__":

    """
    PREPARE
    """

    # card_set = SPADES[5:], CLUBS[5:], DIAMONDS[5:], HEARTS[5:]
    # card_set = SPADES[5:], C[4], H[A]
    # card_set = S[9], S[10], S['Q'], S['K']
    card_set = SPADES[5:]

    left_hand = Player()
    right_hand = Player()
    my_hand = Player()

    deck = Deck()
    pile = Pile()

    table = Table(card_set=card_set, deck=deck, pile=pile, players=[left_hand, right_hand, my_hand])

    print(table.cards)

    table.reset()

    """
    LET'S PLAY
    """

    total_try = 1000000
    stat.total_try = total_try

    print('====== MY_HAND   :', my_hand)
    print('====== DECK     :', deck)
    print('====== TRYs     :', total_try)

    for i in range(total_try):
        deck.draw(my_hand, (S[7], S[J], S[K], S[A]))

        for card in deck.cards:
            random_opponent = random.choice([right_hand, left_hand])
            deck.draw(random_opponent, card)

        # print(f'Try {i}: RIGHT {right_hand} \t LEFT {left_hand}'.expandtabs(40), end="\r")
        # print(f'Try {i}: RIGHT {right_hand} \t LEFT {left_hand}'.expandtabs(40))
        analyze(right_hand, left_hand)
        table.reset()

    stat.printing()
