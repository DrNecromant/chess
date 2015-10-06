from factory import *
from logger import log

from config import *
from errors import *

class Board(SquareManager):
	def __init__(self, size):
		SquareManager.__init__(self)
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
				self.createSquare(name, x, y)

	def getSquare(self, pos):
		if pos not in self.squares:
			raise PositionError("Wrong position %s" % pos)
		return self.squares[pos]

	def observeSquare(self, x, y):
		for c in (x, y):
			if c not in range(len(self.numbers)):
				return None
		return self.getSquare((x, y))

class Game(object):
	def __init__(self, size):
		self.bd = Board(size)
		self.pm = PieceManager()
		self.cm = ColorManager()
		self.mm = MovementManager()

	def setPosition(self, pos):
		for pname in [pos[i:i+3] for i in range(0, len(pos), 3)]:
			piece_config = PIECES[pname[0]]
			square_name = pname[1:]
			piece = self.pm.createPiece(piece_config["name"])
			movement = self.mm.getMovement(piece_config["movement"])
			color = self.cm.getColor(piece_config["color"])
			square = self.bd.getSquare(square_name)
			self.setPiece(piece, square, color, movement)

	def setPiece(self, piece, square, color = None, movement = None):
		piece.square = square
		square.piece = piece
		if color:
			piece.color = color
			color.piece = piece
		if movement:
			piece.movement = movement
			movement.piece = piece

	def movePiece(self, piece, square):
		# Make the old square is empty
		self.bd.cleanSquare(piece.square)
		if square.piece:
			# remove piece from new square
			self.pm.removePiece(square.piece)
		self.setPiece(piece, square)

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
				s = self.bd.observeSquare(x, y)
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
			s = self.bd.observeSquare(x0 + dx, y0 + dy)
			if s is None:
				break
			yield s

if __name__ == "__main__":
	g = Game(8)
	g.setPosition("Ra1Rh1ra8rh8Bc1Bf1bc8bf8")

	log.debug("=== squares ===")
	bdinfo = g.bd.info
	for l in g.bd.letters:
		for n in g.bd.numbers:
			k = l + n
			s = bdinfo[k]
			if s.piece is not None:
				log.debug("%s %s %s %s" % (k, s.x, s.y, s.piece))
	log.debug("=== pieces ===")
	for p in g.pm.info:
		log.debug("%s: %s" % (p, map(str, g.getMoves(p))))
	log.debug("=== pieces_del ===")
	for p in g.pm.info_del:
		log.debug("%s: %s" % (p, map(str, g.getMoves(p))))
	log.debug("=== colors ===")
	cminfo = g.cm.info
	for c in cminfo:
		log.debug("%s %s" % (c, cminfo[c]))