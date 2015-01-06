from factory import *
from logger import log

if __name__ == "__main__":
	b = Board(8)
	pm = PieceManager()
	s1 = b.getSquare("b4")
	s2 = b.getSquare((0, 2))
	piece = pm.createPiece("Bishop", "Black")
	s2.piece = piece
	piece.square = s1
	s3 = b.getSquare("g2")
	s3.piece = piece
	piece.square = s2
	s4 = b.getSquare("h5")
	piece.square = s4
	log.debug("=== Moves ===")
	def observe(x ,y):
		try:
			s = b.getSquare((x, y))
		except Exception, e:
			print str(e)
			s = None
		return s
			
	for m in piece.getMoves(observe = observe):
		log.debug(m)

	log.debug("=== squares ===")
	binfo = b.info
	for k in binfo:
		log.debug("%s %s %s" % (k, binfo[k].x, binfo[k].y))
	log.debug("=== pieces ===")
	for p in pm.info:
		log.debug("%s %s %s" % (p.square, p.name, p.color))
