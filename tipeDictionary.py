#!C:\Python27\python

##################################################
# judul program: penggunaan tipe data dictionary
##################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # deklarasi array
    # satu, dua, tiga sebagai key atau indeks
    # 10, 20, 30 sebagai value atau nilai
    d = {'satu':10, 'dua':20, 'tiga':30}

    # menempilkan hasil ke layar
    print("d['satu']: ", d['satu'])
    print("d['dua']: ", d['dua'])
    print("d['tiga']: ", d['tiga'])
    print("d['dua'] * d['tiga']: ", d['dua'] * d['tiga'])

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()