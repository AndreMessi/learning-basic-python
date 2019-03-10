class karyawan:
  '''Dasar kelas untuk semua karyawan'''
  jumlah_karyawan = 0

  def __init__(self, nama ,gaji):
    self.nama = nama
    self.gaji = gaji
    karyawan.jumlah_karyawan +=1

  def tampilkan_jumlah(self):
    print("total karyawan :", karyawan.jumlah_karyawan)
  
  def tampilkan_profile(self):
    print("nama :", self.nama)
    print("gaji :", self.gaji)

karyawan1 = karyawan("andre",1000000)
karyawan2 = karyawan("akbar",1000000)
karyawan3 = karyawan("nurmayana",1000000)
karyawan4 = karyawan("naya safitri",1000000)

karyawan1.tampilkan_profile()
karyawan2.tampilkan_profile()
karyawan3.tampilkan_profile()
karyawan4.tampilkan_profile()

print("total karyawan :", karyawan.jumlah_karyawan)
#menambahkan atribut builtin 
print("karyawan.__doc__ :",karyawan.__doc__)
print("karyawan.__name__ :",karyawan.__name__)
print("karyawan.__module__ :",karyawan.__module__)
print("karyawan.__dict__ :",karyawan.__dict__)
print("karyawan.__bases__ :",karyawan.__bases__)