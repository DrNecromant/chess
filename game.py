from factory import *
from logger import log

if __name__ == "__main__":
	b = Board(8)
	pm = PieceManager()
	cm = ColorManager()
	mm = MovementManager()

	s1 = b.getSquare("b4")
	s2 = b.getSquare((0, 2))
	s3 = b.getSquare("g2")
	s4 = b.getSquare("c3")

	p1 = pm.createPiece("Bishop")
	p2 = pm.createPiece("Bishop")
	p3 = pm.createPiece("Bishop")

	black = cm.getColor("Black")
	white = cm.getColor("White")
	move = mm.getMovement("move")

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

	move.directions = set([(1, 1), (1, -1), (-1, 1), (-1, -1)])
	move.observe = b.observeSquare
	move.piece = p1
	p2.movement = move
	p3.movement = move

	moves1 = list(p1.getMoves())
	moves2 = list(p2.getMoves())
	moves3 = list(p3.getMoves())

	log.debug("=== squares ===")
	binfo = b.info
	for k in binfo:
		s = binfo[k]
		log.debug("%s %s %s %s" % (k, s.x, s.y, s.piece))
	log.debug("=== pieces ===")
	for p in pm.info:
		log.debug(p)
	log.debug("=== colors ===")
	cinfo = cm.info
	for c in cinfo:
		log.debug("%s %s" % (c, cinfo[c]))
	log.debug("=== moves ===")
	log.debug("Move for %s: %s" % (p1, map(str, moves1)))
	log.debug("Move for %s: %s" % (p2, map(str, moves2)))
	log.debug("Move for %s: %s" % (p3, map(str, moves3)))
