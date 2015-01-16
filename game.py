from factory import *
from logger import log

if __name__ == "__main__":
	b = Board(8)
	pm = PieceManager()
	cm = ColorManager()

	s1 = b.getSquare("b4")
	s2 = b.getSquare((0, 2))
	s3 = b.getSquare("g2")
	s4 = b.getSquare("h5")

	p1 = pm.createPiece("Bishop")
	p2 = pm.createPiece("Bishop")

	black = cm.getColor("Black")
	white = cm.getColor("White")

	p1.color = black
	s2.piece = p1
	p1.square = s1
	s3.piece = p1
	p1.square = s2

	p2.color = white
	p2.square = s4

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
