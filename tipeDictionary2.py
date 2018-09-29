#!C:\Python27\python

################################################################
# judul program: penggunaan tipe data dictionary gabungan
################################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat nilai dictionary berbeda tipe data 
    # nama, uts, uas sebagai key atau indeks
    # fitra, 92.5, 92.75, A sebagai value atau nilai
    data = {'nama':"fitra", 'uts':95.25, 'uas':92.75, 'nilai':'A'}

    # menampilkan nilai dictionay ke layar
    print("nama: ", data['nama'])
    print("nilai uts: ", data['uts'])
    print("nilai uas: ", data['uas'])
    print("nilai indeks: ", data['nilai'])

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()