#!C:\Python27\python

#######################################################
# judul program: menghapus elemen dari dictionary
#######################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # deklarasi dictionary
    data = {'satu': 10, 'dua':20, 'tiga':30}

    # tampilan elemen dictionary sebelum dihapus
    print("elemen dictionary sebelum dihapus: ")
    print(data)

    # mengahapus nilai elemen dari data['satu'] dan data['tiga']
    del data['satu']
    del data['tiga']

    # tampilan elemen dictionary sesudah dihapus
    print("\nelemen dictionary sesudah dihapus: ")
    print(data)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()