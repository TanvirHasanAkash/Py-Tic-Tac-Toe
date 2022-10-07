from turn import Turn
from position import Position
from board import Board
from turn_manager import TurnManager
from input_manager import InputManager


class GameManager:
	def __init__(self):
		self.board = Board()
		self.turn_manager = TurnManager()
		self.game_loop = True

	def print_winner(self) -> None:
		if self.turn_manager.turn == Turn.player_1:
			print("Player 2 won!")
			return
		if self.turn_manager.turn == Turn.player_2:
			print("Player 1 won!")
			return

	def run(self) -> None:
		while self.game_loop:
			if not self.board.check_winner():
				self.board.take_turn(self.turn_manager.turn, InputManager.take_input())
				self.board.print()
				self.turn_manager.switch_turn()
			else:
				self.print_winner()
				self.game_loop = False


if __name__ == '__main__':
	game = GameManager()
	game.run()
