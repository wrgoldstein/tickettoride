from ticket_to_ride import TicketToRide, Player, DefaultStrategy

def test_no_reuse_of_train_deck():
	game1 = TicketToRide()
	Player(DefaultStrategy).sit(game1)
	Player(DefaultStrategy).sit(game1)
	game1.train_deck.deal(30)

	game2 = TicketToRide()
	Player(DefaultStrategy).sit(game2)
	Player(DefaultStrategy).sit(game2)
	game1.train_deck.deal(30)

	assert len(game1.train_deck.cards) != len(game2.train_deck.cards)

def test_simulate():
	game = TicketToRide()
	Player(DefaultStrategy).sit(game)
	Player(DefaultStrategy).sit(game)
	game.simulate()
	assert game.winner is not None
	assert game.winner in game.players

def test_scores_start_negative():

	game1 = TicketToRide()
	Player(DefaultStrategy).sit(game1)
	Player(DefaultStrategy).sit(game1)
	Player(DefaultStrategy).sit(game1)
	game1.simulate()

	game2 = TicketToRide()
	Player(DefaultStrategy).sit(game2)
	Player(DefaultStrategy).sit(game2)
	Player(DefaultStrategy).sit(game2)

	assert game2.players[0].score() == 0
	assert game2.players[1].score() == 0
	assert game2.players[2].score() == 0
