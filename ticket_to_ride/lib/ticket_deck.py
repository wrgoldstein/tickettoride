from data import *
from copy import deepcopy
from helpers import *

class TicketDeck(object):
    cards = tickets

    def __init__(self):
        self.cards = deepcopy(TicketDeck.cards)
    
    def deal(self, n):
        return [self.cards.pop(0) for _ in range(n)]

    def accept(self, cards):
    	self.cards += cards

    def shuffle(self):
        self.cards = shuffled(self.cards)