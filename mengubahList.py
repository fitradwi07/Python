#!C\Python27\python

######################################################
# judul program: mengubah nilai elemen didalam list
######################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat list array
    buah = ["durian", "mangga", "apel"]
    # tampilan sebelum diubah isi list
    print("sebelum diubah: ")
    print(buah)

    # mengubah nilai elemen list
    # buah[1] = mangga menjadi salak
    # buah[-1] = apel menjadi pepaya
    buah[1] = "salak"
    buah[-1] = "pepaya"

    # tampilan sesudah diubah isi list
    print("\nsetelah diubah: ")
    print(buah)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi mains
    main()