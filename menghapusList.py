#!C:\Python27\python

####################################################
# judul program: menghapus elemen dari list
####################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat list array
    buah = ["durian", "mangga", "apel"]
    # tampilan isi elemen array sebelum dihapus
    print("sebelum dihapus: ")
    print(buah)

    # mengapus isi elemen array
    buah.remove("durian")
    buah.remove("apel")

    # tampilan isi elemen array setelah dihapus
    print("\nsetelah dihapus: ")
    print(buah)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()