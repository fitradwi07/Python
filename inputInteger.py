#!C:\Python27\python

#######################################
# judul program: input data int
#######################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat prompt untuk tipe data int
    bilanganBulat = int(raw_input("masukan bilangan bulat : "))
    
    # menggunakan variabel untuk proses aritmatika
    hasil = bilanganBulat + 1

    # manampilkan nilai variabel ke layar
    print("bilangan bulat yang dimasukan adalah %d" % (bilanganBulat))
    print("%d + 1 = %d" % (bilanganBulat, hasil))

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # mamanggil fungsi main
    main()