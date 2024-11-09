# PA-Daspro-C-Kelompok-13

+---------= **Sistem Manajemen Mie Gacoan** =-----------+

|  Zyrus Alfredo Randan Malinggato  ( 2409116120 )  

|  Mohamad Ariel Saputra D Loi      ( 2409116087 )  

|  Elvira Agustin                   ( 2409116109 )  

+-----------------------------------------------------------+

# Deskripsi

Program kami adalah sebuah sistem manajemen Mie Gacoan. yang dimana program kami terdapat 2 Role, Admin dan Customer terus di bagian menu
kami membagi menu menjadi 2 kategori yaitu Makanan dan Minuman. Di Role Admin kami memakai sistem CRUD dan Searching, 1.Tampilkan Produk, 2.Tambah Produk, 3.Update Produk, 4.Hapus Produk, 5.Cari Produk dan, 6. kembali. Dibagian Role User kami menyediakan beberapa fitur yaitu: 1.Melihat Produk, 2.Memesan Menu, 3.Cari Produk, 4. E Money dan, 5.Keluar.


# Library

Di program kami memakai beberapa Library yaitu:

1. import json ( untuk membuat penyimpanan sementara )
2. import time ( untuk membuat sistem waktu )
3. from prettytable import PrettyTable ( untuk membuat tabel dengan rapi )
4. from pwinput import pwinput ( untuk menyembunyikan password dengan simbol *)
5. import os ( untuk membersihkan output terminal sebelum kode os )

# Program Fitur

### Admin
1. Tampilkan Produk
2. Tambah Produk
3. Update Produk
4. Hapus Produk
5. Cari Produk
6. kembali

### User
1. Melihat Produk
2. Memesan Menu
3. Cari Produk
4. E Money 
5. Keluar

# PENJELASAN PROGRAM

========= **USER** =========

![1](https://github.com/user-attachments/assets/b337341f-3015-4bb8-a16b-2b789b22522c)

Disaat programnya dimulai menu pertama akan menampilkan seperti ini

![2](https://github.com/user-attachments/assets/8d2e0d53-4f2b-4c76-a5aa-75bc30648691)

Jika Memilih Nomor 1 maka akan langsung di arahkan ke bagian admin. dan untuk di awal harus memasukan akun admin.

![3](https://github.com/user-attachments/assets/31fb6433-5688-4576-a383-01904dd5f223)

Jika berhasil maka langsung di arahkan ke menu admin yang di mana menu admin ini memakai sistem CRUD dan Searching. lalu memilih

pilihan yang sudah di sediakan di fitur admin

![4](https://github.com/user-attachments/assets/0c548bfc-6028-47b4-99dc-47b2cbdaf59f)

Jika memilih pilihan nomor 1 maka akan langsung menampilkan Tabel Menu yang terdapat menu makanan dan minuman di tabel yang terpisah.

dan setelah itu akan langsung otomatis di alihkan ke menu Admin ulang.

![5](https://github.com/user-attachments/assets/e93efe14-acdf-478f-ad18-eb28c26cd206)

Dan jika memilih pilihan nomor 2 akan langsung menampilkan bagian tambah produk, disini kita bisa menambah menu atau produk dengan

menentukan dulu mau menambah di produk di kategori Makanan atau Minuman

![6](https://github.com/user-attachments/assets/e994b140-9c4d-45ea-9853-ca7083f23043)

Jika memilih di bagian kategori makanan akan langsung di minta untuk memasukan menu makanan baru lalu memberikan harganya dengan catatan

menu makanan ini kamu beri pemberitahuan untuk harga minimal 2.000 dan maksimal 20.000.

![7](https://github.com/user-attachments/assets/5322c7f2-b9b1-47e6-8801-42a1e0180e45)

setelah menambahkan menu dan harganya akan mengeluarkan invoice atau pemberitahuan kalau menu tersebut telah berhasil di tambahkan

![8](https://github.com/user-attachments/assets/fe96022c-fd95-4228-ba7b-dc90c16c2a08)

Dan di bagian Menu Admin jika memilih nomor 3 akan langsung ke bagian menu Update Produk. di update produk ini kita harus memntukan

mau update produk di kategori apa, makanan atau minuman.

![9](https://github.com/user-attachments/assets/eadc8765-8cfc-4738-9e2d-422509784c7b)

Jika di bagian menu produk memilih untuk menu update produk minuman. pertama akan langsung menampilkan tabel kategori minuman,

lalu akan langsung di arahkan untuk meng-input ID yang ingin diupdate produknya. setelah itu akan langsung diminta untuk memsukan nama

produk dan harga baru.

![10](https://github.com/user-attachments/assets/e82d1263-a1de-4292-8ec2-391ba70fa341)

setelah update nama beserta harga produk. maka akan muncul pemberitahuan kalau produk tersebut berhasil di update.
















