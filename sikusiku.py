# Minta pengguna memasukan jumlah baris 
jumlah_baris = int(input("Masukkan jumlah baris: "))

# Loop pertama untuk mengontrol baris
for baris in range(1, jumlah_baris + 1):
    for bintang in range(1,baris + 1):
        print("*", end=" ")
    print()