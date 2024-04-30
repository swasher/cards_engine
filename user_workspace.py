from classes import HEARTS, SPADES, CLUBS, DIAMONDS, S, C, D, H
from classes import Table, Card, Deck, Pile, Player


def prn():
    print('\n')
    print('DECK:', deck)
    print('PILE:', pile)
    print('player1:', player1)
    print('player2:', player2)
    print('player3:', player3)
    print('-----------------\n')


card_set = SPADES[5:], CLUBS[5:], DIAMONDS[5:], HEARTS[5:]
Table(card_set=card_set)

deck = Deck()
pile = Pile()
player1 = Player()
player2 = Player()
player3 = Player()


prn()

print()

for i in range(10):
    deck.draw(player1)
    deck.draw(player2)
    deck.draw(player3)

prn()


