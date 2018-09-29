#!C:\Python27\python

###################################################
# judul program: input data pecahan\bilangan Riil
###################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat prompt untuk tipe data float
    bilanganRiil = float(raw_input("masukan bilangan riil : "))

    # proses perhitungan aritmatika
    hasil = bilanganRiil * 2

    # menampilkan hasil ke layar
    print("bilangan yang dimasukan adalah %f" % (bilanganRiil))
    print("%2f x 2 = %2f " % (bilanganRiil, hasil))

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()