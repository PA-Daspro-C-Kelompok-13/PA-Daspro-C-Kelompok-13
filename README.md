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

============================= **ADMIN** =============================

![1](https://github.com/user-attachments/assets/b337341f-3015-4bb8-a16b-2b789b22522c)

Disaat programnya dimulai menu pertama akan menampilkan seperti ini

![2](https://github.com/user-attachments/assets/8d2e0d53-4f2b-4c76-a5aa-75bc30648691)

Jika Memilih Nomor 1 maka akan langsung di arahkan ke bagian admin. dan untuk di awal harus memasukan akun admin.

![3](https://github.com/user-attachments/assets/31fb6433-5688-4576-a383-01904dd5f223)

Jika berhasil maka langsung di arahkan ke menu admin yang di mana menu admin ini memakai sistem CRUD dan Searching. lalu memilih pilihan yang sudah di sediakan di fitur admin

![4](https://github.com/user-attachments/assets/0c548bfc-6028-47b4-99dc-47b2cbdaf59f)

Jika memilih pilihan nomor 1 maka akan langsung menampilkan Tabel Menu yang terdapat menu makanan dan minuman di tabel yang terpisah. dan setelah itu akan langsung otomatis di alihkan ke menu Admin ulang.

![5](https://github.com/user-attachments/assets/e93efe14-acdf-478f-ad18-eb28c26cd206)

Dan jika memilih pilihan nomor 2 akan langsung menampilkan bagian tambah produk, disini kita bisa menambah menu atau produk dengan menentukan dulu mau menambah di produk di kategori Makanan atau Minuman

![6](https://github.com/user-attachments/assets/e994b140-9c4d-45ea-9853-ca7083f23043)

Jika memilih di bagian kategori makanan akan langsung di minta untuk memasukan menu makanan baru lalu memberikan harganya dengan catatan menu makanan ini kamu beri pemberitahuan untuk harga minimal 2.000 dan maksimal 20.000.

![7](https://github.com/user-attachments/assets/5322c7f2-b9b1-47e6-8801-42a1e0180e45)

setelah menambahkan menu dan harganya akan mengeluarkan invoice atau pemberitahuan kalau menu tersebut telah berhasil di tambahkan

![8](https://github.com/user-attachments/assets/fe96022c-fd95-4228-ba7b-dc90c16c2a08)

Dan di bagian Menu Admin jika memilih nomor 3 akan langsung ke bagian menu Update Produk. di update produk ini kita harus memntukan mau update produk di kategori apa, makanan atau minuman.

![9](https://github.com/user-attachments/assets/eadc8765-8cfc-4738-9e2d-422509784c7b)

Jika di bagian menu produk memilih untuk menu update produk minuman. pertama akan langsung menampilkan tabel kategori minuman,lalu akan langsung di arahkan untuk meng-input ID yang ingin diupdate produknya. setelah itu akan langsung diminta untuk memsukan nama produk dan harga baru.

![10](https://github.com/user-attachments/assets/e82d1263-a1de-4292-8ec2-391ba70fa341)

setelah update nama beserta harga produk. maka akan muncul pemberitahuan kalau produk tersebut berhasil di update.

![11](https://github.com/user-attachments/assets/4671e6bb-665a-44cf-b88a-4336dd4cc8da)

Dan Jika Di Menu Admin memilih nomor 4 akan langsung muncul di bagian menu untuk Menghapus Produk. dan di menu ini akan diminta juga untuk memilih ingin menghapus produk di kategori apa, makanan atau minuman.

![12](https://github.com/user-attachments/assets/53287e2e-cd75-499a-ae50-551d9edfe6bc)

dan setelah memasukan pilihan makanan atau minuman maka akan langsung diminta untuk input ID produk yang ingin di hapus.

![13](https://github.com/user-attachments/assets/2abc1c5e-40a4-4061-b0f2-cec827e8a710)

setelah memasukan ID produk yang ingin dihapus. akan muncul pemberitahuan seperti di atas bahwa produk dengan ID tersebut berhasil di hapus

![14](https://github.com/user-attachments/assets/854885dd-ba83-4e6a-a776-70dbd7b07fc0)

Lalu jika memilih Nomor 5 di menu Admin maka akan diminta untuk input mau mencari produk apa. dan langsung memunculkan produk dari kategori makanan ataupun minuman yang bersangkutan dengan input yang dimasukan.

![15](https://github.com/user-attachments/assets/abf025c3-0701-444c-8aae-f11e4a765a49)

Dan jika memilih nomor 6 (Kembali), itu akan langsung di alihkan ke bagian milih Role di awal

============================= **USER** =============================

![1 (1)](https://github.com/user-attachments/assets/215c30a2-bdca-4193-9333-9c40817cb63c)

Jika di awal memilih role User. selanjutnya akan di tanya untuk di user sudah memiliki akun atau tidak. jika ya maka akan langsung ke menu user. jika tidak akan di alihkan untuk membuat akun terlebih dahulu

![Jika -Tidak- (Membuat Akun)](https://github.com/user-attachments/assets/38cce4b3-fbf0-4b48-bda3-1e5298735531)

Jika memilih tidak saat di tanya sudah memiliki akun atau belum. selanjutnya akan di minta untuk membuat akun dan password
dengan beberapa larangan tidak boleh spasi,simbol dan ada minimal kata.


![Berhasil Membuat Akun](https://github.com/user-attachments/assets/284743b8-086f-40b6-95f5-725de331f659)

Jika Suda membuat akun maka akan muncul pemberitahuan akun telah berhasil dibuat

![Jika -Ya- (Ke User Menu) (1)](https://github.com/user-attachments/assets/3d6beb43-f103-4cd5-87df-b56e50c23133)

Jika sudah membuat akun maka langsung di alihkan ke Menu User. di menu user ada beberapa pilihan fitur di Menu User ini

![5 (1)](https://github.com/user-attachments/assets/e934a19f-a845-4557-9bd3-0b2f014482a9)

Jika Memilih Nomor 1 pada Menu user maka akan menampilkan Tabel Produk dari kedua Kategori, Makanan dan Minuman. Selanjutnya akan otomatis kembali ke Menu User

![7 (1)](https://github.com/user-attachments/assets/6699a691-a022-482f-894a-545b6905ddd4)

Jika Memilih untuk Pesan Maka diminta untuk memasukan ID produk yang ingin di pesan dan jumlah produk yang ingin di pesan

![8 (1)](https://github.com/user-attachments/assets/5babf717-b5b2-4543-a33a-339b6e2b0800)

Jika Sudah input ID Produk yang ingin di pesan maka akan ada pemberitahuan bahwa produk tersebut berhasil dipesan.

![9 (1)](https://github.com/user-attachments/assets/9edd3aa6-286d-49bf-8234-72419990c378)

Dan di pemesanan menu ini bisa melihat apa aja yang sudah kita pesan.

![10 (1)](https://github.com/user-attachments/assets/0113ad78-f3ad-4e00-bae6-a7c8dd6bc693)

Selain melihat pesanan kita juga bisa langsug membayar pesanan tersebut dengan syarat harus memasukan Username dan Password kita di Menu User

![11 (1)](https://github.com/user-attachments/assets/ed2c397d-1907-4f68-99bc-bc8118ad2de9)

Jika Username dan Password untuk membayar pesanan akan muncul pemberitahuan Pembayaran berhasil dan di berikan nota struk dan juga ada di beritahu sisa saldo kita berapa.

![Cari #1](https://github.com/user-attachments/assets/ce75b0ee-6b93-49f1-9832-b31500822a5a)

Jika memilih nomor 3 pada user menu maka akan langsung diminta untuk input produk apa yang ingin di cari.

![Cari #2](https://github.com/user-attachments/assets/839b6018-1fc2-4466-bb6c-9e17b963464d)

setelah input produk yang ingin di cari maka akan menampilkan tabel produk yang sesuai atau bersangkutan dengan input yang di masukan

![12 (1)](https://github.com/user-attachments/assets/0c2822a6-66ba-4524-ace9-5290405cd469)

Jika memilih Nomor 4 pada user menu makan akan menampilkan table E-Money. dimana itu ada beberapa fitur yaitu. mengecek dan menambah saldo dan juga keluar

![13 (1)](https://github.com/user-attachments/assets/465a590c-a561-439e-902d-b5fe839afaa6)

![14 (1)](https://github.com/user-attachments/assets/aaa8820c-b9c6-4a2d-afa6-d5f5bf4c3837)

Jika memilih untuk mengecek saldo maka akan langsung di minta memasukan Username dan Password. lalu akan ada pemberitahuan kalau saldo anda berapa.

![16](https://github.com/user-attachments/assets/7ec5bfa4-95ac-4156-a330-8daaff1675bd)

Jika memilih untuk menambah saldo maka sama kayak ngecek saldo. akan langsung diminta untuk memasukan username dan password.Jika sudah memasukan username dan password maka akan langsung diminta untuk memasukan nominal saldo yang ingin di tambah. dengan catatan minimal 20.000 - 500.000

![17](https://github.com/user-attachments/assets/982e64a6-abf9-434d-b4ee-72ab78cc9805)

Setelah memasukan nominal. maka akan muncul pemberitahuan bahwa berhasil menambahkan saldo










































