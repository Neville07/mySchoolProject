import tkinter as tk
from PIL import Image, ImageTk
import random
import sys
import time
from tkinter import messagebox as Msg

class CheckOut(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings
		self.filled = False
		self.delete = False

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
		frame_h =self.settings.height//5

		self.header_frame = tk.Frame(self, bg = self.settings.board_color, width = self.settings.width, height = frame_h)
		self.header_frame.pack(fill = "x")

		self.back_frame = tk.Frame(self.header_frame, bg = self.settings.board_color, width = self.settings.width//10, height = frame_h//2)
		self.back_frame.grid(row = 0, column = 0, sticky = "ne")

		self.header_frame_ = tk.Frame(self.header_frame, bg = self.settings.board_color, width = 9*self.settings.width//10, height = frame_h)
		self.header_frame_.grid(row = 0, column = 1, sticky = 'nsew')

		self.header_label = tk.Label(self.header_frame_, text = "Check Out", fg = self.settings.font_color, bg = self.settings.board_color ,font = self.settings.header_font, image = self.virtual_image, compound = "c")
		self.header_label.place(x= 195, y= 15)

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

		details = ['name :', 'address :', 'phone number :', 'room number :']

		y = 20
		for detail in details:
			label = tk.Label(self.detail_frame, text=detail, bg=self.settings.board_color, fg=self.settings.font_color, font=self.settings.content_font)
			if self.settings.font == 'large':
				label.place(x = 90, y = y)
				y += 45
			elif self.settings.font == 'medium':
				label.place(x = 115, y = y)
				y += 45
			elif self.settings.font == 'small':
				label.place(x = 155, y = y)
				y += 48
			self.details_label.append(label)

		self.entry_frame = tk.Frame(self.content_frame, bg = self.settings.board_color, width = 2*width//3, height = 3*frame_h)
		self.entry_frame.grid(sticky = 'ne', row = 0, column = 1)

		self.name = tk.StringVar()
		self.name_entry =tk.Entry(self.entry_frame, fg='black', font=self.settings.content_font, textvariable = self.name)

		self.address = tk.StringVar()
		self.address_entry =tk.Entry(self.entry_frame, fg='black', font=self.settings.content_font,width = 45, textvariable = self.address)

		self.p_nmbr = tk.StringVar()
		self.p_nmbr_entry =tk.Entry(self.entry_frame,  fg='black', font=self.settings.content_font,width = 45, textvariable = self.p_nmbr)

		self.nmbr = tk.StringVar()
		self.nmbr_entry =tk.Entry(self.entry_frame, fg='black', font=self.settings.content_font,width = 45, textvariable = self.nmbr)	

	# room type
		self.room_type_label = tk.Label(self.content_frame, text= "room type :", bg=self.settings.board_color, fg=self.settings.font_color, font=self.settings.content_font)
	
		self.room_type = tk.IntVar()

		self.dlx_rad = tk.Radiobutton(self.content_frame, text = "delux", value = 1, font=self.settings.content_font, variable = self.room_type, bg = self.settings.board_color, activebackground = self.settings.board_color )
		self.dlx_rad_ = tk.Label(self.content_frame, text = "delux", font=self.settings.content_font,  bg = self.settings.board_color, fg = self.settings.font_color)
		
		self.nrml_rad = tk.Radiobutton(self.content_frame, text = "normal", value = 2, font=self.settings.content_font, variable = self.room_type, bg = self.settings.board_color, activebackground = self.settings.board_color)
		self.nrml_rad_ = tk.Label(self.content_frame, text = "normal", font=self.settings.content_font, bg = self.settings.board_color, fg = self.settings.font_color)

		self.prsdt_rad = tk.Radiobutton(self.content_frame, text = "president", value = 3, font=self.settings.content_font, variable = self.room_type , bg = self.settings.board_color, activebackground = self.settings.board_color)
		self.prsdt_rad_ = tk.Label(self.content_frame, text = "president", font=self.settings.content_font, bg = self.settings.board_color, fg = self.settings.font_color)
		
		self.jnt_rad = tk.Radiobutton(self.content_frame, text = "joint", value = 4, font=self.settings.content_font, variable = self.room_type , bg = self.settings.board_color, activebackground = self.settings.board_color)
		self.jnt_rad_ = tk.Label(self.content_frame, text = "joint",font=self.settings.content_font, bg = self.settings.board_color, fg = self.settings.font_color)

		self.sumbit_buttton = tk.Button(self.content_frame, text = "Check Out", font = self.settings.content_font, bd = 0, width = 15, bg = self.settings.color_theme, fg = self.settings.board_color, command = self.check_out, activebackground = self.settings.color_theme)

		self.placement()

		self.content_frame.grid_columnconfigure(0, weight = 1)
		self.content_frame.grid_rowconfigure(0, weight = 1)

	def placement(self):
		if self.settings.font == 'large':
			self.name_entry.configure(width = 45)
			self.name_entry.place(x = 0, y = 25)

			self.address_entry.configure(width = 45)
			self.address_entry.place(x = 0, y = 70)

			self.p_nmbr_entry.configure(width = 45)
			self.p_nmbr_entry.place(x = 0, y = 115)

			self.nmbr_entry.configure(width = 45)
			self.nmbr_entry.place(x = 0, y = 160)

			self.room_type_label.place(x = 350, y = 200)
			self.dlx_rad.place(x = 75, y = 235)
			self.dlx_rad_.place(x = 95, y = 238)

			self.nrml_rad.place(x = 250, y = 235)
			self.nrml_rad_.place(x = 270, y = 238)

			self.prsdt_rad.place(x = 425, y = 235)
			self.prsdt_rad_.place(x = 445, y = 238)

			self.jnt_rad.place(x = 600, y = 235)
			self.jnt_rad_.place(x = 620, y = 238)

			self.sumbit_buttton.place(x = 605, y = 355)

		elif self.settings.font == 'medium':
			self.name_entry.configure(width = 45)
			self.name_entry.place(x = 5, y = 20)

			self.address_entry.configure(width = 45)
			self.address_entry.place(x = 5, y = 65)

			self.p_nmbr_entry.configure(width = 45)
			self.p_nmbr_entry.place(x = 5, y = 110)

			self.nmbr_entry.configure(width = 45)
			self.nmbr_entry.place(x = 5, y = 155)

			self.room_type_label.place(x = 350, y = 200)
			self.dlx_rad.place(x = 75, y = 225)
			self.dlx_rad_.place(x = 95, y = 228 )

			self.nrml_rad.place(x = 250, y = 225)
			self.nrml_rad_.place(x = 270, y = 228)

			self.prsdt_rad.place(x = 425, y = 225)
			self.prsdt_rad_.place(x = 445, y = 228)

			self.jnt_rad.place(x = 600, y = 225)
			self.jnt_rad_.place(x = 620, y = 228)

			self.sumbit_buttton.place(x = 635, y = 365)

		elif self.settings.font == 'small':
			self.name_entry.configure(width = 55)
			self.name_entry.place(x = 0, y = 21)

			self.address_entry.configure(width = 55)
			self.address_entry.place(x = 0, y = 69)

			self.p_nmbr_entry.configure(width = 55)
			self.p_nmbr_entry.place(x = 0, y = 119)

			self.nmbr_entry.configure(width = 55)
			self.nmbr_entry.place(x = 0, y = 165)

			self.room_type_label.place(x = 350, y = 200)
			self.dlx_rad.place(x = 85, y = 225)
			self.dlx_rad_.place(x = 105, y = 227 )

			self.nrml_rad.place(x = 260, y = 225)
			self.nrml_rad_.place(x = 280, y = 227)

			self.prsdt_rad.place(x = 435, y = 225)
			self.prsdt_rad_.place(x = 455, y = 227)

			self.jnt_rad.place(x = 610, y = 225)
			self.jnt_rad_.place(x = 630, y = 227)

			self.sumbit_buttton.place(x = 685, y = 375)

	def check_out(self):
		self.settings.load_data()

		guest_name = self.name.get()
		guest_address = self.address.get()
		guset_phone = self.p_nmbr.get()
		room_type = self.room_type.get()
		no_room = self.nmbr.get()

		if room_type == 1:
			room_type = 'Delux'
		elif room_type == 2:
			room_type = 'Normal'
		elif room_type == 3:
			room_type = 'President'
		elif room_type == 4:
			room_type = 'Joint'

		self.check_filled()
		print(self.filled)

		if self.filled == True:
			cnt = 0
			room = f'{room_type}-{no_room}'

			for guest in self.settings.guest:
				for key, value in guest.items():
					if room == key:
						print('WORKSS')
						name_ = value.get('name')
						address_ = value.get('address')
						phone_ = value.get('p_nmbr')

						if name_ == guest_name and address_ == guest_address and phone_ == guset_phone:
							self.delete = True
							del self.settings.guest[cnt]
							self.settings.save_data()
							Msg.showinfo("Hotel Management", "Check Out Successed")
							self.app.check_out_page()
					else:
						cnt +=1

			if self.delete == False :
				Msg.showwarning("Hotel Management", "Guest doesn't exists")

		else:
			Msg.showwarning("Hotel Management", "Please Fill The Forum")

	def check_filled(self):
		guest_name = self.name.get()
		guest_address = self.address.get()
		guset_phone = self.p_nmbr.get()
		room_type = self.room_type.get()
		no_room = self.nmbr.get()

		if guest_name == '' or guest_address == '' or guset_phone == '' or room_type == '' or no_room == '' :
			self.filled = False
		else:
			self.filled = True