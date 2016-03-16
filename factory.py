from logger import log
from objects import *

class SquareManager(object):
	def __init__(self):
		self.squares = {}

	def createSquare(self, name, x, y):
		log.debug("Get new square %s" % name)
		square = Square(name, x, y)
		self.squares[name] = square

	def cleanSquare(self, square):
		square.piece = None

	@property
	def info(self):
		return self.squares

class PieceManager(object):
	def __init__(self):
		self.pieces = set()
		self.pieces_del = set()

	def createPiece(self, name):
		log.debug("Get new piece %s" % name)
		piece = Piece(name)
		self.pieces.add(piece)
		return piece

	def removePiece(self, piece):
		piece.square = None
		self.pieces.remove(piece)
		self.pieces_del.add(piece)

	@property
	def info(self):
		return self.pieces

	@property
	def info_del(self):
		return self.pieces_del

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

	def getMovement(self, mconf):
		name = mconf["name"]
		if self.movements.get(name) is None:
			log.debug("Get new movement %s" % name)
			self.movements[name] = Movement(mconf)
		return self.movements[name]

	@property
	def info(self):
		return self.movements
