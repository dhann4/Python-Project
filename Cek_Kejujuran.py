import datetime
from datetime import datetime,time
import time
while True:
    print(87*'=')
    print('''
  /$$$$$$  /$$     /$$ /$$$$$$           /$$$$$ /$$   /$$    /$$$$$ /$$   /$$ /$$$$$$$ 
 /$$__  $$|  $$   /$$//$$__  $$         |__  $$| $$  | $$   |__  $$| $$  | $$| $$__  $$
| $$  \ $$ \  $$ /$$/| $$  \ $$            | $$| $$  | $$      | $$| $$  | $$| $$  \ $$
| $$$$$$$$  \  $$$$/ | $$  | $$            | $$| $$  | $$      | $$| $$  | $$| $$$$$$$/
| $$__  $$   \  $$/  | $$  | $$       /$$  | $$| $$  | $$ /$$  | $$| $$  | $$| $$__  $$
| $$  | $$    | $$   | $$  | $$      | $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  \ $$
| $$  | $$    | $$   |  $$$$$$/      |  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
|__/  |__/    |__/    \______/        \______/  \______/  \______/  \______/ |__/  |__/
''')
    print(87*'=')
    jamLokal = time.asctime(time.localtime(time.time()))
    jam = time.localtime().tm_hour

    jamLokal = time.asctime(time.localtime(time.time()))
    jam = time.localtime().tm_hour

    print("=" * 29 + "-|" + jamLokal + "|-" + "=" * 30)
    if 0 <= jam <= 6:
        print("=" * 34 + "-<|Selamat Subuh|>-" + "=" * 34)

    elif 6 <= jam <= 12:
        print("=" * 35 + "-<|Selamat Pagi|>-" + "=" * 35)

    elif 12 <= jam <= 14:
        print("=" * 34 + "-<|Selamat Siang|>-" + "=" * 34)

    elif 14 <= jam <= 18:
        print("=" * 35 + "-|Selamat Sore|-" + "=" * 35)

    elif 18 <= jam <= 24:
        print("=" * 34 + "-<|Selamat Malam|>-" + "=" * 34)

    print(87*'=')
    nama = input("Masukkan Nama Ngab : ")
    if nama == "":
        print("Lu gk punya nama ?")
        continue

    print("\nJadi " + nama + ",\nApakah sudah siap dengan tes nya ?\n\n1. Iya ( Wajib Cek Umur Ngab )\n2. Bentar, siapin diri dulu\n3. Exit\n4. About")
    pilihan = int(input("\nMasukkan pilihan: "))

    if pilihan == 1:
        hitung_y = 0
        hitung_g = 0
        umur = int(input("\nMasukkan Umur Ngab : "))
        if umur < 14:
            print("\n!!! DASAR BOCIL !!!")
            continue
        elif umur < 17:
            print("\n!!! KHUSUS 18+ !!!")
            continue
        elif umur > 17 and umur < 80:
            print("\nLanjut Ngab")
        else:
            print("\n!!! UMUR NYA KAGAK NGOTAK WOE !!!")
            continue

        print("\nApakah anda pernah melakukan ini ?\n!!!BOHONG DOSA!!!\n")

        print("1. Pernah Nonton Bokep ?")
        jawaban1 = str(input("Jawab (y/g) : ")).lower()
        if jawaban1 == 'y':
            print("Bokep Terus !!!")
            hitung_y += 1
        elif jawaban1 == 'g':
            print("Hilih Kitil -_-")
            hitung_g += 1

        print("\n2. Pernah Ngintip Cewek Mandi ?")
        jawaban2 = str(input("Jawab (y/g) : ")).lower()
        if jawaban2 == 'y':
            print("Leh ugha lu ngab")
            hitung_y += 1
        elif jawaban2 == 'g':
            print("um..........")
            hitung_g += 1

        print("\n3. Pernah Coli ?")
        jawaban3 = str(input("Jawab (y/g) : ")).lower()
        if jawaban3 == 'y':
            print("Coli Terus !!!")
            hitung_y += 1
        elif jawaban3 == 'g':
            print("Mustahil lu kagak pernah coli ngab")
            hitung_g += 1

        print("\n4. Pernah Curi Duit Emak ?")
        jawaban4 = str(input("Jawab (y/g) : ")).lower()
        if jawaban4 == 'y':
            print("Astaga ngab kasian emak lu cari duit, malah lu ambil duit nya")
            hitung_y += 1
        elif jawaban4 == 'g':
            print("Lu pernah ambil duit emak lu buat ke rental PS kan ?")
            hitung_g += 1

        print("\n5. Pernah Skidipapap Ahoy Gehoy ?")
        jawaban5 = str(input("Jawab (y/g) : ")).lower()
        if jawaban5 == 'y':
            print("Kasian anak orang ngab, belum juga nikah udah skidipapap ahoy gehoy")
            hitung_y += 1
        elif jawaban5 == 'g':
            print("Setidaknya lu pernah lah 1x skidipapap ahoy gehoy sama anak orang")
            hitung_g += 1
        else:
            print("Mana jawaban nya woe ngab")

        if hitung_y != 0 and hitung_g != 0:
            print("\nTotal y =",hitung_y,"\nTotal G =",hitung_g)
            if hitung_y < hitung_g:
                print("\ntotal g =",hitung_g,",Selamat Ngab Masuk Surga")
            else:
                print("\ntotal y =",hitung_y,",!!! Siap-Siap Masuk Jahanam Ngab !!!")
            break
        elif hitung_y != 0:
            print("total y =",hitung_y,"\n!!! Siap-Siap Masuk Jahanam Ngab !!!")
            break
        print("total g =",hitung_g,"\nSelamat Ngab Masuk Surga")

        break

    elif pilihan == 2:
        print("Banyak Alasan Lu Ngab\n")

    elif pilihan == 3:
        print("Hadeuh\n")
        break
    elif pilihan == 4:
        
        print("=" * 31 + "-|" + jamLokal + "|-" + "=" * 31)
    if 0 <= jam <= 6:
        print("=" * 35 + "-<|Selamat Subuh|>-" + "=" * 36)

    elif 6 <= jam <= 12:
        print("=" * 36 + "-<|Selamat Pagi|>-" + "=" * 36)

    elif 12 <= jam <= 14:
        print("=" * 36 + "-<|Selamat Siang|>-" + "=" * 35)

    elif 14 <= jam <= 18:
        print("=" * 36 + "-|Selamat Sore|-" + "=" * 36)

    elif 18 <= jam <= 24:
        print("=" * 36 + "-<|Selamat Malam|>-" + "=" * 35)
        
        print('''
  /$$$$$$  /$$$$$$$   /$$$$$$        /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$         /$$$$ 
 /$$__  $$| $$__  $$ /$$__  $$      | $$$ | $$ /$$__  $$ /$$__  $$| $$__  $$       /$$  $$
| $$  \ $$| $$  \ $$| $$  \ $$      | $$$$| $$| $$  \__/| $$  \ $$| $$  \ $$      |__/\ $$
| $$$$$$$$| $$$$$$$/| $$$$$$$$      | $$ $$ $$| $$ /$$$$| $$$$$$$$| $$$$$$$           /$$/
| $$__  $$| $$____/ | $$__  $$      | $$  $$$$| $$|_  $$| $$__  $$| $$__  $$         /$$/ 
| $$  | $$| $$      | $$  | $$      | $$\  $$$| $$  \ $$| $$  | $$| $$  \ $$        |__/  
| $$  | $$| $$      | $$  | $$      | $$ \  $$|  $$$$$$/| $$  | $$| $$$$$$$/         /$$  
|__/  |__/|__/      |__/  |__/      |__/  \__/ \______/ |__/  |__/|_______/         |__/  
''')
        print(90*'=')
        print("Mending lu follow gw ngab")
        print("Facebook     : DHN")
        print("Instagram    : wr_dhanna")
        print(90*'=')
        break
    else:
        print("Pilihan tydack tersedia")
