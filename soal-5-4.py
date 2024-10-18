# MENGHITUNG PERKALIAN DUA BILANGAN TANPA OPERATOR

def perkalian(a, b):
    hasil = 0
    for _ in range(abs(b)):  # Melakukan penjumlahan sebanyak nilai b
        hasil += a
    if b < 0:
        hasil = -hasil  # Mengatasi bilangan negatif
    return hasil

# Input dua bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

# Menampilkan hasil perkalian
print(f"Hasil perkalian {a} dan {b} adalah: {perkalian(a, b)}")


# MENGHITUNG PEMANGKATAN DUA BILANGAN TANPA OPERATOR

def pemangkatan(basis, eksponen):
    hasil = 1
    for _ in range(eksponen):  # Melakukan perkalian berulang
        hasil *= basis
    return hasil

# Input dua bilangan
basis = int(input("Masukkan basis: "))
eksponen = int(input("Masukkan eksponen: "))

# Menampilkan hasil pemangkatan
print(f"Hasil dari {basis} pangkat {eksponen} adalah: {pemangkatan(basis, eksponen)}")


# MENGHITUNG PEMANGKATAN DUA BILANGAN TANPA OPERATOR