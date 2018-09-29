#!C:\Python27\python

###############################################################
# judul program: mengubah elemen didalam dictionary
###############################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # deklarasi dectionary
    data = {'satu': 10, 'dua': 20, 'tiga': 30}

    # tampilan elemen sebelum diubah
    print("elmen dictionary sebelum diubah: ")
    print(data)

    # mengubah nilai elemen data['satu'] dan data['dua']
    data['satu'] = 60
    data['dua'] = 90

    # tampilan elemen sesudah diubah
    print("\nelemen dictionary sesudah diubah: ")
    print(data)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()