from images import *

### Colors ###
White = "White"
Black = "Black"

### Pieces ###
King = "King"
Queen = "Queen"
Bishop = "Bishop"
Knight = "Knight"
Rook = "Rook"
Pawn = "Pawn"

### Movements  ###
KM = {
	"name": "KingMove",
	"directions": set(),
	"steps": set([(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)])
}
QM = {
	"name": "QueenMove",
	"directions": set([(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]),
	"steps": set()
}
BM = {
	"name": "BishopMove",
	"directions": set([(1, 1), (1, -1), (-1, 1), (-1, -1)]),
	"steps": set()
}
NM = {
	"name": "KnightMove",
	"directions": set(),
	"steps": set([(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)])
}
RM = {
	"name": "RookMove",
	"directions": set([(1, 0), (0, 1), (-1, 0), (0, -1)]),
	"steps": set()
}
PM = {
	"name": "PawnMove",
	"directions": set(),
	"steps": set()
}

PIECES = {
	"k": {"name": King, "movement": KM, "color": White, "image": k_image},
	"K": {"name": King, "movement": KM, "color": Black, "image": K_image},
	"q": {"name": Queen, "movement": QM, "color": White, "image": q_image},
	"Q": {"name": Queen, "movement": QM, "color": Black, "image": Q_image},
	"b": {"name": Bishop, "movement": BM, "color": White, "image": b_image},
	"B": {"name": Bishop, "movement": BM, "color": Black, "image": B_image},
	"n": {"name": Knight, "movement": NM, "color": White, "image": n_image},
	"N": {"name": Knight, "movement": NM, "color": Black, "image": N_image},
	"r": {"name": Rook, "movement": RM, "color": White, "image": r_image},
	"R": {"name": Rook, "movement": RM, "color": Black, "image": R_image},
	"p": {"name": Pawn, "movement": PM, "color": White, "image": p_image},
	"P": {"name": Pawn, "movement": PM, "color": Black, "image": P_image},
}
