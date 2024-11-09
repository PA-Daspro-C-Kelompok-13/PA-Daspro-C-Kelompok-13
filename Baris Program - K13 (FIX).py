import json
import time
from prettytable import PrettyTable
from pwinput import pwinput
import os
os.system ('cls')

'''==========================================='''
'''                 JSON PRODUK               '''
'''==========================================='''

def BacaData():
    with open('data_produk.json', 'r') as file:
        data_produk = json.load(file)
        
    return data_produk
    
def SimpanData(Data):
    with open('data_produk.json', 'w') as file:
        json.dump(Data, file, indent=4)

'''==========================================='''
'''                 JSON AKUN                 '''
'''==========================================='''

# Fungsi untuk membaca data user dari file JSON
def baca_data_user():
    try:
        with open("data_user.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"AkunUser": []}

# Fungsi untuk menulis data user ke file JSON
def tulis_data_user(data):
    with open("data_user.json", "w") as file:
        json.dump(data, file, indent=4)

'''=================================================================================================================================='''
'''                                                                   MULAI                                                          '''
'''=================================================================================================================================='''


def Mulai():
    while True:
        print("+===========================================================+")
        print("| SISTEM MIE GACOAN - KELOMPOK 13 (SISTEM INFROMASI C 2024) |")
        print("+===========================================================+")
        print("+===========================================================+")
        print("|                     Halo! Selamat Datang                  |")
        print("+===========================================================+")   
        print("|                          1. Admin                         |")
        print("|                          2. Customer                      |")
        print("|                          3. Keluar                        |")
        print("+===========================================================+")

        try:
            Role = input("Pilih Menu Login Anda (1/2/3): ")
            os.system('cls')
            if Role == '1':
                if AdminLogin():
                    AdminMenu()
                break
            elif Role == "2":
                if AwalUser():
                    UserMenu()
                break
            elif Role == "3":
                print("+=============================================================+")
                print("|                  ANDA KELUAR DARI PROGRAM                   |")
                print("+=============================================================+")
                print("|                Terimakasih & Sampai Jumpa !                 |")
                print("+=============================================================+")
                exit()
                
            else:
                print("+===========================================================+")
                print("|                  PILIHAN TIDAK TERSEDIA                   |")
                print("+===========================================================+")
                print("|               Masukkan Pilihan Anda Kembali               |")
                print("+===========================================================+")
                
        except (ValueError, KeyboardInterrupt):
            os.system('cls')
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            os.system('cls')


'''=================================================================================================================================='''
'''                                                          ADMIN LOGIN                                                             '''
'''=================================================================================================================================='''


# Data Akun
AkunAdmin = {
    'Zyrus': '040706',
    'Vira': '907415',
    'Ariel': '121145'
}

# Admin
def AdminLogin():
    os.system('cls')
    print("+==============================================================+")
    print("|                         HALAMAN ADMIN                        |")
    print("+==============================================================+")
    print("|    Halo Admin, Silahkan Masukkan Username & Password Anda    |")
    print("+==============================================================+")

    Kesempatan = 3
    while Kesempatan > 0:
        Username = input('Username: ')
        Password = pwinput('Password: ')
        os.system('cls')
        try:
            if Username in AkunAdmin and AkunAdmin[Username] == Password:
                print('+' + '-'* 34 + '+')
                print(f'       + Selamat Datang {Username} +')
                print('+' + '-'* 34 + '+')
                AdminMenu()
                return
            elif Username in AkunAdmin and AkunAdmin[Username] != Password or not Username in AkunAdmin:
                Kesempatan -= 1
                print("+====================================================================+")
                print("|                             LOGIN GAGAL                            |")
                print("+====================================================================+")
                print(f"|   Username/Password Yang Anda Masukkan Tidak Sesuai, Coba Lagi {Kesempatan}   |")
                print("+====================================================================+")
                
            if Kesempatan == 0:
                os.system('cls')
                print("+================================================================================+")
                print("|                               AKUN ANDA TERKUNCI                               |")
                print("+================================================================================+")
                print("|  Anda Terlalu Banyak Menggunakan Username/Password Yang Salah, Tunggu Kembali  |")
                print("+================================================================================+")
                for x in range (5, 0, -1):
                    time.sleep(1)
                    print(x)
                Kesempatan = 3
                os.system('cls')
                Mulai()
                return False

        except (ValueError, KeyboardInterrupt):
            os.system('cls')
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')


'''=================================================================================================================================='''
'''                                                           ADMIN MENU                                                             '''
'''=================================================================================================================================='''


# Menu Admin
def AdminMenu():
    while True:
        print('\n')
        print("+==================================+")
        print("|            MENU ADMIN            |")
        print("+==================================+")
        print("| 1. Tampilkan Produk              |")
        print("| 2. Tambah Produk                 |")
        print("| 3. Update Produk                 |")
        print("| 4. Hapus Produk                  |")
        print("| 5. Cari Produk                   |")
        print("| 6. Kembali                       |")
        print("+==================================+")
        
        try:
            Pilihan = int(input("Pilih Menu (1/2/3/4/5/6): "))
            os.system('cls')
            if Pilihan == 1:
                TampilProduk()
            elif Pilihan == 2:
                TambahProduk()
            elif Pilihan == 3:
                UpdateProduk()
            elif Pilihan == 4: 
                HapusProduk()
            elif Pilihan == 5:  
                CariProduk()
            elif Pilihan == 6:
                os.system('cls')
                Mulai()
                return
            else:
                print("+===========================================================+")
                print("|                  PILIHAN TIDAK TERSEDIA                   |")
                print("+===========================================================+")
                print("|               Masukkan Pilihan Anda Kembali               |")
                print("+===========================================================+")
        except (ValueError, KeyboardInterrupt):
            os.system('cls')
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')


'''=================================================================================================================================='''
'''                                              ADMIN (TAMPILKAN PRODUK)                                                            '''
'''=================================================================================================================================='''


def TampilProduk():
    Data = BacaData()
    os.system('cls')
    print('+==========================================+')
    print('+==========================================+')
    print('|  Daftar Menu ~~ MIE GACOAN SAMARINDA ~~  |')
    print('+==========================================+')
    print('+==========================================+')

    for kategori in Data["Kategori"]:
        nama_kategori = kategori["Nama Kategori"]
        print(f"\nKategori: {nama_kategori}")

        table = PrettyTable()
        table.field_names = ["ID", "Menu", "Harga"]
        table.title = f"Daftar Produk {nama_kategori}"

        for produk in kategori["Produk"]:
            table.add_row([produk["ID"], produk["Menu"], produk["Harga"]])

        print(table)
    
    input("\nTekan Enter, Untuk Melanjutkan.....")
    os.system('cls')


'''=================================================================================================================================='''
'''                                              ADMIN (TAMBAHKAN PRODUK)                                                            '''
'''=================================================================================================================================='''


def TambahProduk():
    Data = BacaData()

    while True:
        print('\n')
        print("+=====================================+")
        print("|          MENAMBAHKAN PRODUK         |")
        print("+=====================================+")
        print("|            PILIH KATEGORI           |")
        print("+=====================================+")
        print("| 1. Kategori Makanan                 |")
        print("| 2. Kategori Minuman                 |")
        print("| 3. Kembali                          |")
        print("+=====================================+")
        pilihan = input("Masukkan Pilihan Anda: ")
        os.system('cls')
        
        if pilihan == '1':
            kategori = "Makanan"
        elif pilihan == '2':
            kategori = "Minuman"
        elif pilihan == '3':
            return
        else:
            print("+===========================================================+")
            print("|                  KATEGORI TIDAK TERSEDIA                  |")
            print("+===========================================================+")
            print("|               Masukkan Pilihan Anda Kembali               |")
            print("+===========================================================+")
            continue

        kategori_ditemukan = None
        for found in Data["Kategori"]:
            if found["Nama Kategori"].lower() == kategori.lower():
                kategori_ditemukan = found
                break

        if not kategori_ditemukan:
            print("Kategori tidak ditemukan.")
            continue

        while True:
            try:
                Menu = input("Masukkan Menu Baru: ")
                HargaMenu = input(f"Masukkan Harga Untuk Menu {Menu}, (Minimal 2.000 | Maksimal 20.000): ")
                os.system('cls')

                # Program Prosedur
                if not (3 <= len(Menu) <= 50):
                    print("+=====================================================================+")
                    print("|                          MENU TIDAK SESUAI !                        |")
                    print("+=====================================================================+")
                    print("|                 Menu Yang Anda Masukkan Tidak Sesuai                |")
                    print("+=====================================================================+")
                    continue
                elif not (Menu.strip() and HargaMenu.isdigit()):
                    print("+=====================================================================+")
                    print("|                          MENU TIDAK SESUAI !                        |")
                    print("+=====================================================================+")
                    print("|                 Menu Yang Anda Masukkan Tidak Sesuai                |")
                    print("+=====================================================================+")
                    continue
                elif any(Produk["Menu"].lower() == Menu.lower() for Produk in kategori_ditemukan["Produk"]):
                    print("+=====================================================================+")
                    print("|                           MENU TIDAK SESUAI !                       |")
                    print("+=====================================================================+")
                    print("|                Menu Tersebut Sudah Tersedia, Coba Lagi              |")
                    print("+=====================================================================+")
                    continue

                # Konversi Harga Ke INT
                HargaMenu = int(HargaMenu)

                if not (2000 <= HargaMenu <= 20000):
                    print("+=====================================================================+")
                    print("|                         HARGA TIDAK SESUAI !                        |")
                    print("+=====================================================================+")
                    print("|                Harga Yang Anda Masukkan Tidak Sesuai                |")
                    print("+=====================================================================+")
                    continue

                # Untuk menyimpan produk baru
                MenuBaru = {
                    "ID": len(kategori_ditemukan["Produk"]) + 1,
                    "Menu": str(Menu),
                    "Harga": int(HargaMenu),
                }

                # Untuk menambahkan produk ke dalam data produk
                kategori_ditemukan["Produk"].append(MenuBaru)
                SimpanData(Data)
                print(f' +~~ Menu {Menu} Berhasil Di Tambahkan! ~~+ ')
                break

            except (ValueError, KeyboardInterrupt):
                os.system('cls')
                print('\n')
                print("+=====================================================================+")
                print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
                print("+=====================================================================+")
                print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
                print("+=====================================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
            except Exception as e:
                print(f'Error: {e}')
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')


'''=================================================================================================================================='''
'''                                                 ADMIN (UPDATE PRODUK)                                                            '''
'''=================================================================================================================================='''


def UpdateProduk():
    Data = BacaData()
    
    while True:
        print('\n')
        print("+=====================================+")
        print("|            UPDATE PRODUK            |")
        print("+=====================================+")
        print("|            PILIH KATEGORI           |")
        print("+=====================================+")
        print("| 1. Kategori Makanan                 |")
        print("| 2. Kategori Minuman                 |")
        print("| 3. Kembali                          |")
        print("+=====================================+")
        pilihan = input("Masukkan Pilihan Anda: ")
        os.system('cls')
        
        if pilihan == '1':
            nama_kategori = "Makanan"
        elif pilihan == '2':
            nama_kategori = "Minuman"
        elif pilihan == '3':
            return
        else:
            print("+===========================================================+")
            print("|                  KATEGORI TIDAK TERSEDIA                  |")
            print("+===========================================================+")
            print("|               Masukkan Pilihan Anda Kembali               |")
            print("+===========================================================+")
            continue
    
        kategori_ditemukan = False
        for kategori in Data["Kategori"]:
            if kategori["Nama Kategori"] == nama_kategori:
                kategori_ditemukan = True
                print(f"\nKategori: {nama_kategori}")

                table = PrettyTable()
                table.field_names = ["ID", "Menu", "Harga"]
                table.title = f"Daftar Produk {nama_kategori}"

                for produk in kategori["Produk"]:
                    table.add_row([produk["ID"], produk["Menu"], produk["Harga"]])

                print(table)

                while True: 
                    try:
                        id_produk = int(input("Masukkan ID Produk yang Ingin Diupdate: "))
                        menu_baru = input("Masukkan Nama Menu Baru: ").strip()
                        harga_baru = int(input(f"Masukkan Harga Menu {menu_baru}, (Minimal 2.000 | Maksimal 20.000): "))
                        os.system('cls')
                        
                        # Validasi semua input
                        produk_ditemukan = False
                        for produk in kategori["Produk"]:
                            if produk.get("ID") == id_produk:
                                produk_ditemukan = True
                                break

                        # Program Validasi
                        if not produk_ditemukan or not menu_baru or not (2000 <= harga_baru <= 20000):
                            print("+=====================================================================+")
                            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
                            print("+=====================================================================+")
                            print("|   Pastikan ID produk ada, menu tidak kosong, dan harga sesuai.      |")
                            print("+=====================================================================+")
                            continue

                        # Jika semua validasi lulus
                        for produk in kategori["Produk"]:
                            if produk.get("ID") == id_produk:
                                produk['Menu'] = menu_baru
                                produk['Harga'] = harga_baru
                                break

                        SimpanData(Data)
                        print(f' +~~ Menu {menu_baru} Dengan Harga {harga_baru} Berhasil Diupdate ~~+ ')
                        break
                        
                    except (ValueError, KeyboardInterrupt):
                        os.system('cls')
                        print('\n')
                        print("+=====================================================================+")
                        print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
                        print("+=====================================================================+")
                        print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
                        print("+=====================================================================+")
                        input("Tekan Enter Untuk Melanjutkan....")
                        os.system('cls')
                    except Exception as e:
                        print(f'Error: {e}')
                        input("Tekan Enter Untuk Melanjutkan....")
                        os.system('cls')


'''=================================================================================================================================='''
'''                                                  ADMIN (HAPUS PRODUK)                                                            '''
'''=================================================================================================================================='''


def HapusProduk():
    Data = BacaData()

    while True:
        try:
            print('\n')
            print("+=====================================+")
            print("|              HAPUS PRODUK           |")
            print("+=====================================+")
            print("| 1. Kategori Makanan                 |")
            print("| 2. Kategori Minuman                 |")
            print("| 3. Kembali                          |")
            print("+=====================================+")
            kategori = input("Masukkan Pilihan Anda: ")
            os.system('cls')

            # Mengatur nama kategori berdasarkan input
            if kategori == '1':
                nama_kategori = "Makanan"
            elif kategori == '2':
                nama_kategori = "Minuman"
            elif kategori == '3':
                Mulai()
            else:
                print("+===========================================================+")
                print("|                  KATEGORI TIDAK TERSEDIA                  |")
                print("+===========================================================+")
                print("|               Masukkan Pilihan Anda Kembali               |")
                print("+===========================================================+")
                continue
            
            id_hapus = int(input("Masukkan ID Produk yang Ingin Dihapus: "))

            # Mencari kategori yang cocok
            for kat in Data["Kategori"]:
                if kat["Nama Kategori"] == nama_kategori:
                    produk_list = kat["Produk"]
                    
                    # Mencari produk berdasarkan ID
                    for item in produk_list:
                        if item["ID"] == id_hapus:
                            produk_list.remove(item)
                            
                            # Memperbarui ID produk agar tetap berurutan tanpa menggunakan enumerate
                            new_id = 1
                            for produk in produk_list:
                                produk["ID"] = new_id
                                new_id += 1
                            
                            SimpanData(Data)
                            print(f"Menu dengan ID {id_hapus} berhasil dihapus dari kategori {nama_kategori}.")
                            return

                    print(f"Menu dengan ID {id_hapus} tidak ditemukan dalam kategori {nama_kategori}.")
                    return
            
            # Pesan jika nama kategori tidak ditemukan
            print(f"Kategori {nama_kategori} tidak ditemukan.")
        
        except (ValueError, KeyboardInterrupt):
            os.system('cls')
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
            


'''=================================================================================================================================='''
'''                                                   ADMIN (CARI PRODUK)                                                            '''
'''=================================================================================================================================='''


def CariProduk():
    data = BacaData()
    cari_produk = input("Masukkan Nama Produk yang akan dicari: ")
    hasil_pencarian = []
    
    for kategori in data["Kategori"]:
        for Produk in kategori["Produk"]:
            if cari_produk.lower() in Produk["Menu"].lower():
                hasil_pencarian.append(Produk)
                
    if hasil_pencarian:
        print("Hasil Pencarian:")
        for kategori in data["Kategori"]:
            print(f"\nKategori: {kategori['Nama Kategori']}")
                
            table = PrettyTable()
            table.field_names = ["ID", "Menu", "Harga"]
            table.title = "MIE GACOAN SAMARINDA"
                
            for Produk in kategori["Produk"]:
                if Produk in hasil_pencarian:
                    table.add_row([Produk["ID"], Produk["Menu"], Produk["Harga"]])
                    
            print(table)

            input("\nTekan Enter, Untuk Melanjutkan.....")
            os.system('cls')
    else:
        print("\n----Produk tidak ditemukan----.")

        input("\nTekan Enter, Untuk Melanjutkan.....")
        os.system('cls')
        
    return hasil_pencarian



'''=================================================================================================================================='''
'''                                                                USER                                                              '''
'''=================================================================================================================================='''


def AwalUser():
    os.system('cls')

    while True:
        try:
            print('\n')
            print('+===========================================================+')
            print('|    ~~~ HALO SELAMAT DATANG DI MIE GACOAN SAMARINDA ~~~    |')
            print('|                    JAGONYA MIE INDONESIA                  |')
            print('+===========================================================+')
            pilihan = input("\nApakah Anda Sudah Memiliki Akun? (Ya/Tidak): ").strip().lower()
            os.system('cls')

            if pilihan =='ya':
                if UserMenu():
                    break
            elif pilihan == 'tidak':
                if UserRegistrasi():
                    break
            else:
                print("+=======================================================================+")
                print("|                        PILIHAN TIDAK SESUAI !                         |")
                print("|                Pilihan Yang Anda Masukkan Tidak Sesuai !              |")
                print("+=======================================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
        except (ValueError, KeyboardInterrupt):
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')


'''=================================================================================================================================='''
'''                                                      USER REGISTRASI                                                             '''
'''=================================================================================================================================='''


# Registrasi User
def UserRegistrasi():
    os.system('cls')
    data_user = baca_data_user()

    while True:
        try:
            print('\n')
            print("+==========================================================================+")
            print("|                       ~~~   SELAMAT DATANG   ~~~                         |")
            print("|   Halo !!!, Silahkan Buat Akun Anda Untuk Dapat Menikmati Layanan Kami   |")
            print("+==========================================================================+")
            username = input("Masukkan Username(Minimal 3 Karakter dan Maksimal 10 Karakter): ")
            password = pwinput("Masukkan Password(Minimal 3 Karakter dan Maksimal 8 Karakter): ")
            os.system('cls')
            
            # Program Validasi Username & Password (Sesuai Ketentuan Yang Dibuat)
            if not username:
                print("+=====================================================================+")
                print("|                 DATA YANG ANDA MASUKKAN TIDAK VALID                 |")
                print("+=====================================================================+")
                print("|        Pastikan Username/Password Yang Anda Masukkan Sesuai         |")
                print("+=====================================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
                continue
            if len(username) < 3 or len(username) > 10:
                print("+=====================================================================+")
                print("|                 DATA YANG ANDA MASUKKAN TIDAK VALID                 |")
                print("+=====================================================================+")
                print("|        Pastikan Username/Password Yang Anda Masukkan Sesuai         |")
                print("+=====================================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
                continue
            if not password:
                print("+=====================================================================+")
                print("|                 DATA YANG ANDA MASUKKAN TIDAK VALID                 |")
                print("+=====================================================================+")
                print("|        Pastikan Username/Password Yang Anda Masukkan Sesuai         |")
                print("+=====================================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
                continue
            if len(password) < 3 or len(password) > 8:
                print("+=====================================================================+")
                print("|                 DATA YANG ANDA MASUKKAN TIDAK VALID                 |")
                print("+=====================================================================+")
                print("|        Pastikan Username/Password Yang Anda Masukkan Sesuai         |")
                print("+=====================================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
                continue
            
            # Memeriksa apakah username sudah ada
            for user in data_user["AkunUser"]:
                if user["username"] == username:
                    print("+=========================================================================================+")
                    print("|                 Username Tersebut Sudah Terdaftar, Gunakan Username Lain                |")
                    print("+=========================================================================================+")
                    input("Tekan Enter Untuk Melanjutkan....")
                    os.system('cls')
                    return False

            # Menambahkan user baru ke data JSON
            user_baru = {
                "username": username,
                "password": password,
                "saldo": 0
            }
            data_user["AkunUser"].append(user_baru)
            tulis_data_user(data_user)
            print(" << AKUN ANDA BERHASIL DIBUAT >>")
            print(f"Username Anda: {username}")
            print(f"Password Anda: {password}")
            print('\n')
            input("Tekan Enter Untuk Melanjutkan....")
            UserMenu()
            return
        except (ValueError, KeyboardInterrupt):
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')


'''=================================================================================================================================='''
'''                                                            USER MENU                                                             '''
'''=================================================================================================================================='''

# Menu User
def UserMenu():
    os.system('cls')
    while True:
        
        print('+===========================================================+')
        print('|                 ~~~ MIE GACOAN SAMARINDA ~~~              |')
        print('|                    JAGONYA MIE INDONESIA                  |')
        print('+===========================================================+')
        print("+===================================+")
        print("|             MENU USER             |")
        print("+===================================+")
        print("| 1. Melihat Produk                 |")
        print("| 2. Memesan Menu                   |")
        print("| 3. Cari Menu                      |")
        print("| 4. E-Money                        |")
        print("| 5. Keluar                         |")
        print("+===================================+")
        
        try:
            Pilihan = int(input("Pilih Menu (1/2/3/4/5): "))
            os.system('cls')
            if Pilihan == 1:
                MelihatProduk()
            elif Pilihan == 2:
                MemesanMenu()
            elif Pilihan == 3:
                CariMenu()
            elif Pilihan == 4:  
                TampilanEmoney()
            elif Pilihan == 5:
                Mulai()
            else:
                print("+===========================================================+")
                print("|                  PILIHAN TIDAK TERSEDIA                   |")
                print("+===========================================================+")
                print("|               Masukkan Pilihan Anda Kembali               |")
                print("+===========================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
        except (ValueError, KeyboardInterrupt):
            os.system('cls')
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')

'''=================================================================================================================================='''
'''                                                  USER (Lihat Produk)                                                             '''
'''=================================================================================================================================='''

def MelihatProduk():
    Data = BacaData()
    os.system('cls')
    print('+==========================================+')
    print('+==========================================+')
    print('|  Daftar Menu ~~ MIE GACOAN SAMARINDA ~~  |')
    print('+==========================================+')
    print('+==========================================+')

    for kategori in Data["Kategori"]:
        nama_kategori = kategori["Nama Kategori"]
        print(f"\nKategori: {nama_kategori}")

        table = PrettyTable()
        table.field_names = ["ID", "Menu", "Harga"]
        table.title = f"Daftar Produk {nama_kategori}"

        for produk in kategori["Produk"]:
            table.add_row([produk["ID"], produk["Menu"], produk["Harga"]])

        print(table)
    
    input("\nTekan Enter, Untuk Melanjutkan.....")
    os.system('cls')

'''=================================================================================================================================='''
'''                                                      USER (PEMESANAN)                                                             '''
'''=================================================================================================================================='''

def MemesanMenu():
    os.system('cls')
    Data = BacaData()
    data_user = baca_data_user()
    pesanan = []
    total_harga = 0

# Menu Pemesanan
    while True:
        print('\n')
        print('+==========================+')
        print('|        PEMESANAN         |')
        print('+==========================+')
        print("| 1. Pesan Makanan         |")    
        print("| 2. Pesan Minuman         |") 
        print("| 3. Lihat Pesanan         |")
        print("| 4. Bayar Pesanan         |")
        print("| 5. Kembali               |")
        print('+==========================+')

        try:
            pilihan = input("Pilih Menu (1/2/3/4/5): ")
            os.system('cls')

            if pilihan == '1':
                kategori = "Makanan"
            elif pilihan == '2':
                kategori = "Minuman"
            elif pilihan == '3':
                
                # Tampilkan pesanan
                if pesanan == []:
                    print('\n')
                    print("+=============================================================+")
                    print("| ANDA BELUM MEMESAN APAPUN, SILAHKAN MEMESAN TERLEBIH DAHULU |")
                    print("+=============================================================+")
                    input("Tekan Enter Untuk Melanjutkan....")
                    os.system('cls')
                else:
                    print("+==============+")
                    print("| PESANAN ANDA |")
                    print("+==============+")
                    table = PrettyTable()
                    table.field_names = ["Menu", "Jumlah", "Harga Satuan", "Total"]
                    for p in pesanan:
                        table.add_row([p['menu'], p['jumlah'], p['harga'], p['total']])
                    print(table)
                    print(f"Total Yang Harus Dibayar: Rp {total_harga}")
                    input("\nTekan Enter, Untuk Melanjutkan.....")
                    os.system('cls')
                continue

            elif pilihan == '4':
                
                # Proses pembayaran
                if pesanan == []:
                    print('\n')
                    print("+=============================================================+")
                    print("| ANDA BELUM MEMESAN APAPUN, SILAHKAN MEMESAN TERLEBIH DAHULU |")
                    print("+=============================================================+")
                    input("Tekan Enter Untuk Melanjutkan....")
                    os.system('cls')
                    continue
                
                print("+=============+")
                print("| PEEMBAYARAN |")
                print("+=============+")
                print(f"Total Pembayaran: Rp {total_harga}")
                username = input("Masukkan Username E-Money Anda: ")
                password = pwinput("Masukkan Password E-Money Anda: ")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')


                # Cek Saldo Apakah Cukup/Tidak dan username
                temukanuser = False
                for user in data_user["AkunUser"]:
                    if user["username"] == username and user["password"] == password:
                        temukanuser = True
                        if user["saldo"] >= total_harga:
                            user["saldo"] -= total_harga
                            tulis_data_user(data_user)
                            print('\n=== PEMBAYARAN BERHASIL! ===')

                            # Menampilkan Struk Pemesanan
                            tabelStruk = PrettyTable()
                            tabelStruk.title = "STRUK PESANAN ANDA ~~ MIE GACOAN SAMARINDA ~~"
                            tabelStruk.field_names = ["Menu", "Jumlah", "Harga Satuan", "Total"]
                            for p in pesanan:
                                tabelStruk.add_row([p['menu'], p['jumlah'], p['harga'], p['total']])
                            print(tabelStruk)
                            print(f'Total Harga Yang Anda Bayar: Rp {total_harga}')
                            print(f'Sisa Saldo Anda: Rp {user["saldo"]}')
                            input("\nTekan Enter, Untuk Melanjutkan.....")
                            os.system('cls')
                            Mulai()
                        else:
                            print('+======================================================================+')
                            print('| PEMBAYARAN GAGAL, PASTIKAN AKUN ANDA BENAR/PASTIKAN SALDO ANDA CUKUP |')
                            print('+======================================================================+')
                            print(f"Total Pesanan: Rp {total_harga}")
                            print(f"Saldo Anda: Rp {user['saldo']}")
                            input("\nTekan Enter, Untuk Melanjutkan.....")
                            MemesanMenu()
                if not temukanuser:
                    print("+=======================================================+")
                    print("| Username atau Password Anda Salah. Silahkan Coba Lagi |")
                    print("+=======================================================+")
                    os.system('cls')
                    return

            elif pilihan == '5':
                return

            else:
                print("+=====================================================================+")
                print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
                print("+=====================================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
                continue

            # Menampilkan Menu Sesuai Pilihan Kategori
            print(f"\nMenu {kategori}:")
            for kat in Data["Kategori"]:
                if kat["Nama Kategori"] == kategori:
                    table = PrettyTable()
                    table.field_names = ["ID", "Menu", "Harga"]
                    for produk in kat["Produk"]:
                        table.add_row([produk["ID"], produk["Menu"], produk["Harga"]])
                    print(table)

                    # Proses pemesanan
                    try:
                        id_menu = int(input("Masukkan ID Menu Yang Ingin Dipesan // Tekan 0 Untuk Membatalkan: "))
                        if id_menu == 0:
                            continue

                        # Mencari Menu Berdasaran ID Yang Sudah Di input
                        menu_ditemukan = False
                        for produk in kat["Produk"]:
                            if produk["ID"] == id_menu:
                                menu_ditemukan = True
                                jumlah = int(input("Masukkan Jumlah Pesanan: "))
                                os.system('cls')
                                if jumlah <= 0:
                                    print('\n')
                                    print("+=====================================================================+")
                                    print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
                                    print("+=====================================================================+")
                                    input("Tekan Enter Untuk Melanjutkan....")
                                    os.system('cls')
                                    continue

                                # Menambahkan Pesanan
                                total = produk["Harga"] * jumlah
                                pesanan_baru = {
                                    'menu': produk["Menu"],
                                    'jumlah': jumlah,
                                    'harga': produk["Harga"],
                                    'total': total
                                }
                                pesanan.append(pesanan_baru)
                                total_harga += total
                                print(f"\n=== Berhasil Menambahkan {jumlah} {produk['Menu']} ===")
                                input("\nTekan Enter Untuk Melanjutkan....")
                                os.system('cls')
                                break

                        if not menu_ditemukan:
                            print('\n')
                            print('+======================+')
                            print("| Menu Tidak Ditemukan |")
                            print('+======================+')
                            input("Tekan Enter Untuk Melanjutkan....")
                            os.system('cls')

                    except (ValueError, KeyboardInterrupt):
                        os.system('cls')
                        print('\n')
                        print("+=====================================================================+")
                        print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
                        print("+=====================================================================+")
                        print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
                        print("+=====================================================================+")
                        input("Tekan Enter Untuk Melanjutkan....")
                        os.system('cls')
                    except Exception as e:
                        print(f'Error: {e}')
                        input("Tekan Enter Untuk Melanjutkan....")
                        os.system('cls')

        except (ValueError, KeyboardInterrupt):
            os.system('cls')
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')


'''=================================================================================================================================='''
'''                                                     USER (CARI MENU)                                                             '''
'''=================================================================================================================================='''


def CariMenu():
    data = BacaData()
    cari_produk = input("Masukkan Nama Produk yang akan dicari: ")
    os.system('cls')
    hasil_pencarian = []
    
    for kategori in data["Kategori"]:
        for Produk in kategori["Produk"]:
            if cari_produk.lower() in Produk["Menu"].lower():
                hasil_pencarian.append(Produk)
                
    if hasil_pencarian:
        print(f"=== Anda Mencari Menu {cari_produk} ===")
        for kategori in data["Kategori"]:
            print(f"\nKategori: {kategori['Nama Kategori']}")
                
            table = PrettyTable()
            table.field_names = ["ID", "Menu", "Harga"]
            table.title = "MIE GACOAN SAMARINDA"
                
            for Produk in kategori["Produk"]:
                if Produk in hasil_pencarian:
                    table.add_row([Produk["ID"], Produk["Menu"], Produk["Harga"]])
                    
            print(table)
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
            
    else:
        print('+=============================================+')
        print('| Produk Menu Yang Anda Cari, Tidak Ditemukan |')
        print('+=============================================+')
        input("\nTekan Enter, Untuk Melanjutkan.....")
        os.system('cls')
        
    return hasil_pencarian


'''=================================================================================================================================='''
'''                                                               E-MONEY                                                            '''
'''=================================================================================================================================='''
def TampilanEmoney():
    os.system('cls')
    while True:
        print('+==============================================+')
        print('|                 $$$ E-Money $$$              |')
        print('+==============================================+')
        print('\n')
        print("+=================================+")
        print("|        $$ MENU E-Money $$       |")
        print("+=================================+")
        print("| 1. Mengecek Saldo               |")
        print("| 2. Menambah Saldo               |")
        print("| 3. Keluar                       |")
        print("+=================================+")
        
        try:
            Pilihan = int(input("Pilih Menu (1/2/3): "))
            os.system('cls')
            if Pilihan == 1:
                eMoney()
            elif Pilihan == 2:
                nambahEmoney()
            elif Pilihan == 3: 
                UserMenu()
            else:
                print("+===========================================================+")
                print("|                  PILIHAN TIDAK TERSEDIA                   |")
                print("+===========================================================+")
                print("|               Masukkan Pilihan Anda Kembali               |")
                print("+===========================================================+")
                input("Tekan Enter Untuk Melanjutkan....")
                os.system('cls')
        except (ValueError, KeyboardInterrupt):
            print('\n')
            print("+=====================================================================+")
            print("|                DATA YANG ANDA MASUKKAN TIDAK VALID                  |")
            print("+=====================================================================+")
            print("|                Pastikan Anda Tidak Menekan CTRL + C                 |")
            print("+=====================================================================+")
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
        except Exception as e:
            print(f'Error: {e}')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')

''' ================== '''
'''      CEK SALDO     '''
''' ================== '''

def eMoney():
    os.system('cls')
    data_user = baca_data_user()

    while True:
        username = input("Username: ")
        password = pwinput("Password: ")
        os.system('cls')

        for user in data_user["AkunUser"]:
            if user["username"] == username:
                if user["password"] == password:
                    print(f'\nHalo {username}')
                    print(f"\nSaldo anda saat ini adalah: Rp {user['saldo']}")
                    input("Tekan Enter Untuk Melanjutkan....")
                    os.system('cls')
                    return
                else:
                    print("+=====================================================+")
                    print("| Login Gagal, Pastikan Username/Password Anda Sesuai |")
                    print("+=====================================================+")
                    input("Tekan Enter Untuk Melanjutkan....")
                    os.system('cls')
                    break

        if not data_user or "AkunUser" not in data_user:
            print('+============================================================================+')
            print("| Login Gagal, Akun Anda Tidak Ditemukan. Silahkan Buat Akun Terlebih Dahulu |")
            print('+============================================================================+')
            input("Tekan Enter Untuk Melanjutkan....")
            os.system('cls')
            return
        
# Tambah Saldo
def nambahEmoney():
    os.system('cls')
    data_user = baca_data_user()

    while True:
        username = input("Username: ")
        password = pwinput("Password: ")

        jumlah = int(input("Masukkan Jumlah Saldo(Minimal 20.000 | Maksimal 500.000): "))
        if jumlah < 20000:
            print("+======================================================+")
            print("|                GAGAL MENAMBAHKAN SALDO               |")
            print("| Pastikan Saldo Yang Ingin Ditambahkan Minimal 20.000 |")
            print("+======================================================+")
            return
        elif jumlah > 500000:
            print("+=======================================================+")
            print("|                 GAGAL MENAMBAHKAN SALDO               |")
            print("| Pastikan Saldo Yang Ingin Ditambahkan Maximal 500.000 |")
            print("+=======================================================+")
            return
        
        for user in data_user["AkunUser"]:
            if user["username"] == username:
                if user["password"] == password:
                    user['saldo'] += jumlah
                    print(f'=== Saldo Berhasil Ditambahkan. Saldo Anda Sekarang: {user['saldo']} ===')
                    tulis_data_user(data_user)
                    return
    
        print("+=======================================================================+")
        print("| Pengguna Tidak Ditemukan, Pastikan Username atau Password Anda Sesuai |")
        print("|    Jika Belum Memiliki Akun, Silahkan Membuat Akun Terlebih Dahulu    |")
        print("+=======================================================================+")
        input("Tekan Enter Untuk Melanjutkan....")
        os.system('cls')
        return
Mulai()