class Transaksi:
    def __init__(self):
        """
        fungsi sebagai instansi baru dengan dictionary kosong untuk menyimpan transaksi
        """
        self.inventory_dict = {}  # dictionary kosong untuk menyimpan transaksi#

    def add_item(self):
        """
           Menambahkan item baru ke dalam inventory.

           Input:
           - nama_item: string, nama item yang akan ditambahkan
           - jumlah_item: int, jumlah item yang akan ditambahkan
           - harga: float, harga item yang akan ditambahkan

           Output:
           - Tidak ada output. Inventory akan diperbarui jika item berhasil ditambahkan.

           Raises:
           - TypeError: jika input tidak sesuai dengan tipe data yang diharapkan.

           """
        while True:
            try:
                # Mendapatkan input dari user
                nama_item = input("Masukkan nama item (jika sudah ketik n/no): ")
                if nama_item.lower() == 'no' or nama_item.lower() == 'n':
                    break
                jumlah_item = int(input("Masukkan jumlah item: "))
                harga = float(input("Masukkan harga item: "))
                # Validasi input
                if not isinstance(nama_item, str) or nama_item.isdigit():
                    raise TypeError("Nama item harus string!")
                if not isinstance(jumlah_item, int) or jumlah_item <= 0:
                    raise TypeError("Jumlah item harus lebih dari 0 dan berupa angka!")
                if not isinstance(harga, float) and not isinstance(harga, int) or str(harga).isalpha():
                    raise TypeError("Harga berupa angka!")

                # Menambahkan item pada inventory_dict
                if nama_item in self.inventory_dict:
                    self.inventory_dict[nama_item]['Jumlah Item'] += jumlah_item
                    self.inventory_dict[nama_item]['Harga'] = harga
                else:
                    self.inventory_dict[nama_item] = {'Jumlah Item': jumlah_item, 'Harga': harga}

                print("Item telah ditambahkan ke dalam daftar")  # Memberikan pesan konfirmasi
            except (TypeError, ValueError) as e:
                # Menangani exception jika input tidak sesuai
                print(f"Terjadi kesalahan: {e}")

    def display_all_items(self):
        """
        fungsi untuk menampilkan daftar belanjaan

        Output:
        - Display item pada inventory_dict

        """
        print("Daftar item:")
        print("{:<15} {:<10} {:<10}".format("Nama Item", "Jumlah Item", "Harga"))
        for nama_item, data_item in self.inventory_dict.items():
            print("{:<15} {:<10} {:<10}".format(nama_item, data_item['Jumlah Item'], data_item['Harga']))

    def update_item(self):
        """
            Fungsi ini digunakan untuk memperbarui data item di dalam inventory.

            User akan diminta untuk memilih item yang ingin diperbarui, lalu user dapat memilih
            untuk mengubah jumlah item, harga atau menghapus item tersebut.

            Raises:
                ValueError: Jika input jumlah item atau harga yang dimasukkan kurang dari atau sama dengan 0.

            """
        # Menampilkan seluruh item yang ada di dalam inventory
        self.display_all_items()
        while True:
            # User diminta untuk memilih item yang ingin diperbarui
            nama_item = input("Masukkan nama item yang ingin diubah: ")
            if nama_item not in self.inventory_dict:
                print(f"Item '{nama_item}' tidak ditemukan di dalam daftar.")
                konfirmasi = input("Apakah ingin mencoba lagi? (y/n): ")
                if konfirmasi.lower() == 'n':
                    return
            else:
                break
        # Menampilkan data item yang dipilih user
        print("{:<15} {:<10} {:<10}".format("Nama Item", "Jumlah Item", "Harga"))
        print("{:<15} {:<10} {:<10}".format(nama_item, self.inventory_dict[nama_item]['Jumlah Item'],
                                            self.inventory_dict[nama_item]['Harga']))
        # Menampilkan pilihan aksi yang bisa dilakukan user
        print("Pilih aksi yang ingin dilakukan:")
        print("1. Update nama item")
        print("2. Update jumlah item")
        print("3. Update harga")
        print("4. Delete item")
        print("5. Kembali ke menu")

        try:
            # User diminta untuk memilih aksi yang ingin dilakukan
            action = int(input("Masukkan angka untuk mengedit: "))
            if action == 1:
                # User memilih untuk mengubah nama item
                nama_baru = input(f"Masukkan nama baru: ")
                self.inventory_dict[nama_baru] = self.inventory_dict.pop(nama_item)
                self.inventory_dict[nama_baru]['Nama Item'] = nama_baru
                print(f"Item {nama_item} telah diubah menjadi {nama_baru}")
            elif action == 2:
                # User memilih untuk mengubah jumlah item
                jumlah_baru = int(input(f"Masukkan jumlah item yang baru {nama_item}: "))
                if jumlah_baru <= 0:
                    raise ValueError("Jumlah item harus lebih besar dari 0")
                self.inventory_dict[nama_item]['Jumlah Item'] = jumlah_baru
                print(f"Jumlah item {nama_item} telah diperbarui")
            elif action == 3:
                # User memilih untuk mengubah harga item
                harga_baru = float(input(f"Masukkan harga baru untuk {nama_item}: "))
                if harga_baru <= 0:
                    raise ValueError("Harga harus lebih besar dari 0")
                self.inventory_dict[nama_item]['Harga'] = harga_baru
                print(f"Harga {nama_item} telah diperbarui")
            elif action == 4:
                # User memilih untuk menghapus item pada daftar belanja
                print(f"Item '{nama_item}' akan dihapus dari daftar:")
                print("{:<15} {:<10} {:<10}".format("Nama Item", "Jumlah Item", "Harga"))
                print("{:<15} {:<10} {:<10}".format(nama_item, self.inventory_dict[nama_item]['Jumlah Item'],
                                                    self.inventory_dict[nama_item]['Harga']))
                konfirmasi = input("Apakah Anda yakin ingin menghapus item tersebut? (y/n): ")
                if konfirmasi.lower() == 'y':
                    del self.inventory_dict[nama_item]
                    print(f"Item {nama_item} telah dihapus dari daftar")
                else:
                    print(f"Hapus item {nama_item} dibatalkan")
            elif action == 5:
                # User memilih untuk kembali ke menu awal
                print("Kembali ke menu")
            else:
                raise ValueError("Pilihan tidak valid")
        except ValueError as e:
            print(f"Terjadi kesalahan: {e}")

    def reset_item(self):
        konfirmasi = input("Apakah Anda yakin ingin menghapus seluruh belanjaan?(y/n): ")
        if konfirmasi.lower() == 'y':
            self.inventory_dict.clear()
            print("Seluruh item telah dihapus dari daftar")
        else:
            print("Tidak ada item yang dihapus")

    def cetak_transaksi(self):
        """
        fungsi untuk menampilkan total biaya dari transaksi

        input: none.

        output: daftar belanjaan serta dengan total biayanya
        """
        total_biaya = 0
        print("{:<15} {:<10} {:<10} {:<10}".format("Nama Item", "Jumlah Item", "Harga", "Total"))
        for nama_item, data_belanja in self.inventory_dict.items():
            jumlah_item = data_belanja['Jumlah Item']
            harga = data_belanja['Harga']
            total_belanja = jumlah_item * harga  # Menghitung total belanja dengan mengalikan jumlah dan harga item
            total_biaya += total_belanja
            print("{:<15} {:<10} {:<10} {:<10}".format(nama_item, jumlah_item, harga, total_belanja))

        # Memberikan diskon sesuai dengan harga total belanjaan
        diskon = 0
        if total_biaya > 500000:
            diskon = 0.1
        elif total_biaya > 300000:
            diskon = 0.08
        elif total_biaya > 200000:
            diskon = 0.05

        if diskon > 0:
            potongan_harga = total_biaya * diskon
            total_biaya -= potongan_harga
            print(f"Diskon {diskon * 100:.0f}%: Rp -{potongan_harga:.2f}")

        print(f"Total biaya: Rp {total_biaya:.2f}")

        # Menambahkan kondisi untuk konfirmasi sebelum mencetak transaksi
        while True:
            answer = input("Apakah data transaksi sudah benar? (Y/N) ")
            if answer.lower() == 'y':
                # Jika user memilih Y (yes), maka program akan berhenti dengan kode exit 0
                raise SystemExit(0)
            elif answer.lower() == 'n':
                # Jika user memilih N (no), maka program akan kembali ke menu awal dengan break
                break
            else:
                print("Pilihan tidak valid. Silakan pilih (Y/N).")

        # Kembali ke menu awal
        self.run()

    def run(self):
        """
        Metode ini menampilkan menu utama program dan memproses masukan pengguna. Pengguna diminta untuk memilih
        salah satu opsi dari menu, dan program akan memanggil metode yang sesuai berdasarkan pilihan pengguna.

        Menu:
        1. Tambah item
        2. Update item
        3. Hapus semua item
        4. Lihat daftar transaksi
        5. Keluar

        Jika pengguna memilih opsi 1, metode `add_item` akan dipanggil.
        Jika pengguna memilih opsi 2, metode `update_item` akan dipanggil.
        Jika pengguna memilih opsi 3, metode `reset_item` akan dipanggil.
        Jika pengguna memilih opsi 4, metode `cetak_transaksi` akan dipanggil.
        Jika pengguna memilih opsi 5, program akan dihentikan.

        Jika pengguna memasukkan pilihan yang tidak valid, akan muncul pesan kesalahan dan pengguna akan diminta untuk
        memasukkan pilihan yang benar.

        Parameter:
        - Tidak ada parameter.

        """
        while True:
            print("\n========== MENU ==========")
            print("1. Tambah item")
            print("2. Update item")
            print("3. Hapus semua item")
            print("4. Lihat daftar transaksi")
            print("5. Keluar")

            try:
                pilih_menu = int(input("Masukkan pilihan menu: "))
                if pilih_menu == 1:
                    self.add_item()
                elif pilih_menu == 2:
                    self.update_item()
                elif pilih_menu == 3:
                    self.reset_item()
                elif pilih_menu == 4:
                    self.cetak_transaksi()
                elif pilih_menu == 5:
                    print("Terima kasih telah berbelanja di toko kamui")
                    raise SystemExit()
                else:
                    raise ValueError("Pilihan menu tidak valid")
            except ValueError as e:
                print(f"Terjadi kesalahan: {e}")
