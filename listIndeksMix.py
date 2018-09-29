#!C:\Python27\python

###################################################
# judul program: melihat list indeks campuran
###################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat list array campuran
    listArray = [1, "durian", 2, "mangga", 3, "apel"]

    # tampilan list array
    print(listArray[0])
    print(listArray[1])
    print(listArray[2])
    print(listArray[3])
    print(listArray[4])
    print(listArray[5])

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()