#!C:\Python27\python

##################################################
# judul program: operasi aritmatika
##################################################

# mengubah statemen print menjadi fungsi print()
from __future__ import print_function
import os 

def main():
    # mendefinisikan variabel x dan y
    x = 10
    y = 3

    # menampilkan nilai x dan y
    print("x = ", x)
    print("y = ", y)

    # melakukan perhitungan terhadap nilai x dan y
    print("x + y = ", (x + y))
    print("x - y = ", (x - y))
    print("x * y = ", (x * y))
    print("x / y = ", (x / y))
    print("x // y = ", (x // y))
    print("x % y = ", (x % y))
    print("x ** y = ", (x ** y))

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil method main
    main()