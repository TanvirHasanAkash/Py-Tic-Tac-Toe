from turn import Turn


class TurnManager:
	def __init__(self):
		self.turn = Turn.player_1

	def switch_turn(self) -> None:
		if self.turn == Turn.player_1:
			self.turn = Turn.player_2
		elif self.turn == Turn.player_2:
			self.turn = Turn.player_1
