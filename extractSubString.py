#!C:\Python27\python

###############################################
# judul program: mengambil sub string
###############################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # deklarasi variabel string 
    s = "python"

    # karakter pertama dalam substring s
    print(s[0])
    # karakter ke dua dalam substring s
    print(s[1])
    # karakter ke-4 dihitung dari kanan
    print(s[-4])
    # 2 karakter pertama
    print(s[:2])
    # string s dikurangi 2 karakter pertama
    print(s[2:])
    # substring dari indeks ke 1 sampai dengan 3
    print(s[1:4])
    # substring dari indeks ke 2 sampai dengan 4
    print(s[2:5])

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()