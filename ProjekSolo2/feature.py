from json import load, dump
from os import system 
from time import sleep
from getpass import getpass 
from datetime import datetime
from reportlab.pdfgen import canvas

fileUser = "akun.json"
fileDaftar = "barang.json"

user = {}
daftar = {}


def Oala():
	global user, daftar

	with open(fileUser) as nep:
		user = load(nep)

	with open(fileDaftar) as nep:
		daftar = load(nep)

	return True
def Alberto():
	global user, daftar

	with open(fileUser, "w") as f: 
		dump(user, f) 

	with open(fileDaftar, 'w') as f:
		dump(daftar, f)

	return True
def password():
	global user
	counter = 1
	build = input("Enter Username  : ")
	ghost = getpass("Enter Pass\t: ")
	KOKO = False
	DEDEK = False
	if build in user:
			KOKO = True
			DEDEK = (user[build] == ghost)
	
	while not KOKO or not DEDEK:
		counter += 1
		if counter > 3:
			return False
		print("User/Password Salah")
		build = input("Enter Username  : ")
		ghost = getpass("Enter Pass\t: ")
		if build in user:
			KOKO = True
			DEDEK = (user[build] == ghost)
		else:
			KOKO = False
			DEDEK = False
	else:
		print("\nLogin Pass")
		return True

def main():
	print("Welcome to Stock Contribution Machine\n")
	print("[1]. Melihat isi toko")
	print("[2]. Menambah barang secara detail")
	print("[3]. Menjual barang")
	print("[4]. Menambah stock barang")
	print("[5]. Menghapus semua detail barang")
	print("[6]. Mencari barang di toko")
	print("[7]. Export menjadi PDF")
	print("[0]. Keluar dari Program")

def isiToko():
	if len(daftar) > 0:
		no = 1
		for info in daftar:
				print(f"===============================================================================================================")
				print(f"{no}    |  {info}    |   {daftar[info][0]}\t      | {daftar[info][2]}      | {daftar[info][4]}           | {daftar[info][5]}           | {daftar[info][3]} ")
				no += 1
	else:
		print("\nStock Kosong")

def menambah():
	print("Menambah isi toko\n")
	waktu = datetime.now()
	isi = input("Menambahkan isi barang : ")
	dak = int(input("Berapa harganya     : "))
	Rak = int(input("Taro di Rak No : "))
	Jumlah = int(input("Jumlahnya : "))
	Expired = input("Masukkan Tanggal Expired : ")
	IDNYA  = ("%s%02d%2d%s%d" % (waktu.year, waktu.month, waktu.day, Jumlah,Rak))
	dates = ("%s-%s-%s" % (waktu.day, waktu.month, waktu.year))
	print("Saving...")
	daftar.update({isi:[dak,Rak,Jumlah,Expired,IDNYA,dates]})
	Alberto()
	sleep(1.5)
	print("Data Saved.")
def Menjual():
	if len(daftar) > 0:
		for info in daftar:
			print(f"\nIsinya \t: {info}\t")
	isi = input("Pilih barang yang ingin dijual : ")
			
	if isi in daftar:
		total = input("Masukkan jumlah barang yang ingin dibeli : ")
		#TotalJadi = (daftar[isi][2])-int(total)
		#del TotalJadi
		daftar[isi][2] -= int(total)
		Alberto()
		print("Menjual...")
		sleep(1.5)
		print("Barang telah terjual")

	else:
		print("Tidak ada di Rak mana pun")

def Tambah_stock():
	if len(daftar) > 0:
		for info in daftar:
			print(f"\nIsinya \t: {info}\t")
	isi = input("Pilih barang yang ingin ditambahkan : ")
			
	if isi in daftar:
		total = input("Masukkan jumlah barang yang ingin ditambahkan : ")
		#TotalJadi = (daftar[isi][2])-int(total)
		#del TotalJadi
		daftar[isi][2] += int(total)
		Alberto()
		print("Menambah...")
		sleep(1.5)
		print("Barang telah ditambahkan")

	else:
		print("Tidak ada di Rak mana pun")
def mencari():
	print("Mencari isi barang :\n")
	if len(daftar) > 0:
		for info in daftar:
			print(f"Barangnya \t: {info}\t")
	isi = input("\nMencari barang : ")

	if isi in daftar:
		print(f"{isi} ada di Rak Nomor : {daftar[isi][1]}")
	else:
		print(f"{isi} Tidak ada di Rak manapun")
		
def Menghapus():
	print("Menghapus Barang :")
	if len(daftar) > 0:
		for info in daftar:
			print(f"\nIsinya \t: {info}\t")

	isi = input("Pilih barang yang ingin dihapus : ")
	
	if isi in daftar:
		del daftar[isi]
		
		Alberto()
		print("Memhapus seluruh detail barang...")
		sleep(1.5)
		print("Telah terhapus")

	else:
		print("Tidak ada di Rak mana pun")

def JadiPDF():
		for info in daftar:
			DataBarang = {
				"Nama" : "Data",
				"Benda" : " Barang",
				"Laporan" : "Data Barang"
			}

			class Data:

				def __init__(self, filename, documentTitle, heading):
					self.filename = filename
					self.documentTitle = documentTitle
					self.heading = heading
					self.info = {}

			myData = Data(str(DataBarang["Nama"]+DataBarang["Benda"]+".pdf"), "List Product", DataBarang["Laporan"])
			myPDF = canvas.Canvas(myData.filename)
			myPDF.setTitle(myData.documentTitle)

			#Print on Papper
			myPDF.drawString(41,768,myData.heading) #x,y,heading


			myPDF.setFont("Helvetica", 30)
			myPDF.setFillColorRGB(0,0,0)
			myPDF.drawString(42,770,"")
			myPDF.line(30, 760, 560, 760)

			myText = myPDF.beginText(40,680)
			myText.setFont("Helvetica", 10)
			no = 1
			for info in daftar:
				nama = "Nama Barang : "+ info
				harga = "Harga (pcs) : "+ str(daftar[info][0])
				jumlah = "Jumlah : "+ str(daftar[info][2])
				ID = "ID Barang : " + str(daftar[info][4])
				Reg = "Tanggal Registrasi : " + daftar[info][5]
				Exp = "Tanggal Expired : " + daftar[info][3]
				garis = "================================="
				Lines = [nama,harga,jumlah,ID,Reg,Exp,garis]
			
				for line in Lines:
					myText.textLines(line)
				myPDF.drawText(myText)

			myPDF.save()
