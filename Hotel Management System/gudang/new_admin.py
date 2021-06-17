import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import messagebox as Msg

class NewAdmin(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings
		self.filled = None
		self.pass_exist = None
		self.username_exist = None

		super().__init__(parent)
		self.configure(bg=self.settings.board_color)
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		# virtual image
		self.virtual_image = tk.PhotoImage(width = 1, height = 1)
		self.title()
		self.create_button()

	def title(self):
		frame_h =self.settings.height//5

		self.header_frame = tk.Frame(self, bg = self.settings.board_color, width = self.settings.width, height = frame_h)
		self.header_frame.pack(fill = "x")

		self.back_frame = tk.Frame(self.header_frame, bg = self.settings.board_color, width = self.settings.width//10, height = frame_h//2)
		self.back_frame.grid(row = 0, column = 0, sticky = "ne")

		self.header_frame_ = tk.Frame(self.header_frame, bg = self.settings.board_color, width = 9*self.settings.width//10, height = frame_h)
		self.header_frame_.grid(row = 0, column = 1, sticky = 'nsew')

		self.header_label = tk.Label(self.header_frame_, text = "New Admin", fg = self.settings.font_color, bg = self.settings.board_color ,font = self.settings.header_font, image = self.virtual_image, compound = "c")
		self.header_label.place(x= 165, y= 15)

		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

		self.back_photo = tk.PhotoImage(file=self.settings.back_img)
		image = Image.open(self.settings.back_img)
		image_w, image_h = image.size
		ratio = 12
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.back_photo = ImageTk.PhotoImage(image)

		self.back = tk.Button(self.back_frame, image = self.back_photo, bd = 0, bg = self.settings.board_color, command=self.app.back, height = frame_h//2, width = self.settings.width//10, activebackground = self.settings.board_color)
		self.back.grid(column=0, row=0, padx=(0,508))


		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

	def create_button(self):
		frame_h = self.settings.height//3
		width = self.settings.width

	# name, address, phone number, day
		self.content_frame = tk.Frame(self, bg = self.settings.board_color)
		self.content_frame.pack(fill = "both", expand = True)

		self.detail_frame = tk.Frame(self.content_frame, bg = self.settings.board_color, width = width//3, height = 3*frame_h)
		self.detail_frame.grid(sticky = 'ne', row = 0, column = 0)

		self.details_label = []

		details = ['Admin Name :','Status :', 'Username :', 'Password :']

		y = 62
		for detail in details:
			label = tk.Label(self.detail_frame, text=detail, bg=self.settings.board_color, fg = self.settings.font_color, font=self.settings.content_font)
			if self.settings.font == 'large':
				label.place(x = 95, y = y)
				y += 47
			elif self.settings.font == 'medium':
				label.place(x = 115, y = y)
				y += 45
			elif self.settings.font == 'small':
				label.place(x = 155, y = y)
				y += 48
			self.details_label.append(label)

		self.entry_frame = tk.Frame(self.content_frame, bg = self.settings.board_color, width = 2*width//3, height = 3*frame_h)
		self.entry_frame.grid(sticky = 'ne', row = 0, column = 1)

		self.admin_name = tk.StringVar()
		self.admin_name_entry =tk.Entry(self.entry_frame, fg = 'black', font=self.settings.content_font,textvariable = self.admin_name)

		self.status = tk.StringVar()
		self.status_entry =tk.Entry(self.entry_frame, fg = 'black', font=self.settings.content_font, textvariable = self.status)

		def on_enter_(e):
			if self.name.get() == 'admin123':
				self.name_entry.delete(0, 'end')
				self.name_entry.configure(fg = 'black')
		def on_leave_(e):
			if self.name.get() == '':
				self.name_entry.configure(fg = 'gray')
				self.name_entry.insert(0, 'admin123')

		self.name = tk.StringVar()
		self.name_entry =tk.Entry(self.entry_frame, fg = 'gray', font=self.settings.content_font , textvariable = self.name)
		self.name_entry.bind("<Key>", self.check_entry_usernme)
		self.name_entry.bind("<FocusIn>", on_enter_)
		self.name_entry.bind("<FocusOut>", on_leave_)
		self.name_entry.insert(0, "admin123")

		def on_enter(e):
			if self.passwd.get() == 'at least 8 characters and 2 number':
				self.passwd_entry.delete(0, 'end')
				self.passwd_entry.configure(fg = 'black')
		def on_leave(e):
			if self.passwd.get() == '':
				self.passwd_entry.configure(fg = 'gray')
				self.passwd_entry.insert(0, 'at least 8 characters and 2 number')

		self.passwd = tk.StringVar()
		self.passwd_entry =tk.Entry(self.entry_frame, fg = 'gray', font=self.settings.content_font, textvariable = self.passwd)
		self.passwd_entry.bind("<Key>", self.check_entry_password)
		self.passwd_entry.bind("<FocusIn>", on_enter)
		self.passwd_entry.bind("<FocusOut>", on_leave)
		self.passwd_entry.insert(0, "at least 8 characters and 2 number")

		self.sumbit_buttton = tk.Button(self.content_frame, text = "Create Now",  bg = self.settings.color_theme, fg = self.settings.board_color, font = self.settings.content_font, command=self.create_now, width = 13, bd=0, activebackground = self.settings.color_theme)

		self.placement()
		
	def placement(self):
		if self.settings.font == 'large':
			self.admin_name_entry.configure(width = 38)
			self.admin_name_entry.place(x = 0, y = 65)

			self.status_entry.configure(width = 38)
			self.status_entry.place(x = 0, y = 110)

			self.name_entry.configure(width = 38)
			self.name_entry.place(x = 0, y = 155)

			self.passwd_entry.configure(width = 38)
			self.passwd_entry.place(x = 0, y = 200)

			self.sumbit_buttton.place(x = 625, y = 355)

		elif self.settings.font == 'medium':
			self.admin_name_entry.configure(width = 45)
			self.admin_name_entry.place(x = 0, y = 63)

			self.status_entry.configure(width = 45)
			self.status_entry.place(x = 0, y = 108)

			self.name_entry.configure(width = 45)
			self.name_entry.place(x = 0, y = 153)

			self.passwd_entry.configure(width = 45)
			self.passwd_entry.place(x = 0, y = 198)

			self.sumbit_buttton.place(x = 635, y = 365)

		elif self.settings.font == 'small':
			self.admin_name_entry.configure(width = 55)
			self.admin_name_entry.place(x = 0, y = 62)

			self.status_entry.configure(width = 55)
			self.status_entry.place(x = 0, y = 110)

			self.name_entry.configure(width = 55)
			self.name_entry.place(x = 0, y = 158)

			self.passwd_entry.configure(width = 55)
			self.passwd_entry.place(x = 0, y = 206)

			self.sumbit_buttton.place(x = 697, y = 375)

	def create_now(self):
		self.user = self.name.get()
		self.admin_name_ = self.admin_name.get()
		self.passwd_ = self.passwd.get()
		self.status_ = self.status.get()
		self.theme = "#f07b52"
		self.font = "medium"
		self.mode = "day"

		self.cor = self.username_exist and self.pass_exist

		self.check_filled()

		print('filled = ', self.filled)
		print('username_exist =', self.username_exist)
		print('pass_exist = ', self.pass_exist)
		print('cor = ', self.cor)

		if self.filled == True and self.cor  == True:
			info = {self.user : {"password": self.passwd_, "name" : self.admin_name_, "status" : self.status_, "theme" : self.theme, "font" : self.font, "mode" : self.mode }}
			self.settings.admin.append(info)
			self.settings.save_admin()
			Msg.showinfo("Hotel Management", "Successed")
			self.app.new_admin_page()

		elif self.filled == False and self.cor == False:
			Msg.showwarning("Hotel Management", "Please Fill The Forum")

		elif self.filled == False and self.cor == True:
			Msg.showwarning("Hotel Management", "Please Fill The Forum")

		elif self.filled == False and self.cor == False:
			Msg.showwarning("Hotel Management", "Please Fill The Forum")

		elif self.filled == True and self.cor == None:
			Msg.showwarning("Hotel Management", "Please Fill The Forum")

		elif self.filled == False and self.cor == None:
			Msg.showwarning("Hotel Management", "Please Fill The Forum")

	def check_filled(self):
		if self.user == "" or self.passwd_ == "" or self.status_ == "" or self.admin_name_ == "":
			self.filled = False
		else:
			self.filled = True

	def check_entry_password(self, key):
		self.passwd_entry.configure(show = '*')
		self.pass_exist = None
		len_ = None
		number = None
		cnt = 0

		self.new_pass = [str(self.passwd.get())]

		if key.keycode != 8:
			for i in self.new_pass:
				i += str(key.char)
			self.new_pass.append(i)
		elif key.keycode == 8 :
			for i in self.new_pass:
				list1 = list(i)
				list2 = list1[:-1]
				str2 = ''
				for j in list2:
					str2 +=j
			self.new_pass.append(str2)

		for dic in self.settings.admin:
			for key, info in dic.items() :
				pass_list = list(self.new_pass[1])

				for i in pass_list:
					if i == '1' or i =='2' or i =='3' or i == '4' or i =='5' or i =='6' or i == '7' or i =='8' or i =='9' or i == '0' :
						cnt +=1
				if len(pass_list) < 8 :
					len_ = False
				else:
					len_ = True
				if cnt < 4:
					number = False
				else:
					number = True

		self.pass_exist = (len_ and number)

		print(self.new_pass)

		if self.new_pass[1] == '':
			self.pass_exist = None

		self.check_password()
		# print(self.pass_exist)

	def check_password(self):
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

		if self.settings.font == 'large':
			if self.pass_exist == True:
				self.correct_pass = tk.Label(self.entry_frame, image = self.correct_img_, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 203)
			elif self.pass_exist == False:
				self.wrong_pass = tk.Label(self.entry_frame, image = self.wrong_img_, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 203)
			else:
				self.c_pass = tk.Label(self.entry_frame, image = self.virtual_image, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 203)

		elif self.settings.font == 'medium':
			if self.pass_exist == True:
				self.correct_pass = tk.Label(self.entry_frame, image = self.correct_img_, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 196)
			elif self.pass_exist == False:
				self.wrong_pass = tk.Label(self.entry_frame, image = self.wrong_img_, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 196)
			else:
				self.c_pass = tk.Label(self.entry_frame, image = self.virtual_image, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 196)
		
		elif self.settings.font == 'small':
			if self.pass_exist == True:
				self.correct_pass = tk.Label(self.entry_frame, image = self.correct_img_, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 196)
			elif self.pass_exist == False:
				self.wrong_pass = tk.Label(self.entry_frame, image = self.wrong_img_, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 196)
			else:
				self.c_pass = tk.Label(self.entry_frame, image = self.virtual_image, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 196)

	def check_entry_usernme(self, key):
		self.username_exist = True

		self.username = [str(self.name.get())]

		if key.keycode != 8:
			for i in self.username:
				i += str(key.char)
			self.username.append(i)
		elif key.keycode == 8 :
			for i in self.username:
				list1 = list(i)
				list2 = list1[:-1]
				str2 = ''
				for j in list2:
					str2 +=j
			self.username.append(str2)

		for dic in self.settings.admin:
			for key, info in dic.items() :
				if key == self.username[1] or self.username[1] == '':
					self.username_exist = False

		self.check_username()

	def check_username(self):
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

		if self.settings.font == 'large':
			if self.username_exist == True:
				self.correct = tk.Label(self.entry_frame, image = self.correct_img, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 155)
			elif self.username_exist == False:
				self.wrong = tk.Label(self.entry_frame, image = self.wrong_img, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 155)
			else:
				self.c = tk.Label(self.entry_frame, image = self.virtual_image, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 155)

		elif self.settings.font == 'medium':
			if self.username_exist == True:
				self.correct = tk.Label(self.entry_frame, image = self.correct_img, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 152)
			elif self.username_exist == False:
				self.wrong = tk.Label(self.entry_frame, image = self.wrong_img, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 152)
			else:
				self.c = tk.Label(self.entry_frame, image = self.virtual_image, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 152)

		elif self.settings.font == 'small':
			if self.username_exist == True:
				self.correct = tk.Label(self.entry_frame, image = self.correct_img, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 152)
			elif self.username_exist == False:
				self.wrong = tk.Label(self.entry_frame, image = self.wrong_img, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 152)
			else:
				self.c = tk.Label(self.entry_frame, image = self.virtual_image, bg= self.settings.board_color, height = 22, width = 22).place(x = 425, y = 152)