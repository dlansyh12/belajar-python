# Fungsi untuk mengonversi nilai huruf ke bobot angka
def konversi_nilai(nilai_huruf):
    if nilai_huruf == 'A':
        return 4.0
    elif nilai_huruf == 'B':
        return 3.0
    elif nilai_huruf == 'C':
        return 2.0
    elif nilai_huruf == 'D':
        return 1.0
    else:
        return 0.0  # Untuk nilai di luar A, B, C, D (misalnya E, tidak lulus)

# Meminta input jumlah mata kuliah dari pengguna
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

total_bobot = 0  # Variabel untuk menyimpan total bobot nilai
total_sks = 0    # Variabel untuk menyimpan total SKS

# Perulangan untuk input nilai setiap mata kuliah
for i in range(1, jumlah_mata_kuliah + 1):
    print(f"\nMata kuliah ke-{i}:")
    
    # Meminta input nilai dan jumlah SKS untuk mata kuliah
    nilai = input("Masukkan nilai (A/B/C/D): ").upper()  # Pastikan huruf kapital
    sks = int(input("Masukkan jumlah SKS: "))
    
    # Konversi nilai huruf ke bobot angka
    bobot_nilai = konversi_nilai(nilai)
    
    # Menghitung bobot total untuk mata kuliah tersebut
    total_bobot += bobot_nilai * sks
    total_sks += sks

# Menghitung Indeks Prestasi Semester (IPS)
if total_sks > 0:
    ips = total_bobot / total_sks
    print(f"\nTotal SKS: {total_sks}")
    print(f"Indeks Prestasi Semester (IPS): {ips:.2f}")
else:
    print("\nTidak ada mata kuliah yang dimasukkan.")
