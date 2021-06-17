import json

class Settings:

	def __init__(self):

		#App Conf
		self.title = "Hotel Management"


		#Window Conf
		base = 50
		ratio = (16, 10)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+250+50"
		self.guest = []

		self.logo_path = "img/profile.png"
		self.admin = []
		
		# display
		self.font = ''
		self.color_theme = ''
		self.shadow = ''
		self.mode = ''
		self.board_color = ''
		self.board_shadow = ''
		self.font_color = ''
		self.back_img = ''
		self.download_img = ''
		self.menu_img = ''
		self.close_img = ''
		self.ok_img = ''
		self.color_tmp = ''

		print(self.close_img)

		self.font_size()
		self.mode_config()


		# self.blue = "#12a4ff" #0090eb
		# self.orange = "#f07b52"
		self.load_data()
		self.load_admin()

	def mode_config(self):
		if self.mode == 'day':
			self.board_color = '#f5f5f5'
			self.board_shadow = '#e7e7e7'
			self.font_color = 'black'
			self.back_img = 'img/back_day.png'
			self.download_img = 'img/download_day.png'
			self.menu_img = 'img/menu_day.png'
			self.close_img = 'img/close_day.png'
			self.ok_img = 'img/ok_day.png'
		elif self.mode == 'night':
			self.board_color = '#1a1a1a'
			self.board_shadow = '#0d0d0d'
			self.font_color = '#f5f5f5'
			self.back_img = 'img/back_night.png'
			self.download_img = 'img/download_night.png'
			self.menu_img = 'img/menu_night.png'
			self.close_img = 'img/close_night.png'
			self.ok_img = 'img/ok_night.png'

	def font_size(self):
		if self.font == 'medium':
			self.font_default()
		elif self.font == 'small':
			self.font_small()
		elif self.font == 'large':
			self.font_large()

	def font_default(self):
		self.option_font_size = 13
		self.content_font_size = 12
		self.apppage_header_font_size = 24
		self.header_font_size = 40
		self.sub_header_login_size = 16
		self.user_font_size = 15
		self.info_font_size = 11

		self.font_style()
		print('aaym')

	def font_small(self):
		print('ok')
		self.option_font_size = 10
		self.content_font_size = 9
		self.apppage_header_font_size = 21
		self.header_font_size = 37
		self.sub_header_login_size = 13
		self.user_font_size = 12
		self.info_font_size = 9

		self.font_style()

	def font_large(self):
		print('awa')
		self.option_font_size = 16
		self.content_font_size = 15
		self.apppage_header_font_size = 26
		self.header_font_size = 43
		self.sub_header_login_size= 19
		self.user_font_size = 18
		self.info_font_size = 14

		self.font_style()
		
	def font_style(self):
		self.option_font = ("Cambira", self.option_font_size, "bold")
		self.content_font = ("Cambira", self.content_font_size, "bold")
		self.apppage_header_font = ("Cambira", self.apppage_header_font_size , "bold")
		self.header_font = ("Arial", self.header_font_size, "bold")
		self.sub_header_login = ("Cambira", self.sub_header_login_size)
		self.user_font = ("Cambira", self.user_font_size, "bold")
		self.status_font =("cambira", self.option_font_size)
		self.info_font = ("cambira", self.info_font_size)

	def shadow_color(self):
		value = self.color_theme.lstrip('#')
		lv = len(value)
		rgb = tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
		r = rgb[0] - 30
		g = rgb[1] - 15
		b = rgb[2] - 10

		if r < 0:
			r = 0
		if g < 0:
			g = 0
		if b < 0:
			b = 0

		new_rgb = (r,g,b)
		shadow = '%02x%02x%02x' % new_rgb
		self.shadow = '#' + shadow


	def save_data(self):
		with open('data/guest.json', 'w') as f:
			json.dump(self.guest, f)

	def load_data(self):
		with open('data/guest.json', 'r') as f:
			self.guest = json.load(f)

	def save_admin(self):
		with open('data/admin.json', 'w') as admin:
			json.dump(self.admin, admin)

	def load_admin(self):
		with open('data/admin.json', 'r') as admin:
			self.admin = json.load(admin)
