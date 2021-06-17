from json import load, dump
from os import system 
from time import sleep

import feature

status = feature.Oala()

if status :
	system("cls")
	ghost = feature.password()
	if ghost:
		print("Selamat datang")
		sleep(0.5)
		system("cls")
		generation = ""
		while generation != "0":
			system("cls")
			sleep(1.0)
			feature.main()
			generation = input("Pilih Opsinya : ")

			if generation == "1":
				system("cls")
				print(f"No   |  Barang       |  Harga (pcs)   |  Jumlah | ID Barang             | Tanggal Registrasi  | Tanggal Expired ")
				feature.isiToko()
				input("ENTER TO EXIT")

			elif generation == "2":
				feature.menambah()
				input("ENTER TO EXIT")
			elif generation == "3":
				feature.Menjual()
				input("ENTER TO EXIT")
			elif generation == "4":
				feature.Tambah_stock()
				input("ENTER TO EXIT")
			elif generation == "5":
				feature.Menghapus()
				input("ENTER TO EXIT")
			elif generation == "6":
				feature.mencari()
				input("\nENTER TO EXIT")
			elif generation == "7":
				feature.JadiPDF()
			elif generation == "0":
				break

			else:
				print("Input Menu Yang Benar")
				input("ENTER untuk keluar")
				