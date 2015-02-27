from logger import log
from errors import *

class Square(object):
	def __init__(self, name, x, y):
		self._piece = None
		self.name = name
		self.x = x
		self.y = y

	def __str__(self):
		return self.name

	@property
	def piece(self):
		return self._piece

	@piece.setter
	def piece(self, piece):
		self._piece = piece

class Piece(object):
	def __init__(self, name):
		self.name = name
		self._square = None
		self._color = None
		self._movement = None

	def __str__(self):
		piece_attrs = [self.name]
		if self._color:
			piece_attrs.append(str(self._color))
		if self._square:
			piece_attrs.append(str(self._square))
		if self._movement:
			piece_attrs.append(str(self._movement))
		return "-".join(piece_attrs)

	def capture(self):
		self._square = None

	@property
	def square(self):
		return self._square

	@square.setter
	def square(self, square):
		self._square = square

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, color):
		self._color = color

	@property
	def movement(self):
		return self._movement

	@movement.setter
	def movement(self, movement):
		self._movement = movement

class Color(object):
	def __init__(self, name):
		self.name = name
		self._piece = set()

	def __str__(self):
		return self.name

	@property
	def piece(self):
		return self._piece

	@piece.setter
	def piece(self, piece):
		self._piece.add(piece)

class Movement(object):
	def __init__(self, name, directions, steps):
		self.name = name
		self._piece = set()
		self.directions = directions
		self.steps = steps

	def __str__(self):
		return self.name

	@property
	def piece(self):
		return self._piece

	@piece.setter
	def piece(self, piece):
		self._piece.add(piece)
