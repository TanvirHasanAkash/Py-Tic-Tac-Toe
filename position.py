class Position:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	def __str__(self):
		return f"X: {self.x}; Y: {self.y};"

	def parse_input(self, x: str, y: str) -> bool:
		try:
			x = int(x) - 1
			y = int(y) - 1

			if x < 0 or x > 2 or y < 0 or y > 2:
				return False

			self.x = x
			self.y = y

			return True
		except ValueError:
			return False
