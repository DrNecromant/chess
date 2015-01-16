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
		if piece.square != self:
			piece.square = self

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
		if piece.color != self:
			piece.color = self

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
		return "-".join(piece_attrs)

	@property
	def square(self):
		return self._square

	@square.setter
	def square(self, square):
		self._square = square
		if square.piece != self:
			square.piece = self

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, color):
		self._color = color
		if self not in color.piece:
			color.piece = self

class Movement(object):
	def __init__(self, name):
		self.name = name
		self._piece = set()
		self.directions = set()

	def __str__(self):
		return self.name

	@property
	def piece(self):
		return self._piece

	@piece.setter
	def piece(self, piece):
		self._piece.add(piece)
		if piece.movement != self:
			piece.movement = self

	def getMoves(self):
		for direction in directions:
			square = self.piece.square
			x, y = square.x, square.y
			dx, dy = direction
			while True:
				x += dx
				y += dy
				if observe(x, y) is None:
					break
				yield x, y
