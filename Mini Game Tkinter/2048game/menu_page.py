import tkinter as tk
from PIL import Image, ImageTk
import random
import sys
import pygame
import time

class MenuPage(tk.Frame):

	def __init__(self, parent, Game):
		pygame.mixer.init()
		self.game = Game
		self.config = Game.config # config di Battleship
		self.row = self.config.row
		self.column = self.config.column

		#CONFIG FRAME
		super().__init__(parent) #parent -> container di Game
		self.configure(bg="#92877d")
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.virtual_image = tk.PhotoImage(width = 1, height = 1)

		self.create_header()
		self.create_button()

	def create_header(self):
		frame_h = self.config.height//2

		self.header_frame = tk.Frame(self, bg = "#92877d", width = self.config.width, height = frame_h)
		self.header_frame.pack(fill = "x")

		self.header_label = tk.Label(self.header_frame, text = "2048", font = ("Comic Sans MS", 42, "bold"), image = self.virtual_image, compound = 'c', height = frame_h, bg = "#92877d", fg = "#eee4da")
		self.header_label.grid(row = 0, column = 0)

		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

	def quit(self):
		self.game.button_effect()
		time.sleep(0.2)
		sys.exit()

	def create_button(self):
		frame_h = self.config.height//2

		self.button_frame = tk.Frame(self, bg = "#92877d", width = self.config.width, height = frame_h)
		self.button_frame.pack(fill = "x")

		self.start_button_frame = tk.Frame(self.button_frame, bg = "#92877d", width = self.config.width, height = frame_h//2)
		self.start_button_frame.pack()

		self.start_button = tk.Button(self.start_button_frame, text = "START",  bg = "#edc22e", fg = "white", font = ("Comic Sans MS", 12), width = 13, bd=0, command = lambda:self.game.start_page("board"))
		self.start_button.grid(sticky="nsew", padx=20, pady=(10, 10))

		self.quit_button_frame = tk.Frame(self.button_frame, bg = "#92877d", width = self.config.width, height = frame_h//2)
		self.quit_button_frame.pack()

		self.quit_button = tk.Button(self.quit_button_frame, text = "QUIT",  bg = "#edc22e", fg = "white", font = ("Comic Sans MS", 12), width = 13, bd=0, command=quit)
		self.quit_button.grid(row = 0, column = 0, sticky="nsew", padx=20, pady=(10, 10))