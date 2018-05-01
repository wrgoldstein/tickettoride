from ticket_to_ride import TicketToRide, Player, DefaultStrategy

def test_initialization():
	game = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy])
	assert game.strategies == [DefaultStrategy, DefaultStrategy]
	assert len(game.players) == 2

def test_setup():
	game = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy])
	game.setup()
	for player in game.players:
		assert player.trains == 45
		assert len(player.train_cards) == 4

def test_game_turn():
	def mock_action(self):
		self.took_an_action = True
		return 'action!'

	old_action = Player.action
	Player.action = mock_action

	game = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy])
	game.setup()

	game.game_turn()
	
	for player in game.players:
		assert player.took_an_action == True

	Player.action = old_action

def test_game_turn():
	def mock_action(self):
		self.took_an_action = True
		return 'action!'

	old_action = Player.action
	Player.action = mock_action

	game = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy])
	game.setup()

	game.game_turn()
	
	for player in game.players:
		assert player.took_an_action == True

	Player.action = old_action

def test_no_reuse_of_train_deck():
	game1 = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy])
	game1.train_deck.deal(30)

	game2 = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy])

	assert len(game1.train_deck.cards) != len(game2.train_deck.cards)

def test_simulate():
	game = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy])
	game.simulate()
	assert game.winner is not None
	assert game.winner in game.players

def test_scores_start_negative():
	game1 = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy, DefaultStrategy])
	game1.simulate()

	game2 = TicketToRide(strategies=[DefaultStrategy, DefaultStrategy, DefaultStrategy])
	assert game2.players[0].score() == 0
	assert game2.players[1].score() == 0
	assert game2.players[2].score() == 0
