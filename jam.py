import datetime
from datetime import datetime,time
import time

jamLokal = time.asctime(time.localtime(time.time()))
jam = time.localtime().tm_hour

jamLokal = time.asctime(time.localtime(time.time()))
jam = time.localtime().tm_hour

print("=" * 60 + "\n" + "=" * 24 + "-|" + "Tanggal dan Waktu" + "|-" + "=" * 22)
print("=" * 16 + "-|" + jamLokal + "|-" + "=" * 16)

if 0 <= jam <= 6:
    print("=" * 21 + "-<|Selamat subuh|>-" + "=" * 20)

elif 6 <= jam <= 12:
    print("=" * 21 + "-<|Selamat pagi|>-" + "=" * 21)

elif 12 <= jam <= 14:
    print("=" * 21 + "-<|Selamat siang|>-" + "=" * 20)

elif 14 <= jam <= 18:
    print("=" * 22 + "-|Selamat sore|-" + "=" * 22)

elif 18 <= jam <= 24:
    print("=" * 21 + "-<|Selamat malam|>-" + "=" * 20)
