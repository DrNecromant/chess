from factory import *
from logger import log

if __name__ == "__main__":
	b = Board(8)
	pm = PieceManager()
	cm = ColorManager()

	s1 = b.getSquare("b4")
	s2 = b.getSquare((0, 2))

	piece1 = pm.createPiece("Bishop")
	black = cm.getColor("Black")
	s2.piece = piece1
	piece1.color = black
	piece1.square = s1
	s3 = b.getSquare("g2")
	s3.piece = piece1
	piece1.square = s2

	s4 = b.getSquare("h5")
	piece2 = pm.createPiece("Bishop")
	white = cm.getColor("White")
	piece2.color = white
	piece2.square = s4

	log.debug("=== squares ===")
	binfo = b.info
	for k in binfo:
		log.debug("%s %s %s" % (k, binfo[k].x, binfo[k].y))
	log.debug("=== pieces ===")
	for p in pm.info:
		log.debug(p)
	log.debug("=== colors ===")
	cinfo = cm.info
	for c in cinfo:
		log.debug("%s %s" % (c, cinfo[c]))
