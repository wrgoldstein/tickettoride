from collections import Counter
import random

class DefaultStrategy:
	"""
	The default strategy will be to claim a random available route if possible
	and otherwise draw from the deck.
	"""

	def __init__(self, player):
		self.player = player

	def __str__(self):
		return "DefaultStrategy"

	def action(self):
		"""
		Take a random route if possible, otherwise take
		the top two train cards.
		"""
		claimable = self.claimable_routes()

		if self.claim_best_route(claimable):
			return
		elif self.player.gameboard.train_deck.cards_left() >= 2:
			self.pick_best_train_cards()
		else:
			self.player.draw_ticket(1)
		pass

	def claim_best_route(self, claimable):
		if not len(claimable):
			return False
		route = claimable[0]

		color = self.route_solutions(route)[0]  # choose any eligible train color

		self.player.claim_route(route, color)
		return True

	def pick_best_train_cards(self):
		"""
		Pick two cards off the top of the deck.
		"""
		return self.player.gameboard.deal_player_trains(self.player, 2) 

	def claimable_routes(self):
		claimable = []
		claimed_pairs = [(r.from_city, r.to_city) for r in self.player.routes]
		for route in self.player.gameboard.routes:
			if not route.claimed and self.route_solutions(route):
				# A double route cannot be claimed twice
				if (route.from_city, route.to_city) not in claimed_pairs:
					claimable.append(route)
		return claimable

	def route_solutions(self, route):
		"""
		Given a player's available train cards, what can they use to 
		claim a given route.
		"""
		solutions = []
		for color in 'bgkoprwy':
			if route.color == color or route.color == '-':
				if len(self.player.trains_for_color(color)) >= route.length: 
					solutions.append(color)
		return solutions

	#TODO
	# def choose_tickets(self, cards, must_keep):
	# 	"""
	# 	Choose a random minimum number of ticket cards
	# 	"""
	# 	return cards[:must_keep]
