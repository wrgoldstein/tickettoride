from copy import deepcopy
from helpers import *

class TrainDeck(object):
    def __init__(self):
        self.cards = list('bgkoprwy' * 12) # colored cards
        self.discards = []
    
    def shuffle(self):
        self.cards = shuffled(self.cards + self.discards)
        self.discards = []
        
    def deal(self, n):
        if n > len(self.cards):
            self.shuffle()  # simplification
        return [self.cards.pop() for _ in range(n)]

    def stats(self):
        return {
            'cards': len(self.cards),
            'discards': len(self.discards)
        }