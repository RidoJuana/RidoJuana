import math


# Jari-jari lingkaran
r = 10

# Menghitung luas lingkaran
luas_lingkaran = math.pi * r**2

print("Luas lingkaran dengan jari-jari", r, "adalah:", luas_lingkaran)
      
# Suhu dalam derajat Celsius
celsius = 130

# Menghitung konversi ke Fahrenheit
fahrenheit = (9/5) * celsius + 32

print("Suhu", celsius, "derajat Celsius sama dengan", fahrenheit, "derajat Fahrenheit")

# Masukkan nilai alas dan tinggi
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Menghitung luas segitiga
luas_segitiga = 0.5 * alas * tinggi

print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah:", luas_segitiga)