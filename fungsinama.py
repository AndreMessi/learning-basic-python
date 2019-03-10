def print_info(nama,usia=20):
    """Fungsi ini menampilkan info yang dimasukkan"""
    print("nama",nama)
    print("usia",usia)

print_info(usia=25,nama="andre")

# Pemanggilan fungsi tidak menyediakan argumen usia 
print_info( nama = "andre" ) 


total = 0

def sum(arg1,arg2):
    """Menambahkan variabel dan mengembalikan hasilnya."""
    total=arg1+arg2
    print("di dalam fungsi nilai total",total)
    return total

sum(10,20)
print("di luar fungsi nilai total",total)