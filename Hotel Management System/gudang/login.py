import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


class Login(tk.Frame):

	def __init__(self, parent, App): #self.container, self.app

		self.app = App
		self.settings = App.settings

		super().__init__(parent)
		self.configure(bg="#ebebeb")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		# virtual image
		self.virtual_image = tk.PhotoImage(width = 1, height = 1)

		self.create_header()
		self.create_button()
		self.create_cancel()

	def create_header(self):
		frame_h = self.settings.height//8
		self.header_frame = tk.LabelFrame(self, bg = "white", width = self.settings.width, height = frame_h)
		self.header_frame.pack(fill = "x", padx=10, pady=(20,10))

		self.header_label = tk.Label(self.header_frame, text = "LOGIN FORM", font = ("Arial", 37, "bold"), image = self.virtual_image, compound = 'c', height = frame_h, bg = "white", fg = "black")
		self.header_label.grid(row = 0, column = 0)

		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

	def create_button(self):
		frame_h = self.settings.height//3

		self.button_frame = tk.LabelFrame(self, bg = "white", width = self.settings.width, height = frame_h)
		self.button_frame.pack(fill = "x", padx=10)

		self.profile_frame = tk.Frame(self.button_frame, bg = "white", width = self.settings.width//2, height = frame_h//3)
		self.profile_frame.pack()

		self.profile_photo = tk.PhotoImage(file="img/profile.PNG")
		image = Image.open("img/profile.PNG")
		image_w, image_h = image.size
		ratio = 6
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.back_photo = ImageTk.PhotoImage(image)

		self.human_photo = tk.PhotoImage(file="img/human.png")
		image = Image.open("img/human.PNG")
		image_w, image_h = image.size
		ratio = 10
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.human_photo_img = ImageTk.PhotoImage(image)

		self.lock_photo = tk.PhotoImage(file="img/lock.png")
		image = Image.open("img/lock.PNG")
		image_w, image_h = image.size
		ratio = 11.5
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.lock_photo_img = ImageTk.PhotoImage(image)

		self.photo = tk.Label(self.profile_frame, image=self.back_photo, bg="white")
		self.photo.grid()

		self.username_frame = tk.Frame(self.button_frame, bg = "white", width = self.settings.width//2, height = frame_h//3)
		self.username_frame.pack()

		self.username_img = tk.Label(self.username_frame, image=self.human_photo_img, bg="white")
		self.username_img.grid(column=0, row=1, pady = 5)

		self.username_label = tk.Label(self.username_frame, text="   USERNAME", font = ("Cambira", 12, "bold"), bg="white")
		self.username_label.grid(padx=(2,self.settings.width), row=1, column=1)

		self.username_entry_frame = tk.Frame(self.button_frame, bg = "white", width = self.settings.width, height = frame_h//2)
		self.username_entry_frame.pack()

		def on_enter(e):
			if self.nameVar.get() == 'username':
				self.username_entry.delete(0, 'end')
				self.username_entry.configure(fg = 'black')
		def on_leave(e):
			if self.nameVar.get() == '':
				self.username_entry.configure(fg = 'gray')
				self.username_entry.insert(0, 'username')

		self.nameVar = tk.StringVar()
		self.username_entry = tk.Entry(self.username_entry_frame,width=62, font=("Cambira", 16), textvariable=self.nameVar, border=0, fg="gray")
		
		self.username_entry.bind("<FocusIn>", on_enter)
		self.username_entry.bind("<FocusOut>", on_leave)
		self.username_entry.insert(0, "username")
		self.username_entry.grid(padx=(15,self.settings.width), row=1)

		self.garis = tk.Frame(self.username_entry_frame, width=750, height=8, bg="#141414").place(x=15,y=25)

		self.password_frame = tk.Frame(self.button_frame,bg = "white", width = self.settings.width, height = frame_h//3)
		self.password_frame.pack()

		self.password_img = tk.Label(self.password_frame, image= self.lock_photo_img, bg="white")
		self.password_img.grid(column=0, row=1, pady = 11)

		self.password_label = tk.Label(self.password_frame, text="PASSWORD", font = ("Cambira", 12, "bold"), bg="white")
		self.password_label.grid(padx=(15,self.settings.width), row=1, column=1)

		self.password_entry_frame = tk.Frame(self.button_frame, bg = "white", width = self.settings.width, height = frame_h//2)
		self.password_entry_frame.pack()

		def on_enter2(e):
			if self.passwordVar.get() == 'Password':
				self.password_entry.delete(0, 'end')
				self.password_entry.configure(fg = 'black')
		def on_leave2(e):
			if self.passwordVar.get() == '':
				self.password_entry.configure(fg = 'gray')
				self.password_entry.insert(0, 'Password')

		self.passwordVar = tk.StringVar()
		self.password_entry = tk.Entry(self.password_entry_frame,width=62, font=("Cambira", 16), show="*", textvariable=self.passwordVar, border=0, fg = 'gray')
		self.password_entry.bind("<FocusIn>", on_enter2)
		self.password_entry.bind("<FocusOut>", on_leave2)
		self.password_entry.insert(0, "Password")
		self.password_entry.grid(padx=(15,self.settings.width), row=1)

		self.garis2 = tk.Frame(self.password_entry_frame, width=750, height=8, bg="#141414").place(x=15,y=25)

		self.masuk_frame = tk.Frame(self.button_frame, bg = "", width = self.settings.width, height = frame_h//2)
		self.masuk_frame.pack()

		self.masuk_entry = tk.Button(self.masuk_frame, text="Log In", width=75, height=1, bg="green", fg="white", command=lambda:self.app.change("menu_page"), font = ("Cambira", 12, "bold"), activebackground = 'green')

		self.masuk_entry.grid(pady=30)

	def create_cancel(self):
		frame_h = self.settings.height//7

		self.buttons_frame = tk.Frame(self, bg = "red", width = self.settings.width, height = frame_h)
		self.buttons_frame.pack(fill = "both", expand=True)

		self.cancel_frame = tk.Frame(self.buttons_frame, width = self.settings.width, height = frame_h, bg="#ebebeb")
		self.cancel_frame.pack(fill = "both", expand=True)

		self.cancel_button = tk.Button(self.cancel_frame, text="Exit", bg="red", height=1, width=12, fg="white", command=self.exit, font = ("Cambira", 12, "bold"), activebackground = 'red')
		self.cancel_button.place(x = 10, y = 20)

	def exit(self):
		confirm = messagebox.askyesnocancel("Login Confirmation", "Are you sure to exit this app ?")
		if confirm:
			sys.exit()

	"""	self.settings.usernameVar = self.pages['pageLogin'].userVar.get()
		self.settings.passwordVar = self.pages['pageLogin'].passwordVar.get()

		match = self.settings.usernameVar == self.settings.username and self.settings.passwordVar == self.settings.password
		if match:
			Msg.showinfo("LOGIN SUCCESS",'Do you want to continue?')
			page = self.pages['page01']
			page.tkraise()
		else:
			Msg.showwarning("WRONG","Check your Username/Password")"""