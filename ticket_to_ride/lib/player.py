import uuid
from itertools import chain
from helpers import satisfied

class Player:
	ROUTE_SCORING = {
	    1: 1,
	    2: 2,
	    3: 4,
	    4: 7,
	    5: 10,
	    6: 15
	}

	def __init__(self, strategy):
		self.name = uuid.uuid4().get_hex()[:6]
		print 'made name, ', self.name
		self.strategy = strategy(self)
		self.trains = []
		self.routes = []
		self.tickets = []
		self.ticket_points = 0
		self.route_points = 0
		self.train_count = 45

	def sit(self, gameboard):
		gameboard.players.append(self)
		self.gameboard = gameboard

	def score(self):
		return self.route_points + self.ticket_points

	def choose_tickets(self, tickets, keep):
		to_keep = tickets[:keep] #TODO defer to a strategy
		self.tickets += to_keep
		self.ticket_points -= sum([ticket.points for ticket in to_keep])
		return list(set(tickets).difference(to_keep))

	def action(self):
		self.strategy.action()

	def trains_for_color(self, color):
		return [t for t in self.trains if t == color]

	def unsatisfied_tickets(self):
		return [ticket for ticket in self.tickets if not ticket.satisfied]

	def satisfy_any_tickets(self):
		for ticket in self.unsatisfied_tickets():
			if satisfied(ticket, self.routes):
				ticket.satisifed = True
				self.ticket_points += ticket.points

	def connected_cities(self):
		return list(chain(*map(lambda r: [r.from_city, r.to_city], self.routes)))

	def claim_route(self, route, color):
		filtered = 0
		trains = []
		for train in self.trains:
			if train == color and route.length > filtered:
				filtered += 1
			else:
				trains.append(train)
		self.trains = trains
		# print self.name, " is claiming route:", route, '; ', self.train_count, 'left', self.gameboard.train_deck.cards_left()
		self.train_count -= route.length
		self.gameboard.train_deck.discards += list(route.length * color)
		route.claimed = True
		self.routes.append(route)
		self.satisfy_any_tickets()
		self.route_points += Player.ROUTE_SCORING[route.length]
		return