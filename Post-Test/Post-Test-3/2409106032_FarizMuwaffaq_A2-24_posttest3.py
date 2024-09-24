Nama = input("Masukkan Nama Kamu!")
NIM = input("Masukkan NIM Kamu!")
BanyakPinjaman = int(input("Masukkan Jumlah Pinjaman!"))
LamaPinjaman = int(input("Masukkan Lama Pinjaman(Tahun)"))
JumlahBulan = 12 * LamaPinjaman

if LamaPinjaman == 1:
    BungaPerTahun = 7/100
    BungaPerBulan = (BungaPerTahun/12) * BanyakPinjaman
    TotalCicilanPerBulan = (BanyakPinjaman + BungaPerBulan)/JumlahBulan
    print(f"""
          Nama kamu adalah {Nama}. Dengan NIM {NIM}.
          Cicilan perbulan yang harus kamu bayar adalah {TotalCicilanPerBulan}
          """)
elif LamaPinjaman == 2:
    BungaPerTahun = 13/100
    BungaPerBulan = (BungaPerTahun/12) * BanyakPinjaman
    TotalCicilanPerBulan = (BanyakPinjaman + BungaPerBulan)/JumlahBulan
    print(f"""
          Nama kamu adalah {Nama}. Dengan NIM {NIM}.
          Cicilan perbulan yang harus kamu bayar adalah {TotalCicilanPerBulan}
          """)
elif LamaPinjaman == 3:
    BungaPerTahun = 19/100
    BungaPerBulan = (BungaPerTahun/12) * BanyakPinjaman
    TotalCicilanPerBulan = (BanyakPinjaman + BungaPerBulan)/JumlahBulan
    print(f"""
          Nama kamu adalah {Nama}. Dengan NIM {NIM}.
          Cicilan perbulan yang harus kamu bayar adalah {TotalCicilanPerBulan}
          """)
else:
    print("Hanya dapat melakukan pinjaman 1-3 tahun!")
