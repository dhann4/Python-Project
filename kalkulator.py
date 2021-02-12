import datetime
from datetime import datetime,time
import time



def tambah(a,b):
    tambah = a + b
    return tambah

def kurang(a,b):
    kurang = a - b
    return kurang

def kali(a,b):
    kali = a * b
    return kali

def bagi(a,b):
    bagi = a / b
    return bagi

while True:
    jamLokal = time.asctime(time.localtime(time.time()))
    jam = time.localtime().tm_hour

    jamLokal = time.asctime(time.localtime(time.time()))
    jam = time.localtime().tm_hour

    print("=" * 60 + "\n" + "=" * 24 + "-|" + "Kalkulator" + "|-" + "=" * 22)
    print("=" * 16 + "-|" + jamLokal + "|-" + "=" * 16)
    if 0 <= jam <= 6:
        print("=" * 21 + "-<|Selamat Subuh|>-" + "=" * 20)

    elif 6 <= jam <= 12:
        print("=" * 21 + "-<|Selamat Pagi|>-" + "=" * 21)

    elif 12 <= jam <= 14:
        print("=" * 21 + "-<|Selamat Siang|>-" + "=" * 20)

    elif 14 <= jam <= 18:
        print("=" * 22 + "-|Selamat Sore|-" + "=" * 22)

    elif 18 <= jam <= 24:
        print("=" * 21 + "-<|Selamat Malam|>-" + "=" * 20)
    print(60 * "=")
    print('\n\t============= KALKULATOR SEDERHANA =============')
    a = int(float(input('Masukan Bilangan Pertama : ')))
    b = int(float(input('Masukan Bilangan Kedua   : ')))
    print("\n1. Penjumlahan (+)\n2. Pengurangan (-)\n3. Perkalian (*)\n4. Pembagian (/)\n5. Batal (X)")
    c = input('\nPilih 1 sampai 5 : ')
    if c == '1':
        print('Penjumlahan: ',a,'+',b,'= ',tambah(a,b))
    elif c == '2':
        print('Pengurangan: ',a,'-',b,'= ',kurang(a,b))
    elif c == '3':
        print('Perkalian: ',a,'*',b,'= ',kali(a,b))
    elif c == '4':
        print('Pembagian: ',a,'//',b, '= ', bagi(a,b))
    elif c == '5':
        print('See You Next Time ^_^')
        break
    else:
        print('ANGKA NYA KAGAK NGOTAK WOE!!!')
