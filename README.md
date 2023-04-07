# Self Services Cashier
![Cashier](https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80)

##### Gambar 1.0 ilustrasi kasir

## Latar Belakang Masalah
Andi merupakan seorang pemilik supermarket besar di salah satu kota di indonesia, ia ingin membuat kasir dengan konsep self-service jadi para customer dapat memasukkan item, jumlah, dan harga barang yang dibeli. Hal ini dilakukan demi memangkas dana operasional, dengan adanya kasir self-service maka Andi dapat menghemat dana yang harusnya digunakan untuk petugas kasir.
## Feature Requirements
Fitur yang diminta adalah sebagai berikut:
1. Customer dapat menambahkan item sendiri
2. Customer dapat melakukan update pada item
3. Customer dapat menghapus dan mereset barang belanja
4. Customer dapat melihat daftar transaksi
5. Customer mendapatkan diskon 5%, 8%, 10% dengan S&K berlaku

## Flowchart
![Flowchart](/images/flowchart.jpg)
## Functions dan Attributes
Berikut adalah penjelasan mengenai function atau attribute yang digunakan:
### Function
1.__init__(self)
Metode ini adalah konstruktor yang menginisialisasi instance baru dengan kamus kosong untuk menyimpan transaksi.

2. add_item(self)
Metode ini menambahkan item baru ke inventaris dengan meminta masukan dari pengguna. Ia menerima tiga masukan, yaitu nama item, jumlah item, dan harga item. Jika masukan valid, item akan ditambahkan ke kamus inventaris. Jika masukan tidak valid, TypeError akan diangkat.

3. display_all_items(self)
Metode ini menampilkan semua item dalam kamus inventaris dengan cara yang diformat.

4. update_item(self)
Metode ini memungkinkan pengguna untuk memperbarui item yang ada dalam inventaris. Pertama, ia menampilkan semua item dalam inventaris. Kemudian, pengguna diminta untuk memilih item yang ingin diperbarui. Setelah memilih item, pengguna dapat memilih untuk memperbarui nama item, jumlah, harga, atau menghapus item. Jika masukan tidak valid, ValueError akan diangkat.

5. reset_items(self)
Metode ini memungkinkan pengguna untuk menghapus langsung seluruh daftar belanjaan tanpa perlu menghapus satu-persatu.

6. cetak_transaksi(self)
Metode ini memungkinkan pengguna untuk dapat melihat barang belanjaan.

7 run(self)
Metode ini memungkinkan pengguna untuk memilih menu pada menu yang telah diperlihatkan. Serta digunakan untuk mengimpor module

### Atribut:
Atribut inventory_dict adalah kamus yang menyimpan semua transaksi. Setiap transaksi terdiri dari pasangan kunci-nilai, di mana kunci adalah nama item, dan nilai adalah kamus yang berisi jumlah dan harga item.

## Cara Penggunaan Code
1. Download main.py serta transaksi.py
2. Masukkan ke dua file dalam satu folder
3. Jalankan main.py

## Test Code
### 1. Test Pertama
a. Pengguna memilih menu dan mencoba menambahkan item
![test-1](/images/test-1.png)
b. Pengguna menambahkan nama, jumlah, dan harga item
![test-1.2](/images/test-1.2.png)
### 2. Test Kedua
a. Pengguna ingin mengupdate item dengan memilih menu kedua
![test-2](/images/test-2.png)
b. Pengguna mengupdate sesuai nomor action yang diinginkan
![test-2.2](/images/test-2.2.png)
### 3. Test Ketiga
a. Pengguna ingin menghapus item karena kesalahan input maka dilakukan reset
![test-3](/images/test-3.1.png)
### 4. Test Keempat
a. Pengguna ingin mengecek daftar transaksi serta melakukan checkout
![test-4](/images/test-4.png)

## Conclusion
  Pada permasalahan self-service ini terdapat banyak hal yang perlu diantisipasi sebab program ini masih terbatas sehingga akan terjadi banyak sekali permasalahan yang akan didapat dari penggunaannya. Sebuah sistem self-service sendiri memiliki kelebihan dan kekurangan, jika dilihat dari kelebihannya dapat diketahui bahwa hal ini dapat mengurangi biaya operasional namun pada sisi kekurangan dapat mengakibatkan kerugian yang besar jika program yang digunakan terjadi permasalahan seperti bug yang fatal atau vulnerability yang sampai sekarang masih terjadi meskipun di perusahaan besar. Oleh karena itu diharapkan program ini dapat terus dikembangkan sampai benar-benar menjadi program self-service yang dapat membantu para pebisnis untuk dapat menekan biaya operasional.
