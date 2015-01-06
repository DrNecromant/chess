from logger import log
import string
from objects import *
from errors import *

class Board(object):
	def __init__(self, size):
		#FIXME Set color as a separate object
		self._squares = {}
		self.letters = list(string.ascii_lowercase)
		letters_range = len(self.letters)
		if size > letters_range:
			raise BoardError("Board size %s exceeds letter's range %s" % (size, letters_range))
		self.numbers = map(str, range(1, letters_range + 1))
		self.letters = self.letters[:size]
		self.numbers = self.numbers[:size]

	def _check_pos_value(self, pos):
		"""
		Check that position value is correct. For example, "e4" or (4, 3)
		"""
		if type(pos) not in (tuple, str):
			raise PositionError("Wrong square position type %s %s" % (pos, type(pos)))
		if len(pos) != 2:
			raise PositionError("Wrong square position length %s %s" % (pos, len(pos)))
		if type(pos) == tuple:
			for c in pos:
				if type(c) != int or c not in range(len(self.numbers)):
					raise PositionError("Wrong square coordinate %s in position %s" % (c, pos))
		if type(pos) == str:
			if pos[0] not in self.letters or pos[1] not in self.numbers:
				raise PositionError("Wrong square coordinate in position %s" % pos)

	def getSquare(self, pos):
		self._check_pos_value(pos)
		if type(pos) == str:
			name = pos
			x = self.letters.index(pos[0])
			y = self.numbers.index(pos[1])
		else:
			x, y = pos
			name = self.letters[x] + self.numbers[y]
		if self._squares.get(name) is None:
			log.debug("Get new square %s" % name)
			square = Square(name, x, y)
			self._squares[name] = square
		return self._squares[name]

	@property
	def info(self):
		return self._squares

class PieceManager(object):
	def __init__(self):
		self._pieces = []

	def createPiece(self, name, color):
		log.debug("Create new piece %s %s" % (name, color))
		if name == "Bishop":
			piece = Bishop(name, color)
		self._pieces.append(piece)
		return piece

	@property
	def info(self):
		return self._pieces
