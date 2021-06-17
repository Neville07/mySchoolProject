import pygame
class Settings():

	def __init__(self):
		#setting game
		self.screen_width = 800
		self.screen_height = 600
		self.title = "*Alien Game*"
		self.bg_image = pygame.image.load("img/galaxy.JPG") 
		self.bg_images = pygame.image.load("img/moons.PNG")

		#Setting ship
		#self.ship_speed = 1.0
		self.ship_life = 5
		self.rocket_speed = 5.0
		#setting bullet
		#self.bullet_speed = 1.5
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = (255, 255, 255)
		self.bullets_limit = 5

		#setting alien
		#self.alien_speed = 1.0
		self.alien_army_drop_speed = 1.0
		#self.alien_army_direction = 1 # 1 right, -1 left


		#scaling level
		self.speedup_level = 2.0
		self.score_scale = 2.0

		self.init_dynamic_setting()

	def init_dynamic_setting (self):
		self.ship_speed = 1.5
		self.bullet_speed = 1.0
		self.alien_speed = 1.0
		self.alien_points = 50

		self.alien_army_direction = 1

	def increase_speed(self):
		self.ship_speed *= self.speedup_level
		self.bullet_speed *= self.speedup_level
		self.alien_speed *= self.speedup_level

		self.alien_points *= self.score_scale
