


print(
"""
=================================================
======>            Data Pirate            <======
=================================================
==     Selamat Datang Di Pusat Data Pirate     ==
==   Silahkan Memilih Menu Untuk Melanjutkan   ==
==                                             ==
== 1. LIHAT DATA                               ==
== 2. TAMBAHKAN DATA                           == 
== 3. PERBARUI DATA                            ==
== 4. HAPUS DATA                               ==
== 5. KELUAR                                   == 
=================================================
"""
)

Data_Pirate = []
id_pirate = 1

while True:
    pilih = int(input("PILIH MENU : "))
    if pilih == 1:
        if len(Data_Pirate) == 0:
            print("Data Belum Ditambahkan")
        else:
            for i in range(len(Data_Pirate)):
                print(f"\nData Pirate {i+1}\nNAMA PIRATE : {Data_Pirate[i][0]} \nBUAH IBLIS : {Data_Pirate[i][1]}\nRAS : {Data_Pirate[i][2]}\nBOUNTY : {Data_Pirate[i][3]}")
    elif pilih == 2:
        nama = input("NAMA PIRATE : ")
        buahiblis = input("BUAH IBLIS : ")
        ras = input("RAS : ")
        bounty = int(input("BOUNTY : "))
        Data_Pirate.append([nama,buahiblis,ras,bounty])
        print("Data Berhasil Ditambahkan")
    elif pilih == 3:
        Data_lama = input("\nPilih Data Yang Ingin Diganti: ")
        for i in range(len(Data_Pirate)):
            if Data_Pirate[i][0] == Data_lama:
                Nama_baru = input("Masukkan Nama Baru: ")
                DF_baru = (input("Masukkan Buah Iblis Baru : "))
                Ras_baru = input("Masukkan Ras Baru : ")
                Bounty_baru = int(input("Masukkan Bounty Baru : "))
                while Bounty_baru <= 0:
                    print("Bounty Tidak Bisa Lebih Kecil Dari 0")
                    Bounty_baru = int(input("Masukkan Bounty Baru : "))
                Data_Pirate[i][0] = Nama_baru
                Data_Pirate[i][1] = DF_baru
                Data_Pirate[i][2] = Ras_baru
                Data_Pirate[i][3] = Bounty_baru
                break
        else:
            print("Data Tidak Ada")
    elif pilih == 4:
        if len(Data_Pirate) == 0:
            print("Data Belum Ditambahkan")
        else:
            Data_Hapus = input("\nMasukkan Data Yang Ingin Dihapus: ")
            for i in range(len(Data_Pirate)):
                if Data_Pirate[i][0] == Data_Hapus:
                    del Data_Pirate[i]
                    print("Data Telah Dihapus")
                    break
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Pusat Data Pirate")
        break
    else:
        print("Anda Salah Input")