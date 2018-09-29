#!C:\Python27\python

###############################################
# judul program: penggunaan escape sequence
###############################################

# statemen print diubah menjadi fungsi print()
from __future__ import print_function
import os

def main():
    # deklarasi string 
    stringPertama = 'petik tunggal \'escape\', petik ganda "OK"'
    stringKeDua = "petik tunggal 'OK', petik ganda \"escape\""
    stringKeTiga = "baris pertama\nbaris ke dua"
    
    # menampilkan hasil ke layar
    print(stringPertama)
    print(stringKeDua)
    print(stringKeTiga)

    # perintah pause
    os.system("pause")

if __name__ == "__main__":
    # memanggil fungsi main
    main() 