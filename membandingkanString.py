#!C:\Python27\python

#################################################
# judul program: membandingkan 2 buah string
#################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # deklarasi variabel string
    stringPertama = 'python'
    stringKeDua = "python"

    # menampilkan hasil deklarasi string ke layar
    print("string pertama adalah " + stringPertama)
    print("string ke dua adalah " + stringKeDua)

    # stringPertama == stringKeDua, maka menjalankan statemen if
    if stringPertama == stringKeDua:
        print("stringPertama sama dengan stringKeDua")
    # stringPertama != stringKeDua, maka menjalankan statemen else
    else:
        print("stringPertama tidak sama dengan stringKeDua")

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()