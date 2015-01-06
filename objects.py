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

class Piece(object):
	def __init__(self, name, color):
		self._square = None
		self.name = name
		self.color = color

	def __str__(self):
		if self._square is None:
			return "%s %s" % (self.color, self.name)
		return "%s %s %s" % (self.color, self.name, self.square)

	@property
	def square(self):
		return self._square

	@square.setter
	def square(self, square):
		self._square = square
		if square.piece != self:
			square.piece = self

class Bishop(Piece):
	def __init__(self, name, color):
		Piece.__init__(self, name, color)

	def getMoves(self, observe):
		for delta in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
			x, y = self.square.x, self.square.y
			dx, dy = delta
			while True:
				x += dx
				y += dy
				if observe(x, y) is None:
					break
				yield x, y
