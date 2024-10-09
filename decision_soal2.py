#program menghitung sisi

def input_sisi(prompt):
    # Fungsi untuk memastikan input adalah angka
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Input tidak valid. Masukkan bilangan positif.")

def cek_segitiga(sisi1, sisi2, sisi3):
    # Fungsi untuk mengecek jenis segitiga berdasarkan sisi
    if sisi1 == sisi2 == sisi3:
        return "3 sisi sama"
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        return "2 sisi sama"
    else:
        return "Tidak ada yang sama"

def main():
    print("Program untuk mengecek jenis segitiga berdasarkan panjang sisi.")
    
    # Meminta pengguna untuk memasukkan panjang sisi segitiga
    sisi1 = input_sisi("Masukkan sisi 1: ")
    sisi2 = input_sisi("Masukkan sisi 2: ")
    sisi3 = input_sisi("Masukkan sisi 3: ")
    
    # Memeriksa segitiga dan menampilkan hasil
    hasil = cek_segitiga(sisi1, sisi2, sisi3)
    print(hasil)

# Menjalankan program
if __name__ == "__main__":
    main()
