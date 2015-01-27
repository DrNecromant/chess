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

	def clear(self):
		self._piece = None

	@property
	def piece(self):
		return self._piece

	@piece.setter
	def piece(self, piece):
		if self._piece is not None:
			self._piece.capture()
		self._piece = piece
		if piece.square != self:
			piece.square = self

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
		if self._square is not None:
			# clear old square
			self._square.clear()
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

	@property
	def movement(self):
		return self._movement

	@movement.setter
	def movement(self, movement):
		self._movement = movement
		if self not in movement.piece:
			movement.piece = self

	def getMoves(self):
		if not self.square:
			return
		x0, y0 = self.square.x, self.square.y
		for dx, dy in self.movement.directions:
			x, y = x0, y0
			while True:
				x += dx
				y += dy
				square = self.movement.observe(x, y)
				if square is None:
					break
				piece = square.piece
				if piece:
					if piece.color == self.color:
						break
					else:
						yield square
						break
				yield square
		for dx, dy in self.movement.steps:
			square = self.movement.observe(x0 + dx, y0 + dy)
			if square is None:
				break
			yield square

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

class Movement(object):
	def __init__(self, name):
		self.name = name
		self._piece = set()
		self.directions = set()
		self.steps = set()
		self.observe = lambda x, y: None

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
