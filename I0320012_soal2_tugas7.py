print("=== Program Menghitung Keliling Segitiga beserta Pembulatannya ===")
print()
import math
a = float(input('Masukkan sisi pertama= '))
b = float(input('Masukkan sisi kedua= '))
c = float(input('Masukkan sisi ketiga= '))

#menghitung keliling dan pembulatan kebawah
keliling = a+b+c
print("Keliling segitiga adalah ",keliling,"cm")
print("Hasil pembulatan kebawah keliling segitiga= ", math.floor(keliling),"cm")
print()

#menentukan panjang sisi terpanjang dan terpendek beserta pembulatan keatas
print("Panjang sisi terpanjang segitiga= ", max(a,b,c),"cm")
sisi_terpanjang = max(a,b,c)
print("Hasil pembulatan keatas sisi terpanjang= ", math.ceil(sisi_terpanjang),"cm")
print()
print("Panjang sisi terpendek segitiga= ", min(a,b,c),"cm")
sisi_terpendek = min(a,b,c)
print("Hasil pembulatan keatas sisi terpendek= ", math.ceil(sisi_terpendek),"cm")







