from position import Position


class InputManager:
	@staticmethod
	def take_input() -> Position:
		print('Use x-coordinate and y-coordinate to specify your square.')
		position = Position(0, 0)

		while not position.parse_input(input('X: '), input('Y: ')):
			print('Invalid input! Try again!')

		return position
