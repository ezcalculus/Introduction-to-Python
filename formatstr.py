# format string

# contoh generic

# string
name = "curacao"
format_str = f"hello {name}"
print(format_str)

# angka
number = 1123.8
format_str = f"angka = {number}"
print(format_str)

# boolean
bool = True
format_str = f"boolean = {bool}"
print(format_str)

# integer
angka = 20
format_str = f"int = {angka:d}"
print(format_str)

# ordo ribuan
angka = 10**9
format_str = f"ribuan = {angka:,}"
print(format_str)

# float
angka = 3.14653473
format_str = f"float = {angka:.4f}"
print(format_str)

# Menampilkan leading zero
angka = 3.14653473
format_str = f"float = {angka:08.4f}"
print(format_str)

# Menampilkan tanda + -
min = -10.123456789
plus = +10.123456789
format_min = f"minus = {min:+.3f}"
format_plus = f"plus = {plus:+.9f}"
print(format_min)
print(format_plus)

# Format %
persentase = 0.66
format_persen = f"persen = {persentase:.0%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
value = 10000.500
jumlah = 5
format_str = f"total value = {value*jumlah:.1f}"
print(format_str)

# format angka lain (biner, oktal, hexadesimal)
number = 512
format_binary = f"biner = {bin(number)}"
format_octal = f"oktal = {oct(number)}"
format_hex = f"hex = {hex(number)}"

print(format_binary)
print(format_octal)
print(format_hex)