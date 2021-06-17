import tkinter as tk
from PIL import Image, ImageTk
import random
import sys
import time

class MenuPage(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings
		self.btn_status = False

		#CONFIG FRAME
		super().__init__(parent) #parent -> container di Game
		self.configure(bg=self.settings.board_color)
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.virtual_image = tk.PhotoImage(width = 1, height = 1)

		self.create_header()
		self.create_button()

	def create_header(self):
		frame_h = self.settings.height//2

		self.header_frame = tk.Frame(self, bg = self.settings.board_color, width = self.settings.width, height = frame_h)
		self.header_frame.pack(fill = "x")

		self.header_label = tk.Label(self.header_frame, text = "Hotel Management System", font = self.settings.header_font, image = self.virtual_image, compound = 'c', height = frame_h, bg = self.settings.board_color, fg = self.settings.font_color,  width = self.settings.width)
		self.header_label.grid(row = 0, column = 0)

		self.create_navbar()

		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

	def create_navbar(self):
		frame_h = self.settings.height//3 + 37

		self.nav_photo = tk.PhotoImage(file=self.settings.menu_img)
		image = Image.open(self.settings.menu_img)
		image_w, image_h = image.size
		new_size = (int(image_w-8), int(image_h-8))
		image = image.resize(new_size)
		self.nav_photo = ImageTk.PhotoImage(image)

		self.navbar_button = tk.Button(self.header_frame, image = self.nav_photo, bg = self.settings.board_color, bd = 0, command = self.navbar_swtitch, activebackground = self.settings.board_color)
		self.navbar_button.place(x = 10, y = 10)

		self.navbar_option_frame = tk.Frame(self, bg = self.settings.board_color, height = 1000, width = self.settings.width//2)
		self.navbar_option_frame.place(x = -self.settings.width//2, y = 0)

		self.admin_info = tk.Frame(self.navbar_option_frame, bg = self.settings.color_theme, height = self.settings.height//3, width = self.settings.width//2)
		self.admin_info.place(x =0, y = 0)

		self.close_photo = tk.PhotoImage(file= self.settings.close_img)
		image = Image.open(self.settings.close_img)
		image_w, image_h = image.size
		new_size = (int(image_w-8), int(image_h-8))
		image = image.resize(new_size)
		self.close_photo = ImageTk.PhotoImage(image)

		self.close_button = tk.Button(self.admin_info, image = self.close_photo, bg = self.settings.color_theme, bd = 0, command = self.navbar_swtitch, activebackground = self.settings.color_theme)
		self.close_button.place(x = self.settings.width//2 - 50, y = 10)

		self.avatar = tk.PhotoImage(file = 'img/profile_icon.png')
		image = Image.open("img/profile_icon.PNG")
		image_w, image_h = image.size
		ratio = 8
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.avatar = ImageTk.PhotoImage(image)

		self.avatar_label = tk.Label(self.admin_info, image = self.avatar, bg = self.settings.color_theme)
		self.avatar_label.place(x = 10, y = 13)


		self.admin_name =tk.Label(self.admin_info, text = self.app.name, bg = self.settings.color_theme, font=self.settings.user_font, fg = self.settings.board_color)
		self.admin_name.place(x = 20, y = 100)

		self.admin_status = tk.Label(self.admin_info, text = self.app.status, bg = self.settings.color_theme, font=self.settings.status_font, fg = self.settings.board_color, height = 1)
		if self.settings.font == 'large':
			self.admin_status.place(x = 25, y = 129)
		elif self.settings.font == 'medium' :
			self.admin_status.place(x = 25, y = 123)
		elif self.settings.font == 'small':
			self.admin_status.place(x = 25, y = 121)

		if self.app.status == 'CEO':
			options = ['Show Guest Info', 'Print Guest Info', 'Settings', 'New Admin', 'Log Out']
			commands = [self.app.show_guest, self.app.print, self.app.setting_page, self.app.new_admin_page, self.app.log_out]
		else:
			options = ['Show Guest Info', 'Print Guest Info', 'Settings', 'Log Out']
			commands = [self.app.show_guest, self.app.print, self.app.setting_page,self.app.log_out]

		self.navbar_option = []
		y = self.settings.height//3 + 35

		for option in options:
			index = options.index(option)
			button = tk.Button(self.navbar_option_frame, text = option, bg = self.settings.board_color, fg = self.settings.font_color, bd= 0, font=self.settings.option_font, command = commands[index], activebackground = self.settings.board_color)
			button.place(x = 15, y = y)

			if self.app.status == 'CEO':
				if option == 'New Admin':
					y+= 85
				else:
					y += 55
			else:
				if option == 'Settings':
					y += 140
				else:
					y += 55

		self.garis = tk.Frame(self.navbar_option_frame, width=self.settings.width//2 - 20, height=3, bg="#ededed").place(x=10,y=self.settings.height-60)
		
	def navbar_swtitch(self):
		if self.btn_status == False:
			self.configure(bg = self.settings.board_shadow)
			self.header_frame.configure(bg = self.settings.board_shadow)
			self.header_label.configure(bg = self.settings.board_shadow, fg = '#404040')
			self.button_frame.configure(bg = self.settings.board_shadow)
			self.check_in_frame.configure(bg = self.settings.board_shadow)
			self.check_out_frame.configure(bg = self.settings.board_shadow)
			self.check_in.configure(bg =self.settings.shadow, fg = self.settings.board_shadow, state ='disabled')
			self.check_out.configure(bg = self.settings.shadow, fg = self.settings.board_shadow, state ='disabled')
			self.navbar_button.configure(bg = self.settings.board_shadow)

			for i in range(-self.settings.width,0):
				self.navbar_option_frame.place(x=i, y=0)
				self.navbar_option_frame_.place(x=i, y=0)
				self.header_frame.update()

			self.btn_status = True

		else:

			for i in range(0, self.settings.width):
				self.navbar_option_frame.place(x=-i, y=0)
				self.navbar_option_frame_.place(x=-i, y=0)
				self.header_frame.update()

			self.configure(bg = self.settings.board_color)
			self.header_frame.configure(bg = self.settings.board_color)
			self.header_label.configure(bg = self.settings.board_color, fg = self.settings.font_color)
			self.button_frame.configure(bg = self.settings.board_color)
			self.check_in_frame.configure(bg = self.settings.board_color)
			# self.show_guest_frame.configure(bg = self.settings.board_color)
			self.check_out_frame.configure(bg = self.settings.board_color)
			self.check_in.configure(bg =self.settings.color_theme, fg = self.settings.board_color, state = 'normal')
			# self.show_guest.configure(bg = self.settings.color_theme, fg =self.settings.board_color)
			self.check_out.configure(bg = self.settings.color_theme, fg = self.settings.board_color, state = 'normal')
			self.navbar_button.configure(bg = self.settings.board_color)

			self.btn_status = False

	def create_button(self):
		frame_h = 2*self.settings.height//3

		self.button_frame = tk.Frame(self, bg = self.settings.board_color, height = frame_h,width = self.settings.width//2)
		self.button_frame.pack()

		self.check_in_frame = tk.Frame(self.button_frame, bg = self.settings.board_color ,height = frame_h//2)
		self.check_in_frame.pack()

		self.check_in = tk.Button(self.check_in_frame, text = "Check In",  bg = self.settings.color_theme , fg = self.settings.board_color, font = self.settings.option_font, width = 17, bd=0, command=self.app.check_in_page, activebackground = self.settings.color_theme)
		self.check_in.grid(sticky="nsew", padx=20, pady=15, row=0)

		self.check_out_frame = tk.Frame(self.button_frame, bg = self.settings.board_color, height = frame_h//2)
		self.check_out_frame.pack()

		self.check_out = tk.Button(self.check_out_frame, text = "Check Out",  bg = self.settings.color_theme , fg = self.settings.board_color, font = self.settings.option_font, width = 17, bd=0, command=self.app.check_out_page, activebackground = self.settings.color_theme)
		self.check_out.grid(sticky="nsew", padx=20, pady=15, row = 1)

		if self.settings.font == 'medium':
			self.navbar_option_frame_ = tk.Frame(self.button_frame, bg = self.settings.board_color, height = 1000, width = 108)
			self.navbar_option_frame_.place(x = -108, y = 0)
		elif self.settings.font == 'small':
			self.navbar_option_frame_ = tk.Frame(self.button_frame, bg = self.settings.board_color, height = 1000, width = 91)
			self.navbar_option_frame_.place(x = -91, y = 0)
		elif self.settings.font == 'large':
			self.navbar_option_frame_ = tk.Frame(self.button_frame, bg = self.settings.board_color, height = 1000, width = 134)
			self.navbar_option_frame_.place(x = -134, y = 0)

	def exit(self):
		sys.exit()
