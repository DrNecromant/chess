from factory import *
from logger import log

class Game(object):
	def __init__(self):
		self.bd = Board(8)
		self.pm = PieceManager()
		self.cm = ColorManager()
		self.mm = MovementManager()

if __name__ == "__main__":
	g = Game()

	s1 = g.bd.getSquare("b4")
	s2 = g.bd.getSquare((0, 2))
	s3 = g.bd.getSquare("g2")
	s4 = g.bd.getSquare("c3")

	p1 = g.pm.createPiece("Bishop")
	p2 = g.pm.createPiece("Bishop")
	p3 = g.pm.createPiece("Bishop")

	black = g.cm.getColor("Black")
	white = g.cm.getColor("White")
	move = g.mm.getMovement("move", directions = set([(1, 1), (1, -1), (-1, 1), (-1, -1)]), steps = set())

	p1.color = black
	s2.piece = p1
	p1.square = s1
	s3.piece = p1
	p1.square = s2

	p2.color = white
	p2.square = s4

	p3.color = white
	p3.square = s1
	p1.square = s1

	move.piece = p1
	p2.movement = move
	p3.movement = move

	moves1 = list(g.bd.getMoves(p1))
	moves2 = list(g.bd.getMoves(p2))
	moves3 = list(g.bd.getMoves(p3))

	log.debug("=== squares ===")
	bdinfo = g.bd.info
	for k in bdinfo:
		s = bdinfo[k]
		log.debug("%s %s %s %s" % (k, s.x, s.y, s.piece))
	log.debug("=== pieces ===")
	for p in g.pm.info:
		log.debug(p)
	log.debug("=== pieces_del ===")
	for p in g.pm.info_del:
		log.debug(p)
	log.debug("=== colors ===")
	cminfo = g.cm.info
	for c in cminfo:
		log.debug("%s %s" % (c, cminfo[c]))
	log.debug("=== moves ===")
	log.debug("Move for %s: %s" % (p1, map(str, moves1)))
	log.debug("Move for %s: %s" % (p2, map(str, moves2)))
	log.debug("Move for %s: %s" % (p3, map(str, moves3)))
