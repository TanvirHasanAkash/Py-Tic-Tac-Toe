from position import Position
from turn import Turn


class Board:
	def __init__(self):
		self.x = 'X'
		self.o = 'O'
		self.empty = '-'
		self.board_size = 3

		self.board = [
			[self.empty, self.empty, self.empty],
			[self.empty, self.empty, self.empty],
			[self.empty, self.empty, self.empty]
		]

	def turn_to_symbol(self, turn: Turn) -> str:
		if turn == Turn.player_1:
			return self.x
		if turn == Turn.player_2:
			return self.o
		return '-'

	def check_winner(self) -> bool:
		# Rows
		for y in self.board:
			if y[0] == y[1] == y[2] != self.empty:
				return True

		# Columns
		for x in range(self.board_size):
			if self.board[0][x] == self.board[1][x] == self.board[2][x] != self.empty:
				return True

		# Diagonal [Top-Left to Bottom-Right]
		if self.board[0][0] == self.board[1][1] == self.board[2][2] != self.empty:
			return True

		# Diagonal [Top-Right to Bottom-Left]
		if self.board[0][2] == self.board[1][1] == self.board[2][0] != self.empty:
			return True

		return False

	def take_turn(self, turn: Turn, position: Position) -> None:
		self.board[position.y][position.x] = self.turn_to_symbol(turn)

	def print(self) -> None:
		print(end='\n')
		for y in self.board:
			for i, x in enumerate(y):
				if i + 1 == self.board_size:
					print(x)
				else:
					print(x, end='\t')
		print(end='\n')
