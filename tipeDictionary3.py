#!C:\Python27\python

######################################################################################
# judul program: menambahkan indeks dan value ke dalam dictionary yang bersangkutan
######################################################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # deklarasi dictionary
    data = {'satu':10, 'dua':20, 'tiga':30}

    # tampilan elemen dictionary sebelum ditambah
    print("elemen dictionary sebelum ditambah: ")
    print(data)

    # menambah elemn baru ke dalam dictionary data
    data['empat'] = 40
    data['lima'] = 50

    # tampilan elemen dictionary sesudah ditambah
    print("\nelemen dictionary sesudah ditambah: ")
    print(data)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()
