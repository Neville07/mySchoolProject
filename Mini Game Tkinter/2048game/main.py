import tkinter as tk
import sys
import time
import random
import os
import pygame
from tkinter import messagebox as Msg

from config import Config
from game_stat import GameStats
from board import Board
from ship import Ship
from player import Player
from menu_page import MenuPage
from pause import Pause

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config #Batteship

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)
		self.resizable(0,0)

		photo = tk.PhotoImage(file="img/2048.PNG")

		self.iconphoto(False, photo)
		self.create_container()


		self.create_container()

		self.pages = {}

		self.create_pause()
		self.create_board()
		self.create_menu_page()
				
	def create_container(self):
		self.containter = tk.Frame(self, bg="#92877d")
		self.containter.pack(fill="both", expand=True)

	def create_menu_page(self):
		self.pages['menu_page'] = MenuPage(self.containter, self.game)

	def create_board(self):
		self.pages['board'] = Board(self.containter, self.game)

	def create_pause(self):
		self.pages['pause'] = Pause(self.containter, self.game)

class Game2048:

	def __init__(self):
		pygame.mixer.init()
		self.grid_cell = []
		self.game_stat = GameStats()
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

		self.gerak = False
		self.gabung = False
		self.check_gabung = False
		self.play = True
		self.score = 0
		
	def key_pressed(self, event): #check_event
		key_value = event.keysym

		if key_value in self.config.up_keys:
			self.up()
		elif key_value in self.config.down_keys:
			self.down()
		elif key_value in self.config.left_keys:
			self.left()
		elif key_value in self.config.right_keys:
			self.right()
		else:
			pass

		self.check_win_lose()

		self.window.pages['board'].paint_grid
		
	def left(self):
		# print("left")
		self.stack()
		self.combine()
		self.add_new_cells()
		self.stack()
		self.update()

	def right(self):
		# print("right")
		self.reverse()
		self.stack()
		self.combine()
		self.add_new_cells()
		self.stack()
		self.reverse()
		self.update()

	def up(self):
		# print("up")
		self.transpose()
		self.stack()
		self.combine()
		self.check_win_lose()
		self.add_new_cells()
		self.stack()
		self.transpose()
		self.update()
		self.check_win_lose()

	def down(self):
		# print("down")
		self.transpose()
		self.reverse()
		self.stack()
		self.combine()
		self.add_new_cells()
		self.stack()
		self.reverse()
		self.transpose()
		self.update()

	def stack(self): #geser semua ke kiri
		self.gerak= False
		new_grid = []
		nRow, nColumn = self.config.row, self.config.column

		for i in range(4):
			cell =[0]*4
			new_grid.append(cell)

		for i in range(4):
			cnt = 0
			for j in range(4):
				if self.grid_cell[i][j] !=0:
					new_grid[i][cnt] = self.grid_cell[i][j]
					self.play = True
					# print(f"c ={cnt}, j = {j}")
					if cnt != j:
						self.gerak = True
						self.play = True
					cnt += 1
		self.grid_cell = new_grid

	def combine(self):
		self.gabung = False
		for i in range(4):
			for j in range(3):
				if self.grid_cell[i][j] != 0 and self.grid_cell[i][j] == self.grid_cell[i][j+1]:
					self.grid_cell[i][j] *= 2
					self.grid_cell[i][j+1] = 0
					self.score += self.grid_cell[i][j]
					self.gabung = True

	def reverse(self): # cermin
		self.play = True
		for i in range(4):
			start = 0
			end = 3
			while start < end:
				self.grid_cell[i][start], self.grid_cell[i][end] = self.grid_cell[i][end], self.grid_cell[i][start]
				start += 1
				end -= 1

	def transpose(self): #i jadi j, j jadi i
		self.play = True
		new_matrix = [[0]*4 for x in range(4)]

		for i in range(4):
			for j in range(4):
				new_matrix[i][j] = self.grid_cell[j][i]
		self.grid_cell = new_matrix

	def add_new_cells(self): # add new random 2 /4
		# print(self.gabung, self.gerak)
		if self.gabung == True or self.gerak == True:
			cell = []

			for i in range(4):
				for j in range(4):
					if self.grid_cell[i][j] == 0 :
						tmp = [i,j]
						cell.append(tmp)
			rndm = random.choice(cell)
			i = rndm[0]
			j = rndm[1]
			self.grid_cell[i][j] = random.choice([2,4])

	def update(self): # tampil di board
		for i in range(4):
			for j in range(4):
				cell = self.grid_cell[i][j]
				if cell == 0:
					self.window.pages['board'].label_board[i][j].configure(text = " ", bg = '#9e948a')
				else:
					self.window.pages['board'].label_board[i][j].configure(text = str(self.grid_cell[i][j]), bg = self.config.cell_bg.get(str(self.grid_cell[i][j])), fg = self.config.cell_color.get(str(self.grid_cell[i][j])))
		self.window.pages['board'].score_label.configure(text = f"Score : {self.score}")
		self.window.update_idletasks()

	def check_play(self):
		self.check_gabung = False
		self.play = False
		for i in range(4):
			for j in range(3):
				if  self.grid_cell[i][j] == self.grid_cell[i][j+1]:
					self.check_gabung = True

		for i in range(3):
			for j in range(4):
				if  self.grid_cell[i][j] == self.grid_cell[i+1][j]:
					self.check_gabung = True

		for i in range(4):
			for j in range(4):
				if self.grid_cell[i][j] == 0 :
					self.play = True

	def check_win_lose(self):
		self.check_play()

		if self.check_gabung == False and self.play == False:
			print("LOSE")
			Msg.showinfo("2048", "Game Over !!!")


		for i in range(4):
			for j in range(4):
				if self.grid_cell[i][j] == 2048:
					Msg.showinfo("2048", "You Won !!!")
					break

	def play_song(self):
		pygame.mixer.music.load("mp3/Ato.m4a")
		pygame.mixer.music.set_volume(0.2)
		pygame.mixer.music.play(-1, 0.0)

	def button_effect(self):
		button = pygame.mixer.Sound("mp3/button effect.wav")
		button.set_volume(0.04)
		button.play()

	def start_page(self, page):
		self.button_effect()
		time.sleep(0.2)
		self.restart('board')
		page = self.window.pages["board"]
		page.tkraise()

	def continue_page(self):
		self.button_effect()
		time.sleep(0.2)
		page = self.window.pages["board"]
		page.tkraise()

	def back_to_menu(self, page):
		self.grid_cell = []
		self.gabung = False
		self.gerak = False
		self.score = 0

		self.window.pages['board'].create_grid_cell()

		self.window.pages['board'].start_game()

		self.update()
		self.button_effect()
		time.sleep(0.2)
		page = self.window.pages["menu_page"]
		page.tkraise()

	def pause(self, page):
		self.button_effect()
		time.sleep(0.2)
		page = self.window.pages["pause"]
		page.tkraise()

	def restart(self, page):
		# self.window.destroy()
		# os.startfile("main.py")

		self.grid_cell = []
		self.gabung = False
		self.gerak = False
		self.score = 0

		self.window.pages['board'].create_grid_cell()

		self.window.pages['board'].start_game()

		self.update()

		self.button_effect()
		time.sleep(0.2)

		page = self.window.pages['board']
		page.tkraise()

	def run(self):
		self.play_song()
		self.window.bind('<Key>', self.key_pressed)
		self.window.mainloop()

if __name__ == '__main__':
	game = Game2048()
	game.run()