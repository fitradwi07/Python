#!C:\Python27\python

############################################################
# judul program: menambahkan elemen ke dalam dictionary
############################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # dekalrasi dictionary
    data = {'satu':10, 'dua':20, 'tiga':30}

    # tampilan elemen dictionary sebelum diubah
    print("elemen dictionary sebelum diubah: ")
    print(data)

    # mengubah nilai elemen data['data']
    data['satu'] = 60
    # menambahkan nilai elemen data['Satu']
    data['Satu'] = 130

    # tampilan elemen dictionary sesudah diubah 
    print("\nelemen dictionary sesudah diubah: ")
    print(data)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()