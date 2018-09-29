#!C\Python27\python

##############################################################
# judul program: list indeks array negatif
##############################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat list array
    listArray = [100, 200, 300, 400, 500]

    # tampilan list array menentukan indeks negatif diawali dari -1, dihitung dari paling kanan
    print(listArray[-1])
    print(listArray[-2])
    print(listArray[-3])
    print(listArray[-4])
    print(listArray[-5])

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()