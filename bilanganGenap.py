#!C:\Python27\python

##########################################################
# judul program: mencari bilangan genap
##########################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def hitungBilanganGenap():
    # input data int 
    bilangan = int(input("masukan panjang angka : "))

    # range sampai dengan jumlah angka yang diinputkan
    for i in range (0, bilangan+1):
        # data pertama(i) % 2 == 0 maka akan eksekusi statemen if
        if (i%2==0):
            print(i, "adalah bilangan genap")
        # data pertama(i) % 2 != 0 maka akan eksekusi statemen else
        else:
            print(i, "adalah bukan bilangan genap")
    
    # perintah pause 
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi hitungBilanganGenap
    hitungBilanganGenap()