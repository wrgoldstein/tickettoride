from collections import Counter
import random

def shuffled(L):
    return sorted(L, key=lambda *args: random.random())

class DefaultStrategy:
	"""
	The default strategy will be to claim a random available route if possible
	and otherwise draw from the deck.
	"""

	def __init__(self, player, gameboard):
		self.player = player
		self.gameboard = gameboard

	def action(self):
		"""
		Take a random route if possible, otherwise take
		the top two train cards.
		"""
		claimable = self.claimable_routes(self.gameboard)
		if not self.claim_best_route(claimable):
			self.pick_best_train_cards()
		pass

	def claim_best_route(self, claimable):
		if not len(claimable):
			return False
		route = claimable[0]
		cards_spent = self.claim_route(route)
		self.gameboard.train_deck.discards += cards_spent
		return True

	def pick_best_train_cards(self):
		"""
		Pick two cards off the top of the deck
		"""
		self.gameboard.deal_player_train_cards(self.player, 2) 
		return True

	def claimable_routes(self, gameboard):
		return filter(self.route_solutions, self.gameboard.routes)

	def train_cards_for_color(self, color):
		return Counter(self.player.train_cards)[color]

	def route_solutions(self, route):
		solutions = []

		if len(route.claimed) == len(route.color):
			return solutions

		# neutral color
		if route.color == '-':
			for color in 'bgkoprwy':
				if self.train_cards_for_color(color) >= route.length:
					solutions.append(color)

		else:

			# some routes have split colors
			for color in route.color:
				if color in route.claimed:
					continue

				if self.train_cards_for_color(color) >= route.length:
					solutions.append(color)

		return solutions


	def claim_route(self, route):
		solution = self.route_solutions(route)[0]

		this_color = filter(lambda s: s == solution, self.player.train_cards)
		other_colors = filter(lambda s: s != solution, self.player.train_cards)

		new_this_color_n = len(this_color) - route.length
		self.player.train_cards = other_colors + list(solution * new_this_color_n)

		self.player.trains -= route.length
		route.claim(solution)
		self.player.routes.append(route)

		return solution * route.length

	def choose_tickets(self, cards, must_keep):
		"""
		Choose a random minimum number of ticket cards
		"""
		chosen = shuffled(cards)[:must_keep]
		self.player.tickets += chosen
