#!C\Python27\python

#################################################
# judul program: deklarasi string
#################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # dekalrasi string
    stringPertama = 'string pertama'
    stringKeDua = "string ke dua"

    # menmapilkan hasil ke layar
    print(stringPertama)
    print(stringKeDua)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()

