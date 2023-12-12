from classes import HEARTS, SPADES, S
from classes import Deck, Pile, Player
from classes import set_table, get_table


def prn():
    print('DECK:', deck)
    print('PILE:', pile)
    print('player1:', player1)
    print('player2:', player2)
    print('player3:', player3)
    print('-----------------\n')


set_table(HEARTS, SPADES)

deck = Deck()
pile = Pile()

player1 = Player()
player2 = Player()
player3 = Player()

prn()

deck.draw(player1)

prn()
