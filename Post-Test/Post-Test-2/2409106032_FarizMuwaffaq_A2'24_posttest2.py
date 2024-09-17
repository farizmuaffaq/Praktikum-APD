Nama = input("Masukkan nama kamu!:")
NIM = input("Masukkan NIM kamu!:")
HargaBeras = int(input("Masukkan harga beras:"))

DiskonMawar = HargaBeras * 11/100
DiskonSania = HargaBeras * 14/100
DiskonMaknyus = HargaBeras * 17/100

TotalMawar = HargaBeras - DiskonMawar
TotalSania = HargaBeras - DiskonSania
TotalMaknyus = HargaBeras - DiskonMaknyus

print(f"""Nama kamu adalah {Nama} dengan NIM {NIM} akan membeli beras seharga Rp.{HargaBeras}
      Jika kamu membeli beras Mawar, maka kamu harus membayar sebesar Rp.{TotalMawar} karena mendapatkan diskon sebesar 11
      Jika kamu membeli beras Sania, maka kamu harus membayar sebesar Rp.{TotalSania} karena mendapatkan diskon sebesar 14
      Jika kamu membeli beras Maknyus, maka kamu harus membayar sebesar Rp.{TotalMaknyus} karena mendapatkan diskon sebesar 17%""")