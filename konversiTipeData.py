#!C:\Python27\python

###############################################################
# judul program: konversi variabel dari string ke integer
###############################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat prompt untuk tipe data string
    s = raw_input("masukan bilangan genap : ")
    
    # melakukan konversi dari string ke integer
    bilanganBulat = int(s)

    # proses perhitungan aritmatika
    hasil = bilanganBulat + 1

    # manampilkan hasil ke layar
    print("bilangan yang dimasukan adalah %d" % (bilanganBulat))
    print("%d + 1 = %d" % (bilanganBulat, hasil))

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()