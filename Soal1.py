def convert_temperature(value, unit):
    if unit == 'C':
        return value * 9/5 + 32
    if unit == 'F':
        return (value - 32) * 5/9

input_value = int(input("Masukkan nilai : "))
input_unit = input("Masukkan unit : ")

konversi = convert_temperature(input_value, input_unit)
print(konversi)