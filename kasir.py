import datetime

def input_data(prompt, is_float=False):
    while True:
        try:
            # Jika is_float True, maka input harus berupa angka desimal
            value = float(input(prompt)) if is_float else input(prompt)
            if is_float and value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar." if is_float else "Input tidak valid.")

def format_rupiah(amount):
    return f"Rp {amount:,.2f}".replace(",", ".")  # Format dengan titik sebagai pemisah ribuan

def cetak_struk(nama_barang, harga_barang, jumlah_barang, total_harga, uang_pembeli, kembalian):
    # Dapatkan waktu transaksi saat ini
    waktu_transaksi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Cetak struk belanjaan
    print("\n" + "="*40)
    print(f"{'TOKO SERBA ADA':^40}")
    print(f"{'Jl. Mawar No. 123, Jakarta':^40}")
    print(f"{'Telp. 021-12345678':^40}")
    print("="*40)
    print(f" Waktu   : {waktu_transaksi}")
    print("="*40)
    print(f" Barang  : {nama_barang}")
    print(f" Harga   : {format_rupiah(harga_barang)}")
    print(f" Jumlah  : {jumlah_barang}")
    print(f" Total   : {format_rupiah(total_harga)}")
    print("="*40)
    print(f" Uang    : {format_rupiah(uang_pembeli)}")
    print(f" Kembalian: {format_rupiah(kembalian)}")
    print("="*40)
    print(f"{'TERIMA KASIH ATAS KUNJUNGAN ANDA':^40}")
    print(f"{'BARANG YANG SUDAH DIBELI TIDAK DAPAT':^40}")
    print(f"{'DITUKAR / DIKEMBALIKAN':^40}")
    print("="*40)

def kasir():
    print("Program Kasir Sederhana")
    
    # Memasukkan data barang
    nama_barang = input_data("Masukkan nama barang: ")
    harga_barang = input_data("Masukkan harga barang: Rp ", is_float=True)
    jumlah_barang = input_data("Masukkan jumlah barang: ", is_float=True)

    # Menghitung total harga
    total_harga = harga_barang * jumlah_barang
    print(f"Total harga {nama_barang}: {format_rupiah(total_harga)}")
    
    # Memasukkan uang pembeli
    while True:
        uang_pembeli = input_data("Masukkan jumlah uang pembeli: Rp ", is_float=True)
        
        if uang_pembeli >= total_harga:
            break
        else:
            print("Uang tidak cukup, coba lagi.")
    
    # Menghitung kembalian
    kembalian = uang_pembeli - total_harga
    
    # Cetak struk belanjaan
    cetak_struk(nama_barang, harga_barang, jumlah_barang, total_harga, uang_pembeli, kembalian)

# Menjalankan program
if __name__ == "__main__":
    kasir()
