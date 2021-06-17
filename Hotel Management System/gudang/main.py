import tkinter as tk
from tkinter import filedialog
import sys
import os
from tkinter import messagebox

from settings import Settings
from appPage import AppPage
from check_in import CheckIn
from check_out import CheckOut
from menu_page import MenuPage
from login import Login
from print_guest import PrintGuest
from set_menu import SetMenu
from new_admin import NewAdmin

class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_container()

		self.pages = {}

		# self.create_appPage()
		# self.create_check_in()
		# self.create_check_out()

		# self.create_menu_page()
		# self.create_print_guest()
		# self.create_set_menu()
		self.create_login_page()

	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)

	def create_appPage(self):
		self.pages["appPage"] = AppPage(self.container, self.app)

	def create_check_in(self):
		self.pages["check_in"] = CheckIn(self.container, self.app)

	def create_check_out(self):
		self.pages["check_out"] = CheckOut(self.container, self.app)

	def create_menu_page(self):
		self.pages["menu_page"] = MenuPage(self.container, self.app)

	def create_login_page(self):
		self.pages["login"] = Login(self.container, self.app)

	def create_print_guest(self):
		self.pages["print_guest"] = PrintGuest(self.container, self.app)

	def create_set_menu(self):
		self.pages["set_menu"] = SetMenu(self.container, self.app)

	def create_new_admin(self):
		self.pages["new_admin"] = NewAdmin(self.container, self.app)

class Gudang:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

		self.user = ''
		self.password = ''
		self.name = ''
		self.status = ''
		self.color = ''
		self.username_exist = None
		self.pass_exist = None

		self.new_username = [""]
		self.new_pass = [""]	

	def run(self):
		self.window.mainloop()

	def check_entry_usernme(self, key):
		user = self.window.pages['set_menu'].user
		self.username_exist =True

		self.new_username = [str(user.get())]

		if key.keycode != 8:
			for i in self.new_username:
				i += str(key.char)
			self.new_username.append(i)
		elif key.keycode == 8 :
			for i in self.new_username:
				list1 = list(i)
				list2 = list1[:-1]
				str2 = ''
				for j in list2:
					str2 +=j
			self.new_username.append(str2)

		key_list = []

		for dic in self.settings.admin:
			for key, info in dic.items() :
				key_list.append(key)
				
		key_list.remove(self.user)
		for i in key_list:
			if i == self.new_username[1] or self.new_username[1] == '' :
				self.username_exist = False

		self.window.pages['set_menu'].check_user()

	def check_entry_password(self, key):
		password = self.window.pages['set_menu'].passwd
		self.pass_exist = None
		len_ = None
		number = None
		cnt = 0

		self.new_pass = [str(password.get())]

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
		print(self.pass_exist)

		self.window.pages['set_menu'].check_pass()

	def save_set(self):
		
		correct = False
		cnt = 0

		print('pass', self.pass_exist)
		print('user', self.username_exist)

	# true true	
		if (self.pass_exist == True and self.username_exist == True):
			for dic in self.settings.admin:
				for key, info in dic.items():
					if key == self.user:
						correct = True
						color = info['theme']
						del self.settings.admin[cnt]
					cnt += 1

			if correct == True:
				if self.window.pages['set_menu'].font.get() == 1 :
					self.settings.font = 'small'
				elif self.window.pages['set_menu'].font.get() == 2 :
					self.settings.font = 'medium'
				elif self.window.pages['set_menu'].font.get() == 3:
					self.settings.font = 'large'

				if self.window.pages['set_menu'].theme.get() == 1:
					self.settings.color_theme = "#f07b52"
				elif self.window.pages['set_menu'].theme.get() == 2:
					self.settings.color_theme = "#12a4ff"
				elif self.window.pages['set_menu'].theme.get() == 3:
					if self.window.pages['set_menu'].theme.get() == '':
						self.settings.color_theme = color
					else:
						self.settings.color_theme = self.settings.color_tmp

				data={str(self.new_username[1]) : {'password' : str(self.new_pass[1]), 'name' : str(self.name), 'status' : str(self.status), 'theme' : self.settings.color_theme, 'font' : self.settings.font, 'mode': self.settings.mode}}
				self.settings.admin.append(data)
				self.settings.save_admin()
				self.settings.font_size()

				self.user = self.new_username[1]
				self.password = self.new_pass[1]
				self.pass_exist = None
				self.username_exist = None

				self.settings.shadow_color()
				self.window.create_menu_page()
				page = self.window.pages["menu_page"]

				page.tkraise()

	#true none
		elif (self.pass_exist == True and self.username_exist == None):
			for dic in self.settings.admin:
				for key, info in dic.items():
					if key == self.user:
						correct = True
						color = info['theme']
						del self.settings.admin[cnt]
					cnt += 1

			if correct == True:
				if self.window.pages['set_menu'].font.get() == 1 :
					self.settings.font = 'small'
				elif self.window.pages['set_menu'].font.get() == 2 :
					self.settings.font = 'medium'
				elif self.window.pages['set_menu'].font.get() == 3:
					self.settings.font = 'large'

				if self.window.pages['set_menu'].theme.get() == 1:
					self.settings.color_theme = "#f07b52"
				elif self.window.pages['set_menu'].theme.get() == 2:
					self.settings.color_theme = "#12a4ff"
				elif self.window.pages['set_menu'].theme.get() == 3:
					if self.window.pages['set_menu'].theme.get() == '':
						self.settings.color_theme = color
					else:
						self.settings.color_theme = self.settings.color_tmp

				data={str(self.user) : {'password' : str(self.new_pass[1]), 'name' : str(self.name), 'status' : str(self.status), 'theme' : self.settings.color_theme, 'font' : self.settings.font, 'mode': self.settings.mode}}
				self.settings.admin.append(data)
				print(self.settings.admin)
				self.settings.save_admin()
				self.settings.font_size()

				self.pass_exist = None
				self.username_exist = None
				self.password = self.new_pass[1]

				self.settings.shadow_color()
				self.window.create_menu_page()
				page = self.window.pages["menu_page"]

				page.tkraise()

	# none true
		elif (self.pass_exist == None and self.username_exist == True):
			for dic in self.settings.admin:
				for key, info in dic.items():
					if key == self.user:
						correct = True
						color = info['theme']
						del self.settings.admin[cnt]
					cnt += 1

			if correct == True:
				if self.window.pages['set_menu'].font.get() == 1 :
					self.settings.font = 'small'
				elif self.window.pages['set_menu'].font.get() == 2 :
					self.settings.font = 'medium'
				elif self.window.pages['set_menu'].font.get() == 3:
					self.settings.font = 'large'

				if self.window.pages['set_menu'].theme.get() == 1:
					self.settings.color_theme = "#f07b52"
				elif self.window.pages['set_menu'].theme.get() == 2:
					self.settings.color_theme = "#12a4ff"
				elif self.window.pages['set_menu'].theme.get() == 3:
					if self.window.pages['set_menu'].theme.get() == '':
						self.settings.color_theme = color
					else:
						self.settings.color_theme = self.settings.color_tmp

				data={str(self.new_username[1]) : {'password' : str(self.password), 'name' : str(self.name), 'status' : str(self.status), 'theme' : self.settings.color_theme, 'font' : self.settings.font, 'mode': self.settings.mode}}
				self.settings.admin.append(data)
				print(self.settings.admin)
				self.settings.save_admin()
				self.settings.font_size()

				self.pass_exist = None
				self.username_exist = None

				self.user = self.new_username[1]

				self.settings.shadow_color()
				self.window.create_menu_page()
				page = self.window.pages["menu_page"]

				page.tkraise()

	# none none
		elif (self.pass_exist == None and self.username_exist == None) :
			for dic in self.settings.admin:
				for key, info in dic.items():
					if key == self.user:
						correct = True
						color = info['theme']
						del self.settings.admin[cnt]
					cnt += 1

			if correct == True:
				if self.window.pages['set_menu'].font.get() == 1 :
					self.settings.font = 'small'
				elif self.window.pages['set_menu'].font.get() == 2 :
					self.settings.font = 'medium'
				elif self.window.pages['set_menu'].font.get() == 3:
					self.settings.font = 'large'

				if self.window.pages['set_menu'].theme.get() == 1:
					self.settings.color_theme = "#f07b52"
				elif self.window.pages['set_menu'].theme.get() == 2:
					self.settings.color_theme = "#12a4ff"
				elif self.window.pages['set_menu'].theme.get() == 3:
					if self.settings.color_theme == '':
						self.settings.color_theme = color
					else:
						self.settings.color_theme = self.settings.color_tmp

					# print('color sett= ',self.settings.color_theme)
					# print('color =', color)
					# print('color tmp =', self.settings.color_tmp)


				data={str(self.user) : {'password' : str(self.password), 'name' : str(self.name), 'status' : str(self.status), 'theme' : self.settings.color_theme, 'font' : self.settings.font, 'mode': self.settings.mode}}
				self.settings.admin.append(data)
				self.settings.save_admin()
				self.settings.font_size()

				self.settings.shadow_color()
				self.window.create_menu_page()
				page = self.window.pages["menu_page"]

				page.tkraise()

	def dark_mode(self):
		cnt = 0

		if self.settings.mode == 'day' :
			self.settings.mode = 'night'
		elif self.settings.mode == 'night' :
			self.settings.mode = 'day'

		for dic in self.settings.admin:
				for key, info in dic.items():
					if key == self.user:
						correct = True
						del self.settings.admin[cnt]
					cnt += 1

		if correct == True:
			data={str(self.user) : {'password' : str(self.password), 'name' : str(self.name), 'status' : str(self.status), 'theme' : self.settings.color_theme, 'font' : self.settings.font, 'mode': self.settings.mode}}
			self.settings.admin.append(data)
			self.settings.save_admin()


			self.settings.mode_config()
			self.window.create_set_menu()
			page = self.window.pages['set_menu']
			page.tkraise()
			print(self.settings.mode)

	def check_in_page(self):
		self.window.create_check_in()
		page = self.window.pages["check_in"]
		page.tkraise()

	def check_out_page(self):
		self.window.create_check_out()
		page = self.window.pages["check_out"]
		page.tkraise()
	
	def show_guest(self):
		self.window.create_appPage()
		page = self.window.pages["appPage"]
		page.tkraise()

	def print(self):
		self.window.create_print_guest()
		page = self.window.pages["print_guest"]
		page.tkraise()
		print('print works')

	def back_print(self):
		# if self.window.pages["print_guest"].dwnld  == False:
		# 	os.remove('pdf/guest.pdf')
		page = self.window.pages["menu_page"]
		page.tkraise()

	def setting_page(self):
		self.window.create_set_menu()
		page = self.window.pages['set_menu']
		page.tkraise()

	def new_admin_page(self):
		self.window.create_new_admin()
		page = self.window.pages["new_admin"]
		page.tkraise()

	def log_out(self):
		self.window.create_login_page()
		page = self.window.pages['login']
		page.tkraise()

	def check_out_page(self):
		self.window.create_check_out()
		page = self.window.pages["check_out"]
		page.tkraise()

	def back(self):
		self.window.create_menu_page()
		page = self.window.pages["menu_page"]
		page.tkraise()

	def change(self, page):
		self.settings.load_admin()
		correct = False
		

		for dic in self.settings.admin:
			for key, info in dic.items() :
				user = key
				passwd = info['password']	
			
				if self.window.pages['login'].nameVar.get() == user and self.window.pages['login'].passwordVar.get() == passwd:
					correct = True
					if correct == True:
						
						self.user = user
						self.password = passwd
						self.name = info['name']
						self.status = info['status']
						self.settings.color_theme = info['theme']
						self.settings.color_tmp = info['theme']
						self.settings.font = info['font']
						self.settings.mode = info['mode']

						print("a = ",info['theme'])

		if correct:

			a =  messagebox.askyesnocancel("LOGIN SUCCESS",'Do you want to continue?')
		
			if a == True:
				self.settings.font_size()
				self.settings.shadow_color()
				self.settings.mode_config()

				self.window.create_menu_page()
				page = self.window.pages["menu_page"]

				page.tkraise()
		else:
			messagebox.showwarning("WRONG","Check your Username/Password")
			
if __name__ == '__main__':
	myGudangApp = Gudang()
	myGudangApp.run()