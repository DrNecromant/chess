import Tkinter as tk
from config import PIECES
from consts import *
from time import sleep

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

    def addpiece(self, name, image, column=0, row=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, column, row)

    def placepiece(self, name, column, row):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (column, row)
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

def drawBoard(pos):
	root = tk.Tk()
	w = 64 * 8
	h = 64 * 8
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))
	board = GameBoard(root)
	board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
	images = dict()
	for pname in [pos[i:i+3] for i in range(0, len(pos), 3)]:
		piece_id = pname[0]
		x = LETTERS.index(pname[1])
		y = 7 - NUMBERS.index(pname[2])
		images[pname] = tk.PhotoImage(data = PIECES[piece_id]["image"])
		board.addpiece(pname, images[pname], x, y)
	root.mainloop()
