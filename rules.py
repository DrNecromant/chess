from factory import *
from logger import log

from config import *
from consts import LETTERS, NUMBERS
from errors import *

class Board(SquareManager):
	def __init__(self, size):
		SquareManager.__init__(self)
		if size > len(LETTERS):
			raise BoardError("Board size %s exceeds letter's range" % size)
		self.letters = LETTERS[:size]
		self.numbers = NUMBERS[:size]
		# Init all squares
		for l in self.letters:
			for n in self.numbers:
				name = l + n
				x = self.letters.index(l)
				y = self.numbers.index(n)
				self.createSquare(name, x, y)

	def getSquare(self, pos):
		if pos in self.squares:
			return self.squares[pos]
		try:
			# Convert square name to coord
			x, y = pos
			pos = self.letters[x] + self.numbers[y] 
		except:
			PositionError("Wrong position %s" % pos)
		if pos in self.squares:
			return self.squares[pos]
		raise PositionError("Wrong position %s" % pos)

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
			piece_id = pname[0]
			square_name = pname[1:]
			piece_config = PIECES[piece_id]
			piece = self.pm.createPiece(piece_config["name"])
			movement = self.mm.getMovement(piece_config["movement"])
			color = self.cm.getColor(piece_config["color"])
			square = self.bd.getSquare(square_name)
			piece.id = piece_id
			self.setPiece(piece, square, color, movement)

	def getPosition(self):
		pos = str()
		for piece in self.pm.pieces:
			pos += piece.id
			pos += piece.square.name
		return pos

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
				continue
			if s.piece and s.piece.color == piece.color:
				continue
			yield s
