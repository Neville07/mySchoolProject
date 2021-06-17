import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import messagebox as Msg

class CheckIn(tk.Frame):

	def __init__(self, parent, App): #self.container, self.app

		self.app = App
		self.settings = App.settings

		super().__init__(parent)
		self.configure(bg=self.settings.board_color)
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		# virtual image
		self.virtual_image = tk.PhotoImage(width = 1, height = 1)

		self.info = {}
		self.filled = False

		self.create_header()
		self.create_content()

	def create_header(self):
		frame_h =self.settings.height//5

		self.header_frame = tk.Frame(self, bg = self.settings.board_color, width = self.settings.width, height = frame_h)
		self.header_frame.pack(fill = "x")

		self.back_frame = tk.Frame(self.header_frame, bg = self.settings.board_color, width = self.settings.width//10, height = frame_h//2)
		self.back_frame.grid(row = 0, column = 0, sticky = "ne")

		self.header_frame_ = tk.Frame(self.header_frame, bg = self.settings.board_color, width = 9*self.settings.width//10, height = frame_h)
		self.header_frame_.grid(row = 0, column = 1, sticky = 'nsew')

		self.header_label = tk.Label(self.header_frame_, text = "Check In", fg = self.settings.font_color, bg = self.settings.board_color ,font = self.settings.header_font, image = self.virtual_image, compound = "c")
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

	def create_content(self):
		frame_h = self.settings.height//3
		width = self.settings.width

	# name, address, phone number, day
		self.content_frame = tk.Frame(self, bg = self.settings.board_color)
		self.content_frame.pack(fill = "both", expand = True)

		self.detail_frame = tk.Frame(self.content_frame, bg = self.settings.board_color, width = width//3, height = frame_h)
		self.detail_frame.grid(sticky = 'ne', row = 0, column = 0)

		self.details_label = []

		details = ['name :', 'address :', 'phone number :', 'day :']
		y = 0
		for detail in details:
			label = tk.Label(self.detail_frame, text=detail, bg=self.settings.board_color, fg=self.settings.font_color, font=self.settings.content_font)
			if self.settings.font == 'large':
				label.place(x = 95, y = y)
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

		self.day = tk.StringVar()
		self.day_entry =tk.Entry(self.entry_frame, fg='black', font=self.settings.content_font,width = 45, textvariable = self.day)

	# room type
		self.room_type_label = tk.Label(self.content_frame, text= "room type :", bg=self.settings.board_color, fg=self.settings.font_color, font=self.settings.content_font)
		self.room_type_label.place(x = 350, y = 180)

		self.room_type = tk.IntVar()

		self.dlx_rad = tk.Radiobutton(self.content_frame, text = "delux", value = 1, font=self.settings.content_font, variable = self.room_type, bg = self.settings.board_color, activebackground = self.settings.board_color )
		self.dlx_rad_ = tk.Label(self.content_frame, text = "delux", font=self.settings.content_font,  bg = self.settings.board_color, fg = self.settings.font_color)
		
		self.nrml_rad = tk.Radiobutton(self.content_frame, text = "normal", value = 2, font=self.settings.content_font, variable = self.room_type, bg = self.settings.board_color, activebackground = self.settings.board_color)
		self.nrml_rad_ = tk.Label(self.content_frame, text = "normal", font=self.settings.content_font, bg = self.settings.board_color, fg = self.settings.font_color)

		self.prsdt_rad = tk.Radiobutton(self.content_frame, text = "president", value = 3, font=self.settings.content_font, variable = self.room_type , bg = self.settings.board_color, activebackground = self.settings.board_color)
		self.prsdt_rad_ = tk.Label(self.content_frame, text = "president", font=self.settings.content_font, bg = self.settings.board_color, fg = self.settings.font_color)
		
		self.jnt_rad = tk.Radiobutton(self.content_frame, text = "joint", value = 4, font=self.settings.content_font, variable = self.room_type , bg = self.settings.board_color, activebackground = self.settings.board_color)
		self.jnt_rad_ = tk.Label(self.content_frame, text = "joint",font=self.settings.content_font, bg = self.settings.board_color, fg = self.settings.font_color)
		
		self.pymnt_label = tk.Label(self.content_frame, text= "payment :", bg=self.settings.board_color, fg=self.settings.font_color, font=self.settings.content_font)
		
		self.payment = tk.IntVar()

		self.cash_rad = tk.Radiobutton(self.content_frame, text = 'by cash',  value = 1, font=self.settings.content_font, variable = self.payment, bg = self.settings.board_color, activebackground = self.settings.board_color)
		self.cash_rad_ = tk.Label(self.content_frame, text = 'by cash', font=self.settings.content_font, bg = self.settings.board_color, fg = self.settings.font_color)
		
		self.card_rad = tk.Radiobutton(self.content_frame, text = 'by credit / debit card',  value = 2, font=self.settings.content_font, variable = self.payment, bg = self.settings.board_color, activebackground = self.settings.board_color)
		self.card_rad_ = tk.Label(self.content_frame, text = 'by credit / debit card', font=self.settings.content_font, bg = self.settings.board_color, fg = self.settings.font_color)
		
		self.sumbit_buttton = tk.Button(self.content_frame, text = "Sumbit", font = self.settings.content_font, bd = 0, width = 15, bg = self.settings.color_theme, fg = self.settings.board_color, command = self.sumbit, activebackground = self.settings.color_theme)
		
		self.placement()

		self.content_frame.grid_columnconfigure(0, weight = 1)
		self.content_frame.grid_rowconfigure(0, weight = 1)

	def placement(self):
		if self.settings.font == 'large':
			self.name_entry.configure(width = 45)
			self.name_entry.place(x = 5, y = 5)

			self.address_entry.configure(width = 45)
			self.address_entry.place(x = 5, y = 50)

			self.p_nmbr_entry.configure(width = 45)
			self.p_nmbr_entry.place(x = 5, y = 95)

			self.day_entry.configure(width = 45)
			self.day_entry.place(x = 5, y = 140)

			self.dlx_rad.place(x = 75, y = 205)
			self.dlx_rad_.place(x = 95, y = 208)

			self.nrml_rad.place(x = 250, y = 205)
			self.nrml_rad_.place(x = 270, y = 208)

			self.prsdt_rad.place(x = 425, y = 205)
			self.prsdt_rad_.place(x = 445, y = 208)

			self.jnt_rad.place(x = 600, y = 205)
			self.jnt_rad_.place(x = 620, y = 208)

			self.pymnt_label.place(x = 350, y = 240)
			self.cash_rad.place(x = 200, y = 270)
			self.cash_rad_.place(x = 220, y = 273)

			self.card_rad.place(x = 400, y = 270)
			self.card_rad_.place(x = 420, y = 273)

			self.sumbit_buttton.place(x = 605, y = 355)

		elif self.settings.font == 'medium':
			self.name_entry.configure(width = 45)
			self.name_entry.place(x = 5, y = 5)

			self.address_entry.configure(width = 45)
			self.name_entry.place(x = 5, y = 5)

			self.address_entry.configure(width = 45)
			self.address_entry.place(x = 5, y = 50)

			self.p_nmbr_entry.configure(width = 45)
			self.p_nmbr_entry.place(x = 5, y = 95)

			self.day_entry.configure(width = 45)
			self.day_entry.place(x = 5, y = 140)

			self.dlx_rad.place(x = 75, y = 205)
			self.dlx_rad_.place(x = 95, y = 208 )

			self.nrml_rad.place(x = 250, y = 205)
			self.nrml_rad_.place(x = 270, y = 208)

			self.prsdt_rad.place(x = 425, y = 205)
			self.prsdt_rad_.place(x = 445, y = 208)

			self.jnt_rad.place(x = 600, y = 205)
			self.jnt_rad_.place(x = 620, y = 208)

			self.pymnt_label.place(x = 350, y = 240)
			self.cash_rad.place(x = 200, y = 270)
			self.cash_rad_.place(x = 220, y = 273)

			self.card_rad.place(x = 400, y = 270)
			self.card_rad_.place(x = 420, y = 273)

			self.sumbit_buttton.place(x = 635, y = 365)

		elif self.settings.font == 'small':
			self.name_entry.configure(width = 55)
			self.name_entry.place(x = 0, y = 1)

			self.address_entry.configure(width = 55)
			self.address_entry.place(x = 0, y = 48)

			self.p_nmbr_entry.configure(width = 55)
			self.p_nmbr_entry.place(x = 0, y = 97)

			self.day_entry.configure(width = 55)
			self.day_entry.place(x = 0, y = 145)

			self.dlx_rad.place(x = 85, y = 205)
			self.dlx_rad_.place(x = 105, y = 207 )

			self.nrml_rad.place(x = 260, y = 205)
			self.nrml_rad_.place(x = 280, y = 207)

			self.prsdt_rad.place(x = 435, y = 205)
			self.prsdt_rad_.place(x = 455, y = 207)

			self.jnt_rad.place(x = 610, y = 205)
			self.jnt_rad_.place(x = 630, y = 207)

			self.pymnt_label.place(x = 350, y = 240)
			self.cash_rad.place(x = 200, y = 270)
			self.cash_rad_.place(x = 220, y = 273)

			self.card_rad.place(x = 400, y = 270)
			self.card_rad_.place(x = 420, y = 273)
			self.sumbit_buttton.place(x = 685, y = 375)

	def sumbit(self):
		guest_name = self.name.get()
		guest_address = self.address.get()
		guset_phone = self.p_nmbr.get()
		day_stay = self.day.get()
		room_type = self.room_type.get()
		pymnt = self.payment.get()

		room_number = random.randint(1,10)

		if room_type == 1:
			room_type = 'Delux'
		elif room_type == 2:
			room_type = 'Normal'
		elif room_type == 3:
			room_type = 'President'
		elif room_type == 4:
			room_type = 'Joint'

		if pymnt == 1:
			pymnt = 'cash'
		elif pymnt == 2:
			pymnt = 'card'

		self.check_filled()

		if self.filled == True:
			info = {f'{room_type}-{room_number}' : {'name':guest_name, 'address' : guest_address, 'p_nmbr' : guset_phone, 'day' : day_stay, 'payment' : pymnt}}
			self.settings.guest.append(info)
			self.settings.save_data()
			Msg.showinfo("Hotel Management", "Check In Successed")
			self.app.check_in_page()

		else:
			Msg.showwarning("Hotel Management", "Please Fill The Forum")

	def check_filled(self):
		guest_name = self.name.get()
		guest_address = self.address.get()
		guset_phone = self.p_nmbr.get()
		day_stay = self.day.get()
		room_type = self.room_type.get()
		pymnt = self.payment.get()

		if guest_name == '' or guest_address == '' or guset_phone == '' or day_stay == '' or room_type == '' or pymnt == '' :
			self.filled = False
		else:
			self.filled = True
