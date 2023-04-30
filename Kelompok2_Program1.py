print("Kelompok 2 Tubes Algoritma Pemrograman")
print("_"*30)
print(" "*20)
print("Program Data Nama dan NIM Mahasiswa")
print("="*30)

import pandas as pd
import numpy as np

# Deklarasi Variabel
data_mahasiswa = []
total_data = 0
next = "y"

while (next == "y") :
    # MENU
    print("[+]== MENU ==[+]")
    print("1. Input Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Tampilkan Data Frame")

    choice = int(input("[+] Pilih Menu : "))
    print("")
    if(choice == 1) :
        n = int(input("Banyak Data : "))
        total_data += n
        for i in range(n):
            temp = []
            nama = input("%d. Masukkan Nama : " % (i+1))
            temp.append(nama)
            nim = input("   Masukkan NIM  : ")
            temp.append(nim)
            data_mahasiswa.append(temp)
            print("")


        print("[+] Selesai Input [+]")

    elif(choice == 2) :
        for i in range(total_data):
            print("%d. Nama : %s" % ((i+1), data_mahasiswa[i][0]))
            print("   NIM  : ", data_mahasiswa[i][1])
            print()

    elif(choice == 3) :
        data_frame = pd.DataFrame(np.array(data_mahasiswa).reshape(2, len(data_mahasiswa)), columns = ['Nama', 'NIM'])
        print(data_frame)
        print()
    else :
        print("Menu tidak tersedia, Harap pilih menu dengan benar !")

    next = input("Apakah ingin melanjutkan program ?(y/n) : ")
    print("\n")