#!C:\Python27\python

##################################################
# judul program: pendeklarasian variabel
#################################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # membuat variabel
    x = 10
    y = 2.34
    z = x * y
    bahasa = 'python'
    kalimat = "pemrograman python"

    # menampilkan nilai variabel ke layar
    print(x)
    print(y)
    print(z)
    print(bahasa)
    print(kalimat)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main()