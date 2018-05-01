from default_strategy import DefaultStrategy
from ..helpers import route_options, distance

class SimpleOptimizer(DefaultStrategy):
	def action(self):
		"""
		Among possible routes to purchase, choose one that best
		connects two cities you have tickets for
		"""
		tickets = self.player.tickets
		for ticket in tickets:
			"""
			Choose an unsatisfied ticket card randomly
			"""
			ticket
			