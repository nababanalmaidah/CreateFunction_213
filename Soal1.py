def convert_temperature(value, unit):
    if unit == 'C':
        return value * 9/5 + 32
    if unit == 'F':
        return (value - 32) * 5/9

input_value = int(input("Masukkan nilai : "))
input_unit = input("Masukkan unit : ")

konversi = convert_temperature(input_value, input_unit)
print(konversi)


import math

luas_lingkaran = lambda r: math.pi * r ** 2

jari_jari = float(input("Masukkan jari-jari: "))
hasil = luas_lingkaran(jari_jari)
print("Luas lingkaran dengan jari-jari", jari_jari, "=", round(hasil, 2))