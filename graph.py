import Tkinter as tk

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=64, color1="white", color2="gray"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

def drawBoard(position):
	root = tk.Tk()
	board = GameBoard(root)
	board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
	imagedata = """
R0lGODlhPAA8APUwAAAAAAEBAQICAgQEBAYGBggICA4ODhMTExcXFx4eHh8fHyAgICYmJjo
6Ojw8PEJCQktLS1FRUVNTU1dXV1hYWFxcXGBgYHNzc3R0dHV1dXZ2dnd3d3t7e4mJiZWVla
CgoKampqioqKysrLe3t7m5udra2t/f3+Dg4Onp6ezs7PT09Pb29vf39/j4+Pz8/P7+/v///
wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAADEA
LAAAAAA8ADwAAAb+wJhwSCwaj8ikcslsOp/QqHRKrVqv2Kx2y+02AWCANxsOj63l8pmaNq+
lbfAbHp/T0/ZoOw+Ny/lKfmqAR4J4hESGdYiKfoSCHSMCjnyGJjAKgpWCJzALhnZxARkfHy
owIh8eBotvcQcuMLKzMBKta34OFhYpMBgWEJO3Y4qdn6CuhiUwCYpzihEcAc7JjdS41sjV2
cNn3JSh34N5YA0oLejp6ugrF3+AAA+xtPSyLxtijAADBf3+//0IuNkkLh/BgnwqgAjBsKHD
hw418CFRr2JFFnwQTKDAsaPHjx4ZHERIruDAkuIQCcmmsoi1bSa5sYkZ8w7Nmk5u6jS45OY
TSpp9Tno51LKo0aNIkypdynRIEAA7
"""
	image = tk.PhotoImage(data = imagedata)
	board.addpiece("smile1", image, 1,1)
	board.addpiece("smile2", image, 2,2)
	root.mainloop()
