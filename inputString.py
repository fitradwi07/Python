#!C:\Python27\python

#############################################
# judul program: input data string
#############################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat prompt untuk tipe data string
    nama = raw_input("masukan nama anda : ")
    # membuat prompt untuk tipe data karakter
    karakter = raw_input("masukan sebuah karakter : ")

    # menampilkan nilai variabel ke layar
    print("hallo ", nama, ", apa kabar?")
    print("karakter yang dimasukan : '", karakter, "'")
    
    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()