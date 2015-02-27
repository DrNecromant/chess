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

Composition = {
	White: [
		{
			"name": B,
			"movement": BM,
			"squares": ("c1", "f1")
		},
		{
			"name": R,
			"movement": RM,
			"squares": ("a1", "h1")
		}
	],
	Black: [
		{
			"name": B,
			"movement": BM,
			"squares": ("c8", "f8")
		},
		{
			"name": R,
			"movement": RM,
			"squares": ("a8", "h8")
		}
	]
}
