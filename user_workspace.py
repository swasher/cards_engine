from classes import HEARTS, SPADES, S
from classes import Table, Card, Deck, Pile, Player


def prn():
    print('DECK:', deck)
    print('PILE:', pile)
    print('player1:', player1)
    print('player2:', player2)
    print('player3:', player3)
    print('-----------------\n')


card_set = S[4], S['A'], HEARTS, SPADES
deck = Deck()
pile = Pile()
player1 = Player()
player2 = Player()
player3 = Player()

table = Table(
    card_set=card_set,
    deck=deck,
    pile=pile,
    players=[player1, player2, player3]
)


prn()

deck.draw(player1)

prn()
