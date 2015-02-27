from logger import log
import string
from objects import *
from errors import *

class Board(object):
	def __init__(self, size):
		self.squares = {}
		self.letters = list(string.ascii_lowercase)
		letters_range = len(self.letters)
		if size > letters_range:
			raise BoardError("Board size %s exceeds letter's range %s" % (size, letters_range))
		self.numbers = map(str, range(1, letters_range + 1))
		self.letters = self.letters[:size]
		self.numbers = self.numbers[:size]
		# Init all squares
		for l in self.letters:
			for n in self.numbers:
				name = l + n
				x = self.letters.index(l)
				y = self.numbers.index(n)
				square = Square(name, x, y)
				self.squares[name] = square
				self.squares[(x, y)] = square

	def getSquare(self, pos):
		if pos not in self.squares:
			raise PositionError("Wrong position %s" % pos)
		return self.squares[pos]

	def observeSquare(self, x, y):
		for c in (x, y):
			if c not in range(len(self.numbers)):
				return None
		return self.getSquare((x, y))

	def getMoves(self, piece):
		if not (piece.square and piece.movement):
			return
		x0, y0 = piece.square.x, piece.square.y
		# get squares by directions
		for dx, dy in piece.movement.directions:
			x, y = x0, y0
			while True:
				x += dx
				y += dy
				s = self.observeSquare(x, y)
				if s is None:
					break
				p = s.piece
				if p:
					if p.color == piece.color:
						break
					else:
						yield s
						break
				yield s
		# get squares by steps
		for dx, dy in piece.movement.steps:
			s = self.observeSquare(x0 + dx, y0 + dy)
			if s is None:
				break
			yield s

	@property
	def info(self):
		return self.squares

class PieceManager(object):
	def __init__(self):
		self.pieces = set()

	def createPiece(self, name):
		log.debug("Create new piece %s" % name)
		piece = Piece(name)
		self.pieces.add(piece)
		return piece

	@property
	def info(self):
		return self.pieces

class ColorManager(object):
	def __init__(self):
		self.colors = {}

	def getColor(self, name):
		if self.colors.get(name) is None:
			log.debug("Get new color %s" % name)
			self.colors[name] = Color(name)
		return self.colors[name]

	@property
	def info(self):
		return self.colors

class MovementManager(object):
	def __init__(self):
		self.movements = {}

	def getMovement(self, name, directions, steps):
		if self.movements.get(name) is None:
			log.debug("Get new movement %s" % name)
			self.movements[name] = Movement(name, directions, steps)
		return self.movements[name]

	@property
	def info(self):
		return self.movements
