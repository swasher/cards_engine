"""
Deck - колода
Trick - взятка
Deal - сдать карты
Dealer - раздающий
Whist - Вист
Безкозырка (No-trump)
Козырь (Trump)
Обязательства (Contracts)
Bids - ставки (торговля)
Discard - сброс (взяток) - это Действие
Pile, или "discard pile" или "discard heap" - Сброс (место для сброшенных карт)
"""
import random
import sys
from classes import *

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
    tretya_dama = 0

    def printing(self):
        # print(f'Расклад 4-0: {self.rasklad_4_0/total_try:.2%}')
        # print(f'Расклад 3-1: {self.rasklad_3_1/total_try:.2%}')
        # print(f'Расклад 2-2: {self.rasklad_2_2/total_try:.2%}')
        # print(f'Дама бланк или вторая дама: {self.dama_blank_OR_vtoraya_dama/total_try:.2%}')
        # print(f'Третья дама: {self.tretya_dama/total_try:.2%}')
        # print(f'Голый туз: {self.goliy_tuz/total_try:.2%}')

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


def analyze(right_hand: Hand, left_hand: Hand):

    suit = Suit.SPADES

    def tretya_dama(hand):
        if len(hand.card_set) >= 3:
            if hand.get_high_card(suit).rank == Rank.QUEEN:
                return True

    def dama_blank_OR_vtoraya_dama(hand):
        if len(hand.card_set) in [1, 2]:
            if hand.get_high_card(suit).rank == Rank.QUEEN:
                return True

    def goliy_tuz(hand: Hand):
        if len(hand.card_set) == 1:
            if hand.card_set[0].rank == Rank.ACE:
                return True

    if tretya_dama(left_hand) or tretya_dama(left_hand):
        stat.tretya_dama += 1

    if goliy_tuz(left_hand) or goliy_tuz(right_hand):
        stat.goliy_tuz += 1

    if dama_blank_OR_vtoraya_dama(left_hand) or dama_blank_OR_vtoraya_dama(right_hand):
        stat.dama_blank_OR_vtoraya_dama += 1

    if len(right_hand.card_set) + len(left_hand.card_set) == 4:
        match len(right_hand.card_set):
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

    if len(right_hand.card_set) + len(left_hand.card_set) == 5:
        match len(right_hand.card_set):
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



import sys
if __name__ == "__main__":

    # DECK = Hand(SPADES, S_Q, D10, H_A)
    # print(type(DECK))
    # print
    # sys.exit()

    """
    PREPARE
    """

    DECK = Hand(SPADES)
    PILE = Hand()

    left_hand = Hand()
    right_hand = Hand()
    player = Hand()

    """
    LET'S PLAY
    """

    DECK.move(player, (S_9, S10, S_Q, S_K))

    total_try = 10000
    stat.total_try = total_try

    print('====== PLAYER   :', player)
    print('====== OPPONENTS:', DECK)
    print('====== TRYs     :', total_try)

    for i in range(total_try):
        for card in list(DECK.card_set):
            random_opponent = random.choice([right_hand, left_hand])
            DECK.move(random_opponent, card)

        # print(f'Try {i}: RIGHT {right_hand} \t LEFT {left_hand}'.expandtabs(40), end="\r")
        analyze(right_hand, left_hand)

        right_hand.discard_to_deck()
        left_hand.discard_to_deck()

    stat.printing()

