#!C:\Python27\python

##################################################################
# judul program: membuat himpunan dengan metode set
##################################################################

# mengubah statemen print menjadi fungsi print()
from __future__ import print_function
import sys

def printElements(dataArray, info):
    # parameter info (informasi)
    print(info)

    # jika data dari elemen dataArray 0 maka cetak himpunan kosong
    if len(dataArray) == 0:
        print("himpunan kosong\n")
        # system exit
        sys.exit(1)
    
    # variabel e = isi elemen dari dataArray
    for e in dataArray:
        # menampilkan data dari indeks ke[0] dan seterusnya
        print(str(e) + " ", end='')
    print("\n")

def main():
    # membuat himpunan
    dataArray = set([11, 22, 33, 44, 55])
    # pemanggilan method printElements
    printElements(dataArray, "elemen awal : ")

    # menambahkan anggota/elemen baru
    # menggunakan metode add()
    dataArray.add(66)
    dataArray.add(77)
    # pemanggilan method printElements
    printElements(dataArray, "setelah pemanggilan add() : ")

    # menambahkan anggota/elemen baru
    # menggunakan metode update()
    dataArray.update([88, 99])
    # pemanggilan method printElements
    printElements(dataArray, "setelah pemanggilan update() : ")

    # menghapus anggota dengan nilai 44
    dataArray.remove(44)
    # pemanggilan method printElements
    printElements(dataArray, "setelah pemanggilan remove() : ")

    # menghapus semua anggota
    dataArray.clear()
    # pemanggilan method printElements
    printElements(dataArray, "setelah pemanggilan celar() : ")

if __name__ == "__main__":
    # pemanggilan method main
    main()