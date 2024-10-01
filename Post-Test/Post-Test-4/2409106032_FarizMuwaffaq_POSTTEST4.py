Username = "fariz"
Password = "32"
kesempatan = 0

print("""
      Selamat datang di Bank.
      Harap Login Terlebih Dahulu
      """)

while kesempatan < 3:
    username = str(input("Masukkan Username Anda! "))
    password = str(input("Masukkan Password Anda! "))
    if Username == username and Password == password:
        print("""
            Anda berhasil login
            Selamat Datang :)
            """)
        break
    else:
        print("Username atau Password Salah!")
        kesempatan += 1
        if kesempatan == 3:
            print("Anda telah melakukan kesalahan sebanyak 3 kali, silahkan memulai program kembali.")
            exit()
        
while True:
    Nama = input("Masukkan Nama Kamu! ")
    NIM = input("Masukkan NIM Kamu! ")
    BanyakPinjaman = int(input("Masukkan Jumlah Pinjaman! "))
    LamaPinjaman = int(input("Masukkan Lama Pinjaman(Tahun) "))
    JumlahBulan = 12 * LamaPinjaman

    if LamaPinjaman == 1:
        BungaPerTahun = 7/100
        BungaPerBulan = (BungaPerTahun/12) * BanyakPinjaman
        TotalCicilanPerBulan = (BanyakPinjaman + BungaPerBulan)/JumlahBulan
        print(f"""
            Nama kamu adalah {Nama}. Dengan NIM {NIM}.
            Cicilan perbulan yang harus kamu bayar adalah {int(TotalCicilanPerBulan)}
            """)
        while True:
            ulang = input("Apakah anda ingin memulai ulang program?[y/n]")
            if ulang == "y":
                break
            elif ulang == "n":
                print("Program akan dihentikan")
                exit()
            else:
                print("Hanya dapat memasukkan input y/n")
                continue
    elif LamaPinjaman == 2:
        BungaPerTahun = 13/100
        BungaPerBulan = (BungaPerTahun/12) * BanyakPinjaman
        TotalCicilanPerBulan = (BanyakPinjaman + BungaPerBulan)/JumlahBulan
        print(f"""
            Nama kamu adalah {Nama}. Dengan NIM {NIM}.
            Cicilan perbulan yang harus kamu bayar adalah {int(TotalCicilanPerBulan)}
            """)
        while True:
            ulang = input("Apakah anda ingin memulai ulang program?[y/n]")
            if ulang == "y":
                break
            elif ulang == "n":
                print("Program akan dihentikan")
                exit()
            else:
                print("Hanya dapat memasukkan input y/n")
                continue
    elif LamaPinjaman == 3:
        BungaPerTahun = 19/100
        BungaPerBulan = (BungaPerTahun/12) * BanyakPinjaman
        TotalCicilanPerBulan = (BanyakPinjaman + BungaPerBulan)/JumlahBulan
        print(f"""
            Nama kamu adalah {Nama}. Dengan NIM {NIM}.
            Cicilan perbulan yang harus kamu bayar adalah {int(TotalCicilanPerBulan)}
            """)
        while True:
            ulang = input("Apakah anda ingin memulai ulang program?[y/n]")
            if ulang == "y":
                break
            elif ulang == "n":
                print("Program akan dihentikan")
                exit()
            else:
                print("Hanya dapat memasukkan input y/n")
                continue
    else:
        print("Hanya dapat melakukan pinjaman 1-3 tahun!")
        break