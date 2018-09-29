#!C:\Python27\python

#####################################################
# judul program: mencari elemen didalam list
#####################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat list array
    buah = ["durian", "mangga", "apel"]
    # tampilan isi array
    print(buah)

    # mencari indeks elemen array
    print('"durian" berada pada indeks ke-', buah.index("durian"))
    print('"apel" berada pada indeks ke-', buah.index("apel"))

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()