#!C:\Python27\python

##########################################################
# judul program: menambahkan nilai elemen didalamn list
##########################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat list array
    buah = ["durian", "mangga", "apel"]
    # menampilakn isi array
    print("elemen awal: ")
    print(buah)

    # menggunakan metode append()
    buah.append("jeruk")
    # menampilkan isi array dibagian belakang 
    print("\nsetelah menggunakan append(): ")
    print(buah)

    # menggunakan metode insert()
    buah.insert(1, "kiwi")
    # menampilakan isi array diindeks ke-1
    print("\nsetelah menggunakan insert(): ")
    print(buah)

    # menggunakan metode extend()
    buah.extend(["melon", "anggur"])
    # menggabungkan isi array di bagian belakang
    print("\nsetelah menggukan extend(): ")
    print(buah)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()