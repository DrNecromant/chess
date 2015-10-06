### Colors ###
White = "White"
Black = "Black"

### Pieces ###
B = "Bishop"
R = "Rook"

### Movements  ###
BM = {
	"name": "BishopMove",
	"directions": set([(1, 1), (1, -1), (-1, 1), (-1, -1)]),
	"steps": set()
}
RM = {
	"name": "RookMove",
	"directions": set([(1, 0), (0, 1), (-1, 0), (0, -1)]),
	"steps": set()
}

PIECES = {
	"B": {
		"name": B,
		"movement": BM,
		"color": White
	},
	"R": {
		"name": R,
		"movement": RM,
		"color": White
	},
	"b": {
		"name": B,
		"movement": BM,
		"color": Black
	},
	"r": {
		"name": R,
		"movement": RM,
		"color": Black
	},
}
