from reportlab.pdfgen import canvas

dataSiswa = {
	"Nama" : "Neville",
	"Kelas" : " 8.2",
	"Laporan" : "Raport Kelas 8 Semester 2"
}
class Data:

	def __init__(self, filename, documentTitle, heading):
		self.filename = filename
		self.documentTitle = documentTitle
		self.heading = heading

myData = Data(str(dataSiswa["Nama"]+dataSiswa["Kelas"]+".pdf"), "Hasil Ujian", dataSiswa["Laporan"])
myPDF = canvas.Canvas(myData.filename)
myPDF.setTitle(myData.documentTitle)

#Print on Papper
myPDF.drawString(227,780,myData.heading) #x,y,heading

myPDF.save()
#print("OK")