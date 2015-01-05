import logging
import string
from obj import *

log = logging.getLogger("chesslib")
log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

class PositionError(Exception):
	pass

class BoardError(Exception):
	pass

class GameError(Exception):
	pass

class Board(object):
	def __init__(self, size):
		#FIXME Set color as a separate object
		self.info = dict()
		self.info["squares"] = dict()
		self.info["pieces"] = dict()
		self.letters = list(string.ascii_lowercase)
		letters_range = len(self.letters)
		if size > letters_range:
			raise BoardError("Board size %s exceeds letter's range %s" % (size, letters_range))
		self.numbers = map(str, range(1, letters_range + 1))
		self.letters = self.letters[:size]
		self.numbers = self.numbers[:size]

	def _check_pos_value(self, pos):
		# Check that position value is correct. For example, "e4" or (4, 3)
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

	def getSquare(self, pos, error = True):
		try:
			self._check_pos_value(pos)
		except PositionError:
			if error:
				raise
			else:
				return None
		if type(pos) == str:
			name = pos
			x = self.letters.index(pos[0])
			y = self.numbers.index(pos[1])
		else:
			x, y = pos
			name = self.letters[x] + self.numbers[y]
		if self.info["squares"].get((x, y)) is None:
			log.debug("Get new square %s" % name)
			square = Square(name, x, y)
			self.info["squares"][(x, y)] = square
		return self.info["squares"][(x, y)]

	def getPiece(self, name, color):
		if name == "Bishop":
			return Bishop(name, color)

	def setPiece(self, pos, name, color):
		square = self.getSquare(pos)
		if square.piece is not None:
			raise GameError("Pos %s is already busy with %s %s" % square.piece.info)
		piece = self.getPiece(name, color)
		log.debug("Set new piece %s on %s" % (piece, square))
		square.piece = piece
		piece.callbacksChangeSquare = self._movePiece
		self.info["pieces"][(square.x, square.y)] = piece

	def _movePiece(self, square1, square2):
		"""
		Change piece location in board info.
		Does not change objects
		"""
		log.debug("Move piece from %s to %s" % (square1, square2))
		pos1 = square1.x, square1.y
		pos2 = square2.x, square2.y
		self.info["pieces"][pos2] = self.info["pieces"][pos1]
		del self.info["pieces"][pos1]

if __name__ == "__main__":
	b = Board(8)
	s1 = b.getSquare("b4")
	b.setPiece("a3", "Bishop", "Black")
	s2 = b.getSquare((0, 2))
	pawn = s2.piece
	pawn.square = s1
	s3 = b.getSquare("g2")
	s3.piece = pawn
	pawn.square = s2
	s4 = b.getSquare("h5")
	pawn.square = s4
	log.debug("=== Moves ===")
	for m in pawn.getMoves(observe = lambda x, y: b.getSquare((x, y), error = False)):
		log.debug(m)

	for obj_type in b.info:
		log.debug("=== %s ===" % obj_type)
		for obj_place in b.info[obj_type]:
			log.debug(b.info[obj_type][obj_place])
