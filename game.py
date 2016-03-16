from rules import Board, Game
from graph import drawBoard
from logger import log

POS = "ke1Ke8ra1rh1Ra8Rh8bc1bf1Bc8Bf8nb1ng1Nb8Ng8qd1Qd8pa2pb2pc2pd2pe2pf2pg2ph2Pa7Pb7Pc7Pd7Pe7Pf7Pg7Ph7"

g = Game(8)
g.setPosition(POS)

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
log.debug("=== position ===")
log.debug(g.getPosition())

drawBoard(POS)
