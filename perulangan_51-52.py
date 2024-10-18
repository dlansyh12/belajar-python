# SOAL 5.1

# Input jumlah donat yang ingin dihitung
banyakDonat = int(input("Banyak donat yang ingin dihitung: \n"))

# Input harga per donat
hargaSatuan = int(input("Harga per donat: \n"))

# Cetak daftar harga donat
print("\nDaftar harga donat:")

# Menggunakan perulangan for untuk menampilkan harga setiap jumlah donat
for i in range(1, banyakDonat + 1):
    print(f"{i} donat: \t Rp {i * hargaSatuan},00")


# SOAL 5.2

# Input bilangan ke-N sebagai batas deret
N = int(input("Masukkan bilangan ke-N: \n"))

# Inisialisasi variabel untuk menyimpan jumlah bilangan
jumlah_total = 0

# Menggunakan perulangan for untuk menjumlahkan bilangan dari 1 hingga N
for i in range(1, N + 1):
    jumlah_total += i  # Menambah nilai i ke jumlah total

# Menghitung rerata (jumlah total dibagi N)
rerata = jumlah_total / N

# Menampilkan hasil jumlah total dan rerata
print(f"\nJumlah total bilangan dari 1 hingga {N}: {jumlah_total}")
print(f"Rerata dari bilangan 1 hingga {N}: {rerata}")
