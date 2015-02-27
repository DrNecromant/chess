from factory import *
from logger import log

from config import *

class Game(object):
	def __init__(self, composition):
		self.bd = Board(8)
		self.pm = PieceManager()
		self.cm = ColorManager()
		self.mm = MovementManager()
		self.setComposition(composition)

	def setComposition(self, com):
		for cname in com:
			for pconf in com[cname]:
				color = self.cm.getColor(cname)
				mconf = pconf["movement"]
				movement = self.mm.getMovement(mconf)
				for sname in pconf["squares"]:
					piece = self.pm.createPiece(pconf["name"])
					square = self.bd.getSquare(sname)
					self.setPiece(piece, square, color, movement)

	def setPiece(self, piece, square, color, movement):
		piece.square = square
		piece.color = color
		piece.movement = movement
		square.piece = piece
		color.piece = piece
		movement.piece = piece

	def movePiece(self, piece, square):
		# Make the old square is empty
		piece.square.piece = None
		if square.piece:
			# remove piece from new square
			self.pm.removePiece(square.piece)
		square.piece = piece
		piece.square = square

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
	g = Game(Composition)

	log.debug("=== squares ===")
	bdinfo = g.bd.info
	for l in g.bd.letters:
		for n in g.bd.numbers:
			k = l + n
			s = bdinfo[k]
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
