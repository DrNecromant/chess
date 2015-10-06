from rules import Board, Game
from logger import log

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
log.debug("=== position ===")
log.debug(g.getPosition())
