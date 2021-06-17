import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox as Msg
import random

class Board(tk.Frame):

	def __init__(self, parent, Game):

		self.game = Game
		self.config = Game.config # config di Battleship
		self.row = self.config.row
		self.column = self.config.column
		self.grid_cell = []
		# print(self.grid_cell)

		#CONFIG FRAME
		super().__init__(parent) #parent -> container di Game
		self.configure(bg="#92877d")
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)


		# self.img_virtual = tk.PhotoImage(width=1, height=1)

		# create board
		self.create_main_frame()
		self.create_header()
		self.create_board()
		self.show_board()
		self.create_label_board()
		self.show_label_board()
		self.create_grid_cell()
		

		# game
		self.start_game()
		
	def start_game(self):
		self.random_sel()
		self.random_sel()
		self.paint_grid()

	def create_grid_cell(self): # create list yg isiny dgn angka di box
		self.grid_cell = self.game.grid_cell

		for i in range(4):
			cell =[0]*4
			self.grid_cell.append(cell)

	def create_main_frame(self):
		self.main_frame = tk.Frame(self, height=self.config.height, width=self.config.width, bg="#92877d")
		self.main_frame.pack(expand=True)

		self.main_frame.grid_columnconfigure(0, weight = 1)
		self.main_frame.grid_rowconfigure(0, weight = 1)

	def create_header(self):
		frame_h = self.config.height//7
		self.header_frame = tk.Frame(self.main_frame, height=frame_h, width=self.config.width, bg="#92877d")
		self.header_frame.pack(fill = 'x')

		self.pause_frame = tk.Frame(self.header_frame, height=frame_h , width=self.config.width//7, bg="#92877d")
		self.pause_frame.pack(side = "left")

		self.pause_frame_ = tk.Frame(self.header_frame, height=frame_h, width=self.config.width//7, bg="#92877d")
		self.pause_frame_.pack(side = "right")

		self.pause_button_img = tk.PhotoImage(file="img/pause.PNG")
		image = Image.open("img/pause.PNG")
		image_w, image_h = image.size
		ratio = 1.3
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.pause_button_img = ImageTk.PhotoImage(image)

		
		self.pause_button = tk.Button(self.pause_frame, image =self.pause_button_img , bd=0, bg="#92877d", command = lambda:self.game.pause("pause"))
		self.pause_button.grid(column  =0, row = 0)

		self.pause_label_ = tk.Label(self.pause_frame, text = "", bg = '#92877d')
		self.pause_label_.grid(column = 0, row = 1)

		self.score_frame = tk.Frame(self.header_frame, height=frame_h, bg="#92877d")
		self.score_frame.pack(expand = True, fill = 'x')

		self.score_label = tk.Label(self.score_frame, text = "score : 0", bg = "#92877d", fg = "#edc22e", font = ("Comic Sans MS", 27, 'bold'))
		self.score_label.pack(padx = 5)

		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

	def create_board(self):
		self.frame_rows = []
		# colors = ["#92877d"]

		nRow, nColumn = self.config.row, self.config.column
		row_height, row_width = self.config.height//nRow, self.config.width

		for i in range(nRow):
			frame = tk.Frame(self.main_frame, height = row_height, width = row_width, bg = "#92877d")
			self.frame_rows.append(frame)

	def show_board(self):
		for frame in self.frame_rows:
			frame.pack()

	def create_label_board(self):
		self.label_board = []

		nRow, nColumn = self.config.row, self.config.column
		button_height, button_width = self.config.height//nRow, self.config.width// nColumn

		for i in range(nRow):
			row = []

			for j in range(nColumn):
				button = tk.Label(self.frame_rows[i], bg = "#9e948a", justify = tk.CENTER, font = ('Verdana', 24, 'bold'), width = 4, height = 2)
				
				row.append(button)

			self.label_board.append(row)

	def show_label_board(self):
		nRow, nColumn = self.config.row, self.config.column


		for i in range(nRow):
			for j in range(nColumn):
				self.label_board[i][j].grid(row = i, column = j, padx = 10, pady = 10)

	def random_sel(self): # random 2
		cell = []

		for i in range(4):
			for j in range(4):
				if self.grid_cell[i][j] == 0 :
					tmp = [i,j]
					cell.append(tmp)
		rndm = random.choice(cell)
		i = rndm[0]
		j = rndm[1]
		self.grid_cell[i][j] = 2

	def paint_grid(self): # create grid sesuai angka & warna
		for i in range(4):
			for j in range(4):
				if self.grid_cell[i][j] == 0:
					self.label_board[i][j].configure(text = " ", bg = '#9e948a')
				else:
					self.label_board[i][j].configure(text = str(self.grid_cell[i][j]), bg = self.config.cell_bg.get(str(self.grid_cell[i][j])), fg = self.config.cell_color.get(str(self.grid_cell[i][j])))
