# SOAL 5.2 bilanggan terbesar dan terkecil

# Inisialisasi variabel untuk menyimpan bilangan terbesar dan terkecil
bilangan_terbesar = None
bilangan_terkecil = None

print("Masukkan bilangan (atau ketik 'stop' untuk mengakhiri):")

# Perulangan untuk terus meminta input dari pengguna
while True:
    input_pengguna = input("Masukkan bilangan: ")

    # Memeriksa jika input adalah "stop" untuk mengakhiri perulangan
    if input_pengguna.lower() == "stop":
        break

    try:
        # Mengubah input menjadi bilangan bulat (integer)
        bilangan = int(input_pengguna)
        
        # Mengecek apakah bilangan_terbesar atau bilangan_terkecil belum diinisialisasi
        if bilangan_terbesar is None or bilangan > bilangan_terbesar:
            bilangan_terbesar = bilangan
        if bilangan_terkecil is None or bilangan < bilangan_terkecil:
            bilangan_terkecil = bilangan

    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat atau ketik 'stop'.")

# Menampilkan hasil bilangan terbesar dan terkecil jika ada input yang valid
if bilangan_terbesar is not None and bilangan_terkecil is not None:
    print(f"\nBilangan terbesar yang dimasukkan: {bilangan_terbesar}")
    print(f"Bilangan terkecil yang dimasukkan: {bilangan_terkecil}")
else:
    print("\nTidak ada bilangan yang dimasukkan.")
