from copy import deepcopy

from lib.data import cities, Route, routes, Ticket, tickets
from lib.train_deck import TrainDeck
from lib.ticket_deck import TicketDeck
from lib.player import Player
from lib.strategies import DefaultStrategy, SimpleOptimizer
from lib import helpers

class TicketToRide(object):
    routes = routes[1:]
    
    def __init__(self):
        self.players = []
        self.routes = deepcopy(routes)
        self.winner = None
        self.train_deck = TrainDeck()
        self.ticket_deck = TicketDeck()
        self.face_up = []
        self.longest_path_bonus = None
        self.last_turns = None
        self.n_turns = 0
        self.score_history = []

    def pick_who_goes_first(self):
        self.players = helpers.shuffled(self.players)

    def setup(self):
        #  each player gets 45 trains
        self.train_deck.shuffle()

        #  deal a starting hand of 4 train cards to each player
        for player in self.players:
            self.deal_player_trains(player, 4)

        #  turn the top 5 remaining train cards face up
        #TODO face up cards
        # self.face_up = self.train_deck.deal(5)

        #TODO  # Longest Path Bonus isn't set

        #  shuffle the ticket deck and deal each player 3, of which they take at least 2 
            # (returned cards go on the bottom of the ticket deck)
        self.ticket_deck.shuffle()

        for player in self.players:
            self.deal_player_tickets(player, 3, keep=2)


    def game_turn(self):
        # perform a single turn of the game
        for player in self.players:

            if self.last_turns == len(self.players):
                self.winner = self.currently_winning()
                self.losers = filter(lambda p: p != self.winner, self.players)
                assert self.winner == self.currently_winning()
                return

            player.action()

            if self.last_turns is not None:
                self.last_turns += 1
            elif self.last_turns is None and player.train_count <= 3:
                self.last_turns = 0
            else:
                continue
        self.score_history.append([p.score() for p in self.players])


    def simulate(self):
        self.pick_who_goes_first()
        self.setup()

        while self.winner is None:
            self.game_turn()
            self.n_turns += 1
        pass

    def deal_player_trains(self, player, n):
        return self.train_deck.deal(player, n)

    def deal_player_tickets(self, player, n, keep):
        tickets = self.ticket_deck.deal(3)
        not_chosen = player.choose_tickets(tickets, keep=2)
        self.ticket_deck.accept(not_chosen)
    
    def currently_winning(self):
        i = max(range(len(self.players)), key=lambda x: self.players[x].score())
        return self.players[i]
