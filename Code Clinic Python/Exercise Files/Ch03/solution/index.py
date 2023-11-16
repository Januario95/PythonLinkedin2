from time import time
from tkinter import *
from tkinter import ttk, messagebox
from itertools import permutations


class Queens():
	def __init__(self, master):
		self.n = 8
		self.queens = (0 for i in range(self.n))
		self.index = 0
		self.solution = []

		self.master = master
		self.master.title('Queens')
		self.master.configure(background='#e1d8b9')
		self.master.minsize(400, 470)
		self.master.resizable(True, True)
		self.master.bind('<Configure>', lambda e: self._draw_board())

		self.style = ttk.Style()
		self.style.configure('TFrame', background='#e1d8b9')
		self.style.configure('TButton', background='#e1d8b9')
		self.style.configure('TLabel', background='#e1d8b9')

		self.board_canvas = Canvas(self.master)
		self.board_canvas.pack()

		self.controls_frame = ttk.Frame(self.master)
		self.controls_frame.pack(side=TOP, pady=10)

		ttk.Label(self.controls_frame, text='Number of Queens',
				 font='Verdana 10 bold').grid(row=0, column=0)
		self.n_var = StringVar()
		self.n_var.set(self.n)
		Spinbox(self.controls_frame, from_=4, to=99, width=2,
				font='Verdana 10 bold', textvariable=self.n_var).grid(row=0, column=1)
		tkk.Button(self.controls_frame, text='Get Next Solution',
				   command=self.)

	def _draw_board(self):
		maxboardsize = min(self.master.winfo_width(), self.master.winfo_height() - 70)
		cellsize = maxboardsize // self.n
		self.board_canvas.config(height=self.n*cellsize, width=self.n*cellsize)
		self.board_canvas.delete('all')

def main():
	root = Tk()
	gui = Queens(root)
	root.mainloop()


if __name__=='__main__':
	main()


