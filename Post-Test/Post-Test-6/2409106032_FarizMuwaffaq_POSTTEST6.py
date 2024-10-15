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
pirate_id = 1

while True:
    pilih = int(input("PILIH MENU : "))
    if pilih == 1:
        if len(Data_Pirate) == 0:
            print("Data Belum Ditambahkan")
        else:
            for Data in Data_Pirate:
                print(f"""
Data Pirate {Data['id']} 
Nama Pirate : {Data['Nama']}
Buah Iblis : {Data['Buahiblis']}
Ras : {Data['Ras']}
Bounty : {Data['Bounty']}""")
    elif pilih == 2:
        nama = input("MASUKKAN NAMA PIRATE : ")
        buahiblis = input("MASUKKAN BUAH IBLIS : ")
        ras = input("MASUKKAN RAS : ")
        bounty = input("MASUKKAN BOUNTY : ")
        
        pirate = {
            'id': pirate_id,
            'Nama': nama,
            'Buahiblis': buahiblis,
            'Ras': ras,
            'Bounty': bounty              
        }
        Data_Pirate.append(pirate)
        pirate_id += 1
        print("Data Telah Ditambahkan")
    elif pilih == 3:
        DataPirate = int(input("Masukkan Data Yang Ingin Diperbarui : "))
        Ditemukan = False
        for Data in Data_Pirate:
            if Data['id'] == DataPirate:
                Data['Nama'] = input("Masukkan Nama Baru : ")
                Data['Buahiblis'] = input("Masukkan Buah Iblis baru : ")
                Data['Ras'] = input("Masukkan Ras Baru : ")
                Data['Bounty'] = input("Masukkan Bounty Baru : ")
                Ditemukan = True
                print("Data Telah Diperbarui!")
                break
        if not Ditemukan:
            print("Data Tidak Ditemukan")
    elif pilih == 4:
        if len(Data_Pirate) == 0:
            print("Data Belum DItambahkan")
        else:
            DataPirate = int(input("Masukkan Data Yang Ingin dihapus : "))
            for Data in Data_Pirate:
                if Data['id'] == DataPirate:
                    del Data['Nama']
                    del Data['Buahiblis']
                    del Data['Ras']
                    del Data['Bounty']
                    print("Data Telah Dihapus")
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Pusat Data Pirate")
        break
    else:
        print("Anda Salah Input")