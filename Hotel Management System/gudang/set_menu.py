import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk
import random
import sys
import time

class SetMenu(tk.Frame):

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
		self.create_set_menu()
		self.check_user()
		self.check_pass()

	def create_header(self):
		frame_h = self.settings.height//3 + 37

		self.admin_info = tk.Frame(self, bg = self.settings.color_theme, height = self.settings.height//4 + 15, width = self.settings.width)
		self.admin_info.pack()

		self.avatar = tk.PhotoImage(file = 'img/profile_icon.png')
		image = Image.open("img/profile_icon.PNG")
		image_w, image_h = image.size
		ratio = 8
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.avatar = ImageTk.PhotoImage(image)

		self.avatar_label = tk.Label(self.admin_info, image = self.avatar, bg = self.settings.color_theme)
		self.avatar_label.place(x = 35, y =40)

		self.admin_name =tk.Label(self.admin_info, text = self.app.name, bg = self.settings.color_theme, font=self.settings.user_font, fg = self.settings.board_color)
		self.admin_name.place(x = 130, y = 60)

		self.admin_status = tk.Label(self.admin_info, text = self.app.status, bg = self.settings.color_theme, font=self.settings.status_font, fg = self.settings.board_color)
		if self.settings.font == 'large':
			self.admin_status.place(x = 135, y = 93)
		elif self.settings.font == 'medium':
			self.admin_status.place(x = 135, y = 83)
		elif self.settings.font == 'small':
			self.admin_status.place(x = 135, y = 83)

		self.back_photo = tk.PhotoImage(file=self.settings.back_img)
		image = Image.open(self.settings.back_img)
		image_w, image_h = image.size
		ratio = 12
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.back_photo = ImageTk.PhotoImage(image)

		self.back = tk.Button(self.admin_info, image = self.back_photo, bd = 0, bg = self.settings.color_theme, command=self.app.back, height = self.settings.height//8//2, width = self.settings.width//13, activebackground = self.settings.color_theme)
		self.back.place(x = 5, y = 5)

		self.ok_img = tk.PhotoImage(file = self.settings.ok_img)
		image = Image.open(self.settings.ok_img)
		image_w, image_h = image.size
		ratio = 18
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.ok_img = ImageTk.PhotoImage(image)

		self.ok = tk.Button(self.admin_info, image = self.ok_img, bd = 0, bg = self.settings.color_theme, activebackground = self.settings.color_theme, command = self.app.save_set)
		self.ok.place(x = self.settings.width-45, y = 10)


		self.moon = tk.PhotoImage(file = 'img/darkmode.png')
		image = Image.open("img/darkmode.PNG")
		image_w, image_h = image.size
		ratio = 3
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.moon = ImageTk.PhotoImage(image)

		self.dark_mode = tk.Button(self.admin_info, image=self.moon, bg=self.settings.color_theme, bd=0, activebackground = self.settings.color_theme, command = self.app.dark_mode)
		self.dark_mode.place(x = self.settings.width-155, y = 45)

	def create_set_menu(self):
		frame_h = self.settings.height//3 
		self.set_menu_frame = tk.Frame(self, bg = self.settings.board_shadow, height = self.settings.height//3, width = self.settings.width)
		self.set_menu_frame.place(x = 0, y = self.settings.height//4 + 15)

	# account settings
		self.account_label = tk.Label(self.set_menu_frame, text = "Account", font = self.settings.option_font, fg = self.settings.color_theme, bg = self.settings.board_shadow)
		self.account_label.place(x = 10 , y = 5)

		self.change_user_ = tk.Label(self.set_menu_frame, text="username", font = self.settings.info_font, anchor = 'w', bd = 0, bg = self.settings.board_shadow, fg = self.settings.font_color)
		self.change_user_.place(x = 15, y = 35)

		self.user = tk.StringVar()
		self.change_user = tk.Entry(self.set_menu_frame, font = self.settings.option_font, width = 80, bd = 0, bg = self.settings.board_shadow, textvariable = self.user, fg = self.settings.font_color)
		self.change_user.insert(0, self.app.user)
		self.change_user.place(x = 13, y = 55)
		self.change_user.bind("<Key>", self.app.check_entry_usernme)

		self.garis = tk.Frame(self.set_menu_frame, width=self.settings.width-45, height=1, bg="#141414").place(x=15,y=80)

		self.change_pass_ = tk.Label(self.set_menu_frame, text="password", font = self.settings.info_font, anchor = 'w', bd = 0, bg = self.settings.board_shadow, fg = self.settings.font_color)
		self.change_pass_.place(x = 15, y = 85)

		self.passwd = tk.StringVar()
		self.change_pass = tk.Entry(self.set_menu_frame, font = self.settings.option_font, width = 80, bd = 0, bg = self.settings.board_shadow, show = "*", textvariable = self.passwd, fg = self.settings.font_color)
		self.change_pass.insert(0, self.app.password)
		self.change_pass.place(x = 13, y =115)
		self.change_pass.bind("<Key>", self.app.check_entry_password)

		self.garis2 = tk.Frame(self.set_menu_frame, width=self.settings.width-45, height=1, bg="#141414").place(x=15,y=135)

	# display settings
		self.set_display_frame = tk.Frame(self, bg = self.settings.board_shadow, height = self.settings.height, width = self.settings.width)
		self.set_display_frame.place(x = 0, y = (self.settings.height//4 + 15)+ self.settings.height//3 + 5)

		self.account_label = tk.Label(self.set_display_frame, text = "Display", font = self.settings.option_font, fg = self.settings.color_theme, bg = self.settings.board_shadow)
		self.account_label.place(x = 10 , y = 5)

		self.change_font_ = tk.Label(self.set_display_frame, text="font", font = self.settings.info_font, anchor = 'w', bd = 0, bg = self.settings.board_shadow, fg = self.settings.font_color)
		self.change_font_.place(x = 15, y = 35)

		self.rad_frame = tk.Frame(self.set_display_frame, bg = self.settings.board_shadow, height = self.settings.height//12, width = self.settings.width)
		self.rad_frame.place(x = 0,y= 55)

		self.font = tk.IntVar()

		x = self.settings.width-30

		self.small_rad = tk.Radiobutton(self.rad_frame, text = "small", value = 1, font=("Cambira", 9), variable = self.font, bg = self.settings.board_shadow, activebackground = self.settings.board_shadow)
		self.small_rad.place(x = 30, y = 10)

		self.small_rad_ = tk.Label(self.rad_frame, text = "small", font=("Cambira", 9), bg = self.settings.board_shadow, fg = self.settings.font_color)
		self.small_rad_.place(x = 47, y = 10)

		self.med_rad = tk.Radiobutton(self.rad_frame, text = "medium", value = 2, font=("Cambira", 12), variable = self.font, bg = self.settings.board_shadow, activebackground = self.settings.board_shadow)
		self.med_rad.place(x = x//3, y = 10)

		self.med_rad_ = tk.Label(self.rad_frame, text = "medium", font=("Cambira", 12), bg = self.settings.board_shadow, fg = self.settings.font_color)
		self.med_rad_.place(x = x//3+19, y = 10)

		self.large_rad = tk.Radiobutton(self.rad_frame, text = "large", value = 3, font=("Cambira", 15), variable = self.font, bg = self.settings.board_shadow, activebackground = self.settings.board_shadow )
		self.large_rad.place(x = 2*x//3, y = 10)

		self.large_rad_ = tk.Label(self.rad_frame, text = "large", font=("Cambira", 15), bg = self.settings.board_shadow, fg = self.settings.font_color )
		self.large_rad_.place(x = 2*x//3+21, y = 10)

		if self.settings.font == 'medium':
			self.med_rad.select()
		elif self.settings.font == 'small':
			self.small_rad.select()
		elif self.settings.font == 'large':
			self.large_rad.select()


		self.change_theme = tk.Label(self.set_display_frame, text="theme", font = self.settings.info_font, anchor = 'w', bd = 0, bg = self.settings.board_shadow, fg = self.settings.font_color )
		self.change_theme.place(x = 15, y = 105)

		self.theme_frame = tk.Frame(self.set_display_frame, bg = self.settings.board_shadow, height = self.settings.height//12, width = self.settings.width)
		self.theme_frame.place(x = 0,y= self.settings.height//12+85)

		self.theme = tk.IntVar()
		x = self.settings.width-30

		self.orange_rad = tk.Radiobutton(self.theme_frame, text = "orange", value = 1, font=("Cambira", 12), variable = self.theme, bg = "#f07b52", activebackground = "#f07b52" )
		self.orange_rad.place(x = 30, y = 15)

		self.blue_rad = tk.Radiobutton(self.theme_frame, text = "blue", value = 2, font=("Cambira", 12), variable = self.theme, bg = "#12a4ff", activebackground ="#12a4ff")
		self.blue_rad.place(x = x//3, y = 15)

		self.other_rad = tk.Radiobutton(self.theme_frame, text = "choose other color", value = 3, font=("Cambira", 12), variable = self.theme, bg = self.settings.board_shadow, state = 'disable', activebackground = self.settings.board_shadow)
		self.other_rad.place(x = 2*x//3, y = 15)

		self.other_button = tk.Button(self.theme_frame, text = "choose other color", font=("Cambira", 12), bg = self.settings.board_shadow, command = self.pick_color, bd =0, fg = self.settings.font_color)
		self.other_button.place(x = 2*x//3 + 15, y = 15)

		if self.settings.color_theme == '#f07b52':
			self.orange_rad.select()
		elif self.settings.color_theme == '#12a4ff':
			self.blue_rad.select()
		else:
			self.other_rad.select()
			self.other_rad.configure(bg = self.settings.color_theme, state = 'normal', activebackground = self.settings.color_theme)
			self.other_button.configure(bg = self.settings.color_theme)

	def pick_color(self):
		self.color_code = colorchooser.askcolor(title ="Choose color")
		if self.color_code != (None,None) :
			self.other_rad.configure(bg = self.color_code[1], state = 'normal', fg = 'black')
			self.other_button.configure(bg = self.color_code[1], fg = 'black')
			self.settings.color_tmp = str(self.color_code[1])
			print(self.settings.color_tmp)
			
	def check_user(self):
		
		self.correct_img = tk.PhotoImage(file = 'img/check_mark.png')
		image = Image.open("img/check_mark.PNG")
		image_w, image_h = image.size
		ratio = 15
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.correct_img = ImageTk.PhotoImage(image)

		self.wrong_img = tk.PhotoImage(file = 'img/wrong_mark.png')
		image = Image.open("img/wrong_mark.PNG")
		image_w, image_h = image.size
		ratio = 10
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.wrong_img = ImageTk.PhotoImage(image)

		if self.app.username_exist == True:
			self.correct = tk.Label(self.set_menu_frame, image = self.correct_img, bg= self.settings.board_shadow, height = 22, width = 22).place(x = 740, y = 50)
		elif self.app.username_exist == False:
			self.wrong = tk.Label(self.set_menu_frame, image = self.wrong_img, bg= self.settings.board_shadow, height = 22, width = 22).place(x = 740, y = 50)
		else:
			self.c = tk.Label(self.set_menu_frame, image = self.virtual_image, bg= self.settings.board_shadow, height = 22, width = 22).place(x = 740, y = 50)

	def check_pass(self):
		self.correct_img_ = tk.PhotoImage(file = 'img/check_mark.png')
		image = Image.open("img/check_mark.PNG")
		image_w, image_h = image.size
		ratio = 15
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.correct_img_ = ImageTk.PhotoImage(image)

		self.wrong_img_ = tk.PhotoImage(file = 'img/wrong_mark.png')
		image = Image.open("img/wrong_mark.PNG")
		image_w, image_h = image.size
		ratio = 10
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.wrong_img_ = ImageTk.PhotoImage(image)

		if self.app.pass_exist == True:
			self.correct_pass = tk.Label(self.set_menu_frame, image = self.correct_img_, bg= self.settings.board_shadow, height = 22, width = 22).place(x = 740, y = 105)
		elif self.app.pass_exist == False:
			self.wrong_pass = tk.Label(self.set_menu_frame, image = self.wrong_img_, bg= self.settings.board_shadow, height = 22, width = 22).place(x = 740, y = 105)
		else:
			self.c_pass = tk.Label(self.set_menu_frame, image = self.virtual_image, bg= self.settings.board_shadow, height = 22, width = 22).place(x = 740, y = 105)