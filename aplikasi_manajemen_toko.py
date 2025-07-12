import csv
import os

FILE_NAME = "produk.csv"

# Fungsi untuk membaca data dari file CSV
def load_data():
    data = []
    if not os.path.exists(FILE_NAME):
        return data
    with open(FILE_NAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['harga'] = int(row['harga'])
            row['stok'] = int(row['stok'])
            data.append(row)
    return data

# Fungsi untuk menyimpan data ke file CSV
def save_data(data):
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['id', 'nama', 'harga', 'stok']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Menampilkan semua data produk
def tampilkan_produk(data):
    if not data:
        print("Tidak ada data produk.")
    else:
        print("=== Daftar Produk ===")
        for d in data:
            print(f"ID: {d['id']}, Nama: {d['nama']}, Harga: {d['harga']}, Stok: {d['stok']}")

# Menambah produk baru
def tambah_produk(data):
    id_produk = input("Masukkan ID Produk: ")
    nama = input("Masukkan Nama Produk: ")
    harga = int(input("Masukkan Harga Produk: "))
    stok = int(input("Masukkan Stok Produk: "))
    data.append({'id': id_produk, 'nama': nama, 'harga': harga, 'stok': stok})
    save_data(data)
    print("Produk berhasil ditambahkan.")

# Mengupdate produk
def update_produk(data):
    id_update = input("Masukkan ID Produk yang ingin diupdate: ")
    for d in data:
        if d['id'] == id_update:
            d['nama'] = input("Masukkan Nama Baru: ")
            d['harga'] = int(input("Masukkan Harga Baru: "))
            d['stok'] = int(input("Masukkan Stok Baru: "))
            save_data(data)
            print("Produk berhasil diupdate.")
            return
    print("Produk tidak ditemukan.")

# Menghapus produk
def hapus_produk(data):
    id_hapus = input("Masukkan ID Produk yang ingin dihapus: ")
    for d in data:
        if d['id'] == id_hapus:
            data.remove(d)
            save_data(data)
            print("Produk berhasil dihapus.")
            return
    print("Produk tidak ditemukan.")

# Menu utama
def main():
    data_produk = load_data()
    while True:
        print("\n=== Menu Toko ===")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_produk(data_produk)
        elif pilihan == "2":
            tambah_produk(data_produk)
        elif pilihan == "3":
            update_produk(data_produk)
        elif pilihan == "4":
            hapus_produk(data_produk)
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
