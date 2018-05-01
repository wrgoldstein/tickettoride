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

	def __init__(self, gameboard, strategy):
		self.strategy = strategy(self, gameboard)
		self.train_cards = []
		self.routes = []
		self.tickets = []
		self.trains = 45

	def score(self):
		return self.route_points() + self.ticket_points()

	def route_points(self):
		route_points = 0
		for route in self.routes:
			route_points += Player.ROUTE_SCORING[route.length]
		return route_points

	def ticket_points(self):
		ticket_points = 0
		for ticket in self.tickets:
			if satisfied(ticket, self.routes):
				ticket_points += ticket.points
			else:
				ticket_points -= ticket.points
		return ticket_points

	def action(self):
		self.strategy.action()

	def choose_tickets(self, cards, must_keep):
		self.strategy.choose_tickets(cards, must_keep)


