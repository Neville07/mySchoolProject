# # from tkinter import PhotoImage
# # import tkinter as tk

# # # dictionary of colors:
# # color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

# # # setting root window:
# # root = tk.Tk()
# # root.title("Tkinter Navbar")
# # root.config(bg="gray17")
# # root.geometry("400x600+850+50")

# # # setting switch state:
# # btnState = False

# # # loading Navbar icon image:
# # navIcon = PhotoImage(file="menu.png")
# # closeIcon = PhotoImage(file="close.png")

# # # setting switch function:
# # def switch():
# #     global btnState
# #     if btnState is True:
# #         # create animated Navbar closing:
# #         for x in range(301):
# #             navRoot.place(x=-x, y=0)
# #             topFrame.update()

# #         # resetting widget colors:
# #         brandLabel.config(bg="gray17", fg="green")
# #         homeLabel.config(bg=color["orange"])
# #         topFrame.config(bg=color["orange"])
# #         root.config(bg="gray17")

# #         # turning button OFF:
# #         btnState = False
# #     else:
# #         # make root dim:
# #         brandLabel.config(bg=color["nero"], fg="#5F5A33")
# #         homeLabel.config(bg=color["nero"])
# #         topFrame.config(bg=color["nero"])
# #         root.config(bg=color["nero"])

# #         # created animated Navbar opening:
# #         for x in range(-300, 0):
# #             navRoot.place(x=x, y=0)
# #             topFrame.update()

# #         # turing button ON:
# #         btnState = True

# # # top Navigation bar:
# # topFrame = tk.Frame(root, bg=color["orange"])
# # topFrame.pack(side="top", fill=tk.X)

# # # Header label text:
# # homeLabel = tk.Label(topFrame, text="PE", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
# # homeLabel.pack(side="right")

# # # Main label text:
# # brandLabel = tk.Label(root, text="Pythonista\nEmpire", font="System 30", bg="gray17", fg="green")
# # brandLabel.place(x=100, y=250)

# # # Navbar button:
# # navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
# # navbarBtn.place(x=10, y=10)

# # # setting Navbar frame:
# # navRoot = tk.Frame(root, bg="blue", height=1000, width=300)
# # navRoot.place(x=-300, y=0)
# # tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# # # set y-coordinate of Navbar widgets:
# # y = 80
# # # option in the navbar:
# # options = ["Profile", "Settings", "Help", "About", "Feedback"]
# # # Navbar Option Buttons:
# # for i in range(5):
# #     tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
# #     y += 40

# # # Navbar Close Button:
# # closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
# # closeBtn.place(x=250, y=10)

# # # window in mainloop:
# # root.mainloop()

# # Imports each and every method and class
# # of module tkinter and tkinter.ttk
# from tkinter import *
# from tkinter.ttk import *

# class GFG:
# 	def __init__(self, master = None):
# 		self.master = master

# 		# Calls create method of class GFG
# 		self.create()

# 	def create(self):

# 		# This creates a object of class canvas
# 		self.canvas = Canvas(self.master)

# 		# This creates a line of length 200 (straight horizontal line)
# 		self.canvas.create_line(15, 225, 200, 225, fill = 'red')

# 		# This creates a lines of 300 (straight vertical dashed line)
# 		# self.canvas.create_line(300, 35, 300, 200, dash = (5, 2))
		
# 		# This creates a triangle (triangle can be created by other methods also)
# 		# self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
		
# 		# This pack the canvas to the main window and make it expandable
# 		self.canvas.pack(fill = BOTH, expand = True)

# if __name__ == "__main__":
	
# 	# object of class Tk, resposible for creating
# 	# a tkinter toplevel window
# 	master = Tk()
# 	geeks = GFG(master)

# 	# This sets the title to Lines
# 	master.title("Lines")

# 	# This sets the geometry and position of window
# 	# on the screen
# 	master.geometry("400x250+300+300")

# 	# Infnite loop breaks only by interrupt
# 	master.mainloop()

# Importing tkinter to make gui in python 
# from tkinter import*
  
# # Importing tkPDFViewer to place pdf file in gui. 
# # In tkPDFViewer library there is 
# # an tkPDFViewer module. That I have imported as pdf 
# from tkPDFViewer import tkPDFViewer as pdf 
  
# # Initializing tk 
# root = Tk() 
  
# # Set the width and height of our root window. 
# root.geometry("550x750") 
  
# # creating object of ShowPdf from tkPDFViewer. 
# v1 = pdf.ShowPdf() 
  
# # Adding pdf location and width and height. 
# v2 = v1.pdf_view(root, 
#                  pdf_location = r"guest.pdf",  
#                  width = 50, height = 100) 
  
# # Placing Pdf in my gui. 
# v2.pack() 
# root.mainloop()

# import os

# # Python program to create color chooser dialog box

# # importing tkinter module
# from tkinter import *

# # importing the choosecolor package
# from tkinter import colorchooser
# # trace_add

# # Function that will be invoked when the
# # button will be clicked in the main window
# def click(key):
# 	print(key)

# 	# # variable to store hexadecimal code of color
# 	# color_code = colorchooser.askcolor(title ="Choose color")
# 	# i = color_code[1]
# 	# button.configure(bg = i)

# root = Tk()
# c = StringVar()
# change_user = Entry(root).pack()
# change_user.bind("<Key>", click)

# root.geometry("300x300")
# root.mainloop()

# from tkinter import Tk, Entry

# root = Tk()
# a = [""]

# def click(key):
# 	global a
# 	# print the key that was pressed 
# 	for i in a:
# 		i += (str(key.char))
# 	a.append(i)
# 	b =a[len(a)-1]

# 	if len(b) <= 1 :
# 		print(b[0])
# 	else:
# 		c = len(b)
# 		print(b[c-1])

# entry = Entry()
# entry.grid()
# # Bind entry to any keypress
# entry.bind("<Key>", click)

# root.mainloop()
# str1 = input("Enter :")
# list1 = list(str1)
# print(list1)
# list2 = list1[:-1]
# str2 = ''
# for i in list2:
# 	str2 += i

# print(str2)

# def rgb_to_hex(rgb):
#     return '%02x%02x%02x' % rgb
# print(rgb_to_hex((255, 255, 195)))

# def hex_to_rgb(value = "#f07b52"):
#     value = value.lstrip('#')
#     lv = len(value)
#     return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
# a = hex_to_rgb()
# print(a[0]-15)


# import os

# import shutil

# def copy_rename(old_file_name, new_file_name):

#         src_dir= os.curdir

#         dst_dir= os.path.join(os.curdir , "subfolder")

#         src_file = os.path.join(src_dir, old_file_name)

#         shutil.copy(src_file,dst_dir)

        

#         dst_file = os.path.join(dst_dir, old_file_name)

#         new_dst_file_name = os.path.join(dst_dir, new_file_name)

#         os.rename(dst_file, new_dst_file_name)

# copy_rename('guest.pdf', 'a.pdf')

# # Importing the modules
# import os
# import shutil

# src_dir = os.getcwd() #get the current working dir
# print(src_dir)

# # # create a dir where we want to copy and rename
# # dest_dir = os.mkdir('subfolder')
# # os.listdir()

# dest_dir = src_dir+"/pdf"
# src_file = os.path.join(src_dir, 'login.py')
# shutil.copy(src_file,dest_dir) #copy the file to destination dir

# dst_file = os.path.join(dest_dir,'login.py')
# new_dst_file_name = os.path.join(dest_dir, 'login1.py')

# os.rename(dst_file, new_dst_file_name)#rename
# os.chdir(dest_dir)

# # print(os.listdir())
# print(dst_file)


# # importing all files from tkinter
# from tkinter import *
# from tkinter import ttk

# # import only asksaveasfile from filedialog
# # which is used to save file in any extension
# from tkinter.filedialog import asksaveasfile

# root = Tk()
# root.geometry('200x150')

# # function to call when user press
# # the save button, a filedialog will
# # open and ask to save file
# def save():
# 	files = [('All Files', '*.*'),
# 			('Python Files', '*.py'),
# 			('Text Document', '*.txt')]
# 	file = asksaveasfile(filetypes = files, defaultextension = files)
# 	print(file)

# btn = ttk.Button(root, text = 'Save', command = lambda : save())
# btn.pack(side = TOP, pady = 20)

# mainloop()


from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")),  defaultextension = (("pdf files","*.pdf"),("all files","*.*")))
print (root.filename)

list1 = list(root.filename)
str1 = ''
str2 = ''
str_dir = ''

cnt = 0
for i in list1:
	if i == '/':
		cnt +=1
c = 0
count = 0
for j in list1:
	if j == '/':
		c += 1
	if c == cnt:
		count +=1
		str1+=j

dir_ = list1[:-(len(str1)-1)]

for a in dir_:
	str_dir += a

name = list(str1)

for i in name:
	if i != '/':
		str2 += i


print(root.filename)
print(str1)
print(str_dir)
print(str2)