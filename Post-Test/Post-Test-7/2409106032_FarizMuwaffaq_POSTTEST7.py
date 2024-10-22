Data_Pirate = {}

def Lihatdata():
    if len(Data_Pirate) == 0:
        print("Data Belum Ditambahkan")
    else:
        for Id, (Nama, Data) in enumerate(Data_Pirate.items()):
            print(f"\nID = {Id + 1}\nNama Pirate : {Nama}\nBuah Iblis : {Data['BuahIblis']}\nRas : {Data['Ras']}\nBounty : {Data['Bounty']}")

def TambahData():
    nama = input("MASUKKAN NAMA PIRATE : ")
    buahiblis = input("MASUKKAN BUAH IBLIS : ")
    ras = input("MASUKKAN RAS : ")
    while True:
        bounty = int(input("MASUKKAN BOUNTY : "))
        if bounty <= 0:
            print("Bounty Tidak Bisa Kurang Dari 0")
        else:
            break
    Data_Pirate[nama] = {"BuahIblis": buahiblis, "Ras": ras, "Bounty": bounty}
    print("Data Telah Ditambahkan")
    
    
def PerbaruiData():
    if len(Data_Pirate) == 0:
        print("Data Belum Ada")
    else:
        Perbarui = input("Masukkan ID Data Yang Ingin Diperbarui : ")
        NamaPirate = list(Data_Pirate.keys())[Perbarui]
        NamaBaru = input("Masukkan Nama Baru : ")
        DF_Baru = input("Masukkan Buah Iblis Baru : ")
        RasBaru = input("Masukkan Ras Baru : ")
        while True:
            BountyBaru = int(input("Masukkan Bounty Baru : "))
            if BountyBaru <= 0:
                print("Bounty Tidak Bisa Kurang Dari 0")
            else:
                break
        Data_Pirate[NamaBaru] = Data_Pirate.pop(NamaPirate)
        NamaPirate = NamaBaru
        Data_Pirate[NamaPirate]["BuahIblis"] = DF_Baru
        Data_Pirate[NamaPirate]["Ras"] = RasBaru
        Data_Pirate[NamaPirate]["Bounty"] = BountyBaru
        print("Data Berhasil Diperbarui")
        
def HapusData():
    Hapus = input("Masukkan Data Siapa Yang Ingin Dihapus : ")
    if Hapus in Data_Pirate:
        del Data_Pirate[Hapus]
    else:
        print("Data Tidak Ada")
        
def KeluarMenu():
    print("Terima Kasih Telah Mengakses Pusat Data Pirate")
    exit()

def TampilanMenu():
    print("""
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
""")

def Program():
    TampilanMenu()
    try:
        pilih = int(input("PILIH MENU : "))
        if pilih == 1:
            Lihatdata()
        elif pilih == 2:
            TambahData()
        elif pilih == 3:
            PerbaruiData()
        elif pilih == 4:
            HapusData()
        elif pilih == 5:
            KeluarMenu()
        else:
            print("Pilihan Menu Tidak Ada")
    except ValueError:
        print("\nHanya Dapat Memasukkan Input Berupa Angka")
        
while True:
    Program()