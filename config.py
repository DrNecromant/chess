### Images ###
b_image = """
R0lGODlhPAA8APUwAAAAAAEBAQICAgQEBAYGBggICA4ODhMTExcXFx4eHh8fHyAgICYmJjo6Ojw8PEJCQktLS1FRUVNTU1dXV1hYWFxcXGBgYHNzc3R0dHV1dXZ2dnd3d3t7e4mJiZWVlaCgoKampqioq
KysrLe3t7m5udra2t/f3+Dg4Onp6ezs7PT09Pb29vf39/j4+Pz8/P7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAADEALAAAAAA8ADwAAAb+wJhwSC
waj8ikcslsOp/QqHRKrVqv2Kx2y+02AWCANxsOj63l8pmaNq+lbfAbHp/T0/ZoOw+Ny/lKfmqAR4J4hESGdYiKfoSCHSMCjnyGJjAKgpWCJzALhnZxARkfHyowIh8eBotvcQcuMLKzMBKta34OFhYpMBg
WEJO3Y4qdn6CuhiUwCYpzihEcAc7JjdS41sjV2cNn3JSh34N5YA0oLejp6ugrF3+AAA+xtPSyLxtijAADBf3+//0IuNkkLh/BgnwqgAjBsKHDhw418CFRr2JFFnwQTKDAsaPHjx4ZHERIruDAkuIQCcmm
soi1bSa5sYkZ8w7Nmk5u6jS45OYTSpp9Tno51LKo0aNIkypdynRIEAA7
"""

### Colors ###
White = "White"
Black = "Black"

### Pieces ###
Bishop = "Bishop"
Rook = "Rook"

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
		"name": Bishop,
		"movement": BM,
		"color": White
	},
	"R": {
		"name": Rook,
		"movement": RM,
		"color": White
	},
	"b": {
		"name": Bishop,
		"movement": BM,
		"color": Black,
		"image": b_image
	},
	"r": {
		"name": Rook,
		"movement": RM,
		"color": Black
	},
}
