import tkinter as tk
from PIL import Image, ImageTk
import random
import sys
class Pause(tk.Frame):

	def __init__(self,parent, Game):
		self.game = Game
		self.config = Game.config
		self.row = self.config.row
		self.column = self.config.column

		#CONFIG FRAME
		super().__init__(parent) #parent -> container di Game
		self.configure(bg="#92877d")
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.virtual_image = tk.PhotoImage(width = 1, height = 1)

		self.create_button()

	def create_button(self):
		frame_h = self.config.height//2
		self.button_frame = tk.Frame(self, bg = "#92877d", width = self.config.width, height = frame_h)
		self.button_frame.pack(fill = "x")

		self.continue_button_frame = tk.Frame(self.button_frame, bg = "#92877d", width = self.config.width, height = frame_h//3)
		self.continue_button_frame.pack()

		self.continue_button = tk.Button(self.continue_button_frame, text = "CONTINUE",  bg = "#dbd956", fg = "white", font = ("Comic Sans MS", 12), width = 13, bd=0, command=self.game.continue_page)
		self.continue_button.grid(sticky="nsew", padx=20, pady=(150, 30))

		self.restart_button_frame = tk.Frame(self.button_frame, bg = "#92877d", width = self.config.width, height = frame_h//3)
		self.restart_button_frame.pack()

		self.restart_button = tk.Button(self.restart_button_frame, text = "RESTART",  bg = "#dbd956", fg = "white", font = ("Comic Sans MS", 12), width = 13, bd=0, command=lambda:self.game.restart("board"))
		self.restart_button.grid(row = 0, column = 0, sticky="nsew", padx=20, pady=(0, 30))

		self.back_button_frame = tk.Frame(self.button_frame, bg = "#92877d", width = self.config.width, height = frame_h//3)
		self.back_button_frame.pack()

		self.back_button = tk.Button(self.back_button_frame, text = "BACK TO MENU",  bg = "#dbd956", fg = "white", font = ("Comic Sans MS", 12), width = 13, bd=0, command= lambda:self.game.back_to_menu("back"))
		self.back_button.grid(row = 0, column = 0, sticky="nsew", padx=20, pady=(0, 30))