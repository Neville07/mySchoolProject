import tkinter as tk
import os
import shutil
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from tkPDFViewer import tkPDFViewer

class PrintGuest(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings
		self.dwnld = False

		super().__init__(parent)
		self.configure(bg=self.settings.board_color)
		self.grid(row=0, column=0, sticky="nsew")

		self.view()

	def view(self):
		self.print()

		self.header_frame = tk.Frame(self, width = self.settings.width, height = self.settings.height//8, bg = self.settings.board_color)
		self.header_frame.grid(row = 0, column = 0)

		self.back_photo = tk.PhotoImage(file=self.settings.back_img)
		image = Image.open(self.settings.back_img)
		image_w, image_h = image.size
		ratio = 12
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.back_photo = ImageTk.PhotoImage(image)

		self.back = tk.Button(self.header_frame, image = self.back_photo, bd = 0, bg = self.settings.board_color, command=self.app.back_print, height = self.settings.height//8//2, width = self.settings.width//10, activebackground = self.settings.board_color)
		self.back.place(x = 5, y = 5)

		self.download_photo = tk.PhotoImage(file=self.settings.download_img)
		image = Image.open(self.settings.download_img)
		image_w, image_h = image.size
		ratio = 6
		new_size = (int(image_w//ratio), int(image_h//ratio))
		image = image.resize(new_size)
		self.download_photo = ImageTk.PhotoImage(image)

		self.download = tk.Button(self.header_frame, image = self.download_photo, bd = 0, bg = self.settings.board_color, height = self.settings.height//12, width = self.settings.width//12, command = self.download, activebackground = self.settings.board_color)
		self.download.place(x = self.settings.width - 95, y = 7)

		self.show_frame = tk.Frame(self, width = self.settings.width, height = 7*self.settings.height//8, bg = self.settings.board_color)
		self.show_frame.grid(row = 1, column = 0)

		view = tkPDFViewer.ShowPdf()
		self.show = view.pdf_view(self.show_frame, pdf_location = 'pdf/guest.pdf', width = 75, height = 27)
		self.show.pack()


	def download(self):
		self.dwnld = True
		print('downloaded')
		filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")),  defaultextension = (("pdf files","*.pdf"),("all files","*.*")))
		print (filename)

		list1 = list(filename)
		tmp_str = ''
		str_dir = ''
		str_name = ''

		cnt1 = 0
		for i in list1:
			if i == '/':
				cnt1 +=1

		cnt2 = 0
		for j in list1:
			if j == '/':
				cnt2 += 1
			if cnt2 == cnt1:
				tmp_str+=j

		dir_ = list1[:-(len(tmp_str)-1)]

		for a in dir_:
			str_dir += a

		name = list(tmp_str)

		for i in name:
			if i != '/':
				str_name += i

		print(str_name)
		print(str_dir)

		pdf_dir = os.getcwd() + '/pdf'
		print(pdf_dir)

		pdf_file = os.path.join(pdf_dir, 'guest.pdf')
		shutil.copy(pdf_file,str_dir)
		dst_file = os.path.join(str_dir,'guest.pdf')
		new_dst_file_name = os.path.join(str_dir, str_name)
		os.rename(pdf_file, new_dst_file_name)
		os.remove(str_dir+'guest.pdf')


	def print(self):
		self.myPdf = canvas.Canvas("pdf/guest.pdf")
		self.myPdf.setTitle("GUEST")

		self.myPdf.setFont("Courier", 30)
		self.myPdf.setFillColorRGB(0,0,0)
		self.myPdf.drawCentredString(300,770,"List Guest")
		self.myPdf.line(30,760, 580, 760)

		self.myText = self.myPdf.beginText(35,680)
		self.myText.setFont("Courier", 18)

		no = 1
		for dic in self.settings.guest:
			for key, info in dic.items() :
				room = str(no) + ". Room :" + key
				name = "Name :" + info['name']
				add = "Address :" + info['address']
				p_nmbr = "Phone :" + info['p_nmbr']
				day = "Day :" + info['day']
				no +=1
				garis = self.myPdf.line(30,760, 580, 760)
				Lines = [room,name,add,p_nmbr,day,garis]

				for line in Lines:
					self.myText.textLine(line)

		self.myPdf.drawText(self.myText)		
		self.myPdf.save()

