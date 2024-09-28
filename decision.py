def jumlah_hari(bulan):
    # Daftar jumlah hari per bulan di tahun 2024
    hari_per_bulan = {
        1: ("Januari", 31),
        2: ("Februari", 29),  # 2024 adalah tahun kabisat
        3: ("Maret", 31),
        4: ("April", 30),
        5: ("Mei", 31),
        6: ("Juni", 30),
        7: ("Juli", 31),
        8: ("Agustus", 31),
        9: ("September", 30),
        10: ("Oktober", 31),
        11: ("November", 30),
        12: ("Desember", 31)
    }

    # Mapping nama bulan ke angka
    nama_ke_bulan = {v[0].lower(): k for k, v in hari_per_bulan.items()}

    # Jika input adalah angka
    if isinstance(bulan, int):
        if 1 <= bulan <= 12:
            nama_bulan, jumlah_hari = hari_per_bulan[bulan]
            return f"Bulan {nama_bulan} memiliki {jumlah_hari} hari."
        else:
            return "Bulan yang Anda masukkan tidak valid. Masukkan angka antara 1 dan 12."
    
    # Jika input adalah string
    elif isinstance(bulan, str):
        bulan = bulan.lower()
        if bulan in nama_ke_bulan:
            bulan_angka = nama_ke_bulan[bulan]
            nama_bulan, jumlah_hari = hari_per_bulan[bulan_angka]
            return f"Bulan ke-{bulan_angka} ({nama_bulan}) memiliki {jumlah_hari} hari."
        else:
            return "Nama bulan yang Anda masukkan tidak valid. Masukkan nama bulan yang benar."
    else:
        return "Input tidak valid."


try:
    # Meminta input dari user
    bulan = input("Masukkan bulan (angka 1-12 atau nama bulan): ")
    
    # Cek apakah input berupa angka
    if bulan.isdigit():
        bulan = int(bulan)
    else:
        bulan = bulan.capitalize()

    # Panggil fungsi untuk mendapatkan hasil
    hasil = jumlah_hari(bulan)
    print(hasil)

except ValueError:
    print("Input tidak valid. Masukkan angka atau nama bulan yang benar.")
