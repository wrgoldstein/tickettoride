from ticket_to_ride import Ticket, Route, helpers

def test_ticket():
	routes = [
		Route('Vancouver', 'Calgary', 3, '-'),
		Route('Vancouver', 'Seattle', 1, '-'),
		Route('Seattle', 'Portland', 1, '-'),
		Route('San Francisco', 'Los Angeles', 1, '-')
	]

	assert helpers.satisfied(Ticket('Vancouver', 'Portland', 10), routes) == True
	assert helpers.satisfied(Ticket('Vancouver', 'Los Angeles', 10), routes) == False
