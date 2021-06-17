import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class AppPage(tk.Frame):

	def __init__(self, parent, App): #self.container, self.app
		self.app = App
		self.settings = App.settings
		self.current_contact = self.settings.guest[0]
		self.last_current_index = 0
		self.update_mode = False
		self.guest_index = []

		super().__init__(parent)
		self.configure(bg=self.settings.board_color)
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_left_frame()
		self.create_right_frame()
		self.config_left_right_frame()

	def create_left_frame(self):
		self.left_frame = tk.Frame(self, bg=self.settings.board_color, width=self.settings.width//3)
		self.left_frame.grid(row=0, column=0, sticky="nsew")
		self.create_left_header()
		self.create_left_content()

	def create_right_frame(self):
		self.right_frame = tk.Frame(self, bg=self.settings.board_color, width=2*self.settings.width//3)
		self.right_frame.grid(row=0, column=1, sticky="nsew")
		self.create_right_header()
		self.create_right_content()
		self.create_right_footer()

	def config_left_right_frame(self):
		self.grid_columnconfigure(0, weight=1) # 1/3
		self.grid_columnconfigure(1, weight=2) # 2/3
		self.grid_rowconfigure(0, weight=1)

	def create_left_header(self):
		frame_w = self.settings.width//3
		frame_h = self.settings.height//6
		
		self.virt_img = tk.PhotoImage(width=1, height=1)

		self.header_frame = tk.Frame(self.left_frame, bg=self.settings.board_color, width=frame_w, height=frame_h)
		self.header_frame.pack(fill="x")

		self.back_frame = tk.Frame(self.header_frame, bg = self.settings.board_color, width = self.settings.width//12, height = self.settings.height//8)
		# self.back_frame.grid(row = 0, column = 0, sticky = "ne")
		self.back_frame.pack(side = 'left')

		self.back_photo = tk.PhotoImage(file=self.settings.back_img)
		image = Image.open(self.settings.back_img)
		image_w, image_h = image.size
		ratio = 12
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.back_photo = ImageTk.PhotoImage(image)

		self.back = tk.Button(self.back_frame, image = self.back_photo, bd = 0, bg = self.settings.board_color, command=self.app.back, width = self.settings.width//19, height = 19, activebackground = self.settings.board_color)
		self.back.grid(row = 0, column = 0, sticky = 'nsew', pady = (7, 22), padx = 2)

		self.header_frame_ = tk.Frame(self.header_frame, bg = self.settings.board_color, height = frame_h,width = self.settings.width//8)
		self.header_frame_.pack(expand = True, fill = 'both', side = 'right')

		self.label_logo = tk.Label(self.header_frame_, text = "Guest Info",  bg=self.settings.board_color, fg=self.settings.font_color, font=self.settings.apppage_header_font)
		self.label_logo.grid(row = 0, column = 0, sticky = 'nsew', padx = (15,0))
		# self.label_logo.pack()

		self.searchbox_frame = tk.Frame(self.left_frame, bg=self.settings.board_color, width=frame_w, height=frame_h)
		self.searchbox_frame.pack(fill="x")

		self.entry_search_var = tk.StringVar()
		self.entry_search = tk.Entry(self.searchbox_frame, bg="white", fg='black', font=self.settings.content_font, textvariable = self.entry_search_var)
		self.entry_search.grid(row=0, column=0)

		self.button_search = tk.Button(self.searchbox_frame, bg = self.settings.color_theme, fg = self.settings.board_color, font=self.settings.content_font, text="find", width = 5, bd = 1//2, command=self.clicked_search_btn, activebackground = self.settings.color_theme)
		self.button_search.grid(row=0, column=1)

		self.searchbox_frame.grid_columnconfigure(0, weight=3) # 3/4
		self.searchbox_frame.grid_columnconfigure(1, weight=1) # 1/4

	def show_current_guest_index_in_listbox(self):
		self.contact_listBox.delete(0, 'end')
		guests =self.settings.guest
		for index in self.guest_index:
			guest = guests[index]
			for key, value in guest.items():
				i = f"{key} - {value['name']}"
				self.contact_listBox.insert("end", i)

	def show_all_contacts_in_listbox(self):
		self.contact_listBox.delete(0, 'end')
		guests = self.settings.guest
		self.guest_index = []
		index_counter = 0

		for guest in guests:
			self.guest_index.append(index_counter)
			index_counter += 1

		for guest in guests:
			for key, value in guest.items():
				i = f"{key} - {value['name']}"
				self.contact_listBox.insert("end", i)

	def create_left_content(self):
		frame_w = self.settings.width//3
		frame_h = 3*self.settings.height//4

		self.left_content = tk.Frame(self.left_frame, width=frame_w, height=frame_h, bg="white")
		self.left_content.pack(fill="x")

		self.contact_listBox = tk.Listbox(self.left_content, bg="white", fg="black", font=self.settings.content_font, height=self.settings.height)
		self.contact_listBox.pack(side="left", fill="both", expand=True)

		self.contacts_scroll = tk.Scrollbar(self.left_content)
		self.contacts_scroll.pack(side="right", fill="y")

		self.show_all_contacts_in_listbox()
		
		self.contact_listBox.configure(yscrollcommand=self.contacts_scroll.set)
		self.contacts_scroll.configure(command=self.contact_listBox.yview)

		self.contact_listBox.bind("<<ListboxSelect>>", self.clicked_item_in_Listbox)

	def clicked_item_in_Listbox(self, event):
		if not self.update_mode:
			selection = event.widget.curselection()
			try:
				index_listbox = selection[0]
				
			except IndexError:
				index_listbox = self.last_current_index

			index = self.guest_index[index_listbox]
			self.last_current_index = index
			self.current_contact = self.settings.guest[index]
			for key, info in self.current_contact.items() :
				room = key
				name = info['name']
				address = info['address']
				p_nmbr = info['p_nmbr']
				day = info['day']
				payment = info['payment']

				self.header_label.configure(text = room)
				self.table_info[0][1].configure(text = name)
				self.table_info[1][1].configure(text = address)
				self.table_info[2][1].configure(text = p_nmbr)
				self.table_info[3][1].configure(text = day)
				self.table_info[4][1].configure(text = payment)

	def create_right_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//6

		self.right_header = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="#f5f5f8")
		self.right_header.pack()

		self.create_detail_right_header()

	def create_detail_right_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//6
		self.detail_header = tk.Frame(self.right_header, width=frame_w, height=frame_h, bg=self.settings.board_color)
		self.detail_header.grid(row=0, column=0, sticky="nsew")

		for Room, info in self.current_contact.items() :
			room = Room

		self.virt_img = tk.PhotoImage(width=1, height=1)
		self.header_label = tk.Label(self.detail_header, text=room, font=self.settings.apppage_header_font , width=frame_w, height=frame_h, image=self.virt_img, compound="c", bg=self.settings.board_color, fg = self.settings.font_color)
		self.header_label.pack()

		self.right_header.grid_columnconfigure(0, weight=1)
		self.right_header.grid_rowconfigure(0, weight=1)

	def create_right_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4 

		self.right_content = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg=self.settings.board_color)
		self.right_content.pack(expand=True)

		self.create_detail_right_content()

	def create_detail_right_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4 

		self.detail_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg=self.settings.board_color)
		self.detail_content.grid(row=0, column=0, sticky="nsew")

		for room, info in self.current_contact.items() :
			info = [
				['Name :', info['name']],
				['Addrres :', info['address']],
				['Phone Number :', info['p_nmbr']],
				['Day :', info['day']],
				['Payment :', info['payment']]
			]

		self.table_info = []

		rows , columns = len(info), len(info[0])
		for row in range(rows):
			aRow = []
			for column in range(columns):
				label = tk.Label(self.detail_content, text=info[row][column], font=self.settings.content_font, bg=self.settings.board_color, fg = self.settings.font_color)
				aRow.append(label)
				if column == 0:
					sticky = "e"
				else:
					sticky = "w"
				label.grid(row=row, column=column, sticky=sticky)
			self.table_info.append(aRow)


		self.right_content.grid_columnconfigure(0, weight=1)
		self.right_content.grid_rowconfigure(0, weight=1)

	def create_right_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4 

		self.right_footer = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg=self.settings.board_color)
		self.right_footer.pack()

		self.create_detail_right_footer()

	def create_detail_right_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4 

		self.detail_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg=self.settings.board_color)
		self.detail_footer.grid(row=0, column=0, sticky="nsew")

		features = ['Edit','Delete']
		commands = [self.clicked_edit_btn, self.clicked_delete_btn]
		self.buttons_features = []

		for feature in features:
			button = tk.Button(self.detail_footer, text=feature,bg = self.settings.color_theme, fg = self.settings.board_color, font=self.settings.content_font, bd=1//2, width = 9, command = commands[features.index(feature)], activebackground = self.settings.color_theme)
			if features.index(feature) == 0:
				padx=(1,115)
			elif features.index(feature) == 1:
				padx=(115,1)

			button.grid(row=0, column=features.index(feature), sticky="nsew", padx=padx, pady=(0, 10))
			self.buttons_features.append(button)

		self.right_footer.grid_columnconfigure(0, weight=1)
		self.right_footer.grid_rowconfigure(0, weight=1)

	def recreate_right_frame_and_listbox(self):
		self.detail_header.destroy()
		self.detail_update_content.destroy()
		self.detail_update_footer.destroy()

	#recreate header
		self.create_detail_right_header()

	# recreate content
		self.create_detail_right_content()

	#recreate footer

		self.create_detail_right_footer()

		self.contact_listBox.delete(0, 'end')
		self.show_all_contacts_in_listbox()


	def clicked_edit_btn(self):
		self.update_mode = True

		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4

		self.detail_content.destroy()
		self.detail_footer.destroy()

		self.detail_update_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg=self.settings.board_color)
		self.detail_update_content.grid(row=0, column=0, sticky="nsew")

		for Room, info in self.current_contact.items() :
			info = [
				['Room :', Room],
				['Name :', info['name']],
				['Addrres :', info['address']],
				['Phone Number :', info['p_nmbr']],
				['Day :', info['day']],
				['Payment :', info['payment']]
			]

		self.table_info = []
		self.entry_update_vars = []

		rows , columns = len(info), len(info[0])
		for row in range(rows):
			aRow = []
			for column in range(columns):
				if column == 0:
					label = tk.Label(self.detail_update_content, text=info[row][column], font=self.settings.content_font, bg=self.settings.board_color, fg = self.settings.font_color)
					aRow.append(label)
					sticky = "e"
					label.grid(row=row, column=column, sticky=sticky)
				else:
					entryVar = tk.StringVar()
					entry = tk.Entry(self.detail_update_content, font=self.settings.content_font, bg="white", textvariable = entryVar)
					entry.insert(0, info[row][column])
					self.entry_update_vars.append(entryVar)
					aRow.append(entry)
					sticky = "w"
					entry.grid(row=row, column=column, sticky=sticky)
				
			self.table_info.append(aRow)
	#footer
		self.detail_update_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg=self.settings.board_color)
		self.detail_update_footer.grid(row=0, column=0, sticky="nsew")

		features = ['Cancel', 'Save']
		commands = [self.clicked_cancel_btn, self.clicked_save_btn]
		self.buttons_features = []

		for feature in features:
			index =features.index(feature)
			button = tk.Button(self.detail_update_footer, text=feature,bg = self.settings.color_theme, fg = self.settings.board_color, font=self.settings.content_font, bd=1//2, width = 9, command = commands[index], activebackground = self.settings.color_theme)
			if features.index(feature) == 0:
				padx=(1,115)
			elif features.index(feature) == 1:
				padx=(115,1)

			button.grid(row=0, column=index, sticky="nsew", padx=padx, pady=(0, 10))
			self.buttons_features.append(button)

		self.right_content.grid_columnconfigure(0, weight=1)
		self.right_content.grid_rowconfigure(0, weight=1)

	def clicked_save_btn(self):
		self.update_mode = False

		confirm = messagebox.askyesnocancel("Contactapp Confirmation", "Are you sure to update this contact?")
		if confirm:
			room = self.entry_update_vars[0].get()
			name = self.entry_update_vars[1].get()
			address = self.entry_update_vars[2].get()
			phone = self.entry_update_vars[3].get()
			day = self.entry_update_vars[4].get()
			payment = self.entry_update_vars[5].get()
			self.settings.guest[self.last_current_index] = {
				room :{
					'name' : name,
					'address' : address,
					'p_nmbr' : phone,
					'day' : day,
					'payment' : payment
				}
			}
			self.settings.save_data()

			self.current_contact = self.settings.guest[self.last_current_index]

		self.recreate_right_frame_and_listbox()

	def clicked_search_btn(self):
		item_search = self.entry_search_var.get()
		guests = self.settings.guest
		self.guest_index = []
		index_counter = 0

		if item_search:
			for guest in guests:
				for key, info in guest.items():
					room = key
					name = info['name']
					address = info['address']
					p_nmbr = info['p_nmbr']

					if item_search in key:
						self.guest_index.append(index_counter)
					elif item_search in name:
						self.guest_index.append(index_counter)
					elif item_search in address:
						self.guest_index.append(index_counter)
					elif item_search in p_nmbr:
						self.guest_index.append(index_counter)
				index_counter +=1
			self.show_current_guest_index_in_listbox()
		else:
			self.show_all_contacts_in_listbox()

	def clicked_delete_btn(self):
		confirm = messagebox.askyesnocancel("Hotel Management Confirmation", "Are you sure to delete this contact?")
		if confirm:
			
			del self.settings.guest[self.last_current_index]
			self.settings.save_data()
			self.contact_listBox.delete(0, 'end')

			self.show_all_contacts_in_listbox()

			self.detail_header.destroy()
			self.detail_content.destroy()
			self.current_contact = self.settings.guest[0]

			self.create_detail_right_header()
			self.create_detail_right_content()

	def clicked_cancel_btn(self):
		self.update_mode = False
		self.recreate_right_frame_and_listbox()
