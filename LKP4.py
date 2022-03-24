import matplotlib.pyplot as plt

print(' ')
print('='*57)
print('Selamat Datang di Program Pendataan Warga Desa Cijujung')
print(57*'=')
print(' ')
userpass={'Cijujung':'1313'}
userid=input('Username : ')
password=input('Password : ')
if userid in userpass and password == userpass[userid]:
    print('Login Berhasil')
else:
    print('Login gagal')
    quit()

print(' ')

class WargaDesaCijujung :
  jumlahwarga = 0
  def __init__(self, nama, usia, nik, status) :
    self.nama = nama
    self.usia = usia
    self.nik = nik
    self.status = status
    WargaDesaCijujung.jumlahwarga += 1

  def keterangan(self) :
      return f'Nama\t\t: {self.nama} \nUsia\t\t: {self.usia} \nNIK\t\t:, {self.nik}'
  
class dataBPJS(WargaDesaCijujung) :
  jumlahBPJS = 0
  def __init__(self,nama,usia,nobpjs,nik,status) :
    WargaDesaCijujung.__init__(self,nama,usia,nik,status)
    self.nobpjs = nobpjs
    dataBPJS.jumlahBPJS += 1
  
  def keterangan(self) :
      return f'Nama\t\t: {self.nama} \nUsia\t\t: {self.usia} \nNIK\t\t: {self.nik} \nNo. BPJS\t: {self.nobpjs} \nStatus\t\t: {self.status}'

class dataNonBPJS(WargaDesaCijujung) :
  jumlahnonbpjs = 0
  def __init__(self,nama,usia,nik,status) :
    super().__init__(nama,usia,nik,status)
    dataNonBPJS.jumlahnonbpjs += 1

  def keterangan(self):
    return f'Nama\t\t: {self.nama} \nUsia\t\t: {self.usia} \nNIK\t\t: {self.nik} \nStatus\t\t: {self.status}'

a = dataBPJS('Irfan',18,12564,21506,'Bekerja')
b = dataBPJS('Nanda',19,13356,21507,'Bekerja')
c = dataBPJS('Samantha',29,14569,21566,'Bekerja')
d = dataBPJS('Saiful',20,15879,25556,'Tidak Bekerja')
e = dataBPJS('Ricky',45,16581,25564,'Bekerja')
f = dataBPJS('Farras',33,17545,26555,'Bekerja')
g = dataNonBPJS('Rakha',24,245627,'Bekerja')
h = dataNonBPJS('Friesella',21,28962,'Bekerja')
i = dataNonBPJS('Ayu',32,25264,'Bekerja')
j = dataNonBPJS('Joko',20,29622,'Tidak Bekerja')


print('='*50)
print(' '*15, 'Warga Anggota BPJS')
print(50*'=')
print(a.keterangan())
print(' ')
print(b.keterangan())
print(' ')
print(c.keterangan())
print(' ')
print(d.keterangan())
print(' ')
print(e.keterangan())
print(' ')
print(f.keterangan())
print('='*50)
print(' '*15, 'Warga Non BPJS')
print(50*'=')
print(g.keterangan())
print(' ')
print(h.keterangan())
print(' ')
print(i.keterangan())
print(' ')
print(j.keterangan())

#Show
print(' ')
print('='*53)
print(' ')
DATA = input("Apakah ingin menampilkan data statistik? (Yes/No)").lower()
print(' ')
if DATA == "yes" :
  print('='*53)
  print(' ')
  print("Jumlah Warga :",WargaDesaCijujung.jumlahwarga)
  print(' ')
  print("Jumlah Warga Anggota BPJS :", dataBPJS.jumlahBPJS)
  print(' ')
  print("Jumlah Warga Non BPJS :", dataNonBPJS.jumlahnonbpjs)

  x = ["Warga","BPJS","Non BPJS"]
  y = [WargaDesaCijujung.jumlahwarga, dataBPJS.jumlahBPJS, dataNonBPJS.jumlahnonbpjs]
  plt.title("Pendataan BPJS Warga Desa Cijujung")
  plt.bar(x,y)
  plt.show()

print(' ')
print('='*50)
print(' '*18, 'Thank You')
print(50*'=')
