# == Operator dalam bentuk methods ==

# --- Merubah case dari string

# Merubah semua ke upper case
capson = "aightyo!" 
print("normal = " + capson)
capson = capson.upper()
print("upper = " + capson)

# Merubah semua ke lower case
capsoff = "ANJINK LU!" 
print("normal = " + capsoff)
capsoff = capsoff.lower()
print("lower = " + capsoff)

# --- Pengecekan dengan isX method

# Contoh pengecekan lower case
halo = "sus"
checklow = halo.islower()
print(halo + " is lower = " + str(checklow))
checkup = halo.isupper()
print(halo + " is upper = " + str(checkup))

# isalpha() <--- check all letter
# isalnum() <--- cek huruf dan angka
# isdecimal() <--- angka
# isspace() <--- spasi, tab, newline \n
# istitle() <--- semua kata diawali dengan huruf besar

# Example

latin = "Binary Operation"
cek = latin.isalpha()
print(latin + " = ", str(cek))

latin = "Code 110"
cek = latin.isalnum()
print(latin + " = ", str(cek))

latin = "433 081210674953"
cek = latin.isdecimal()
print(latin + " = ", str(cek))

latin = "Code 110\n Death Penalty"
cek = latin.isspace()
print(latin + " = ", str(cek))

title = "Kupu Kupu Kertas"
cek = title.istitle()
print(title + " is title", str(cek)) # Note : Pada judul, dilarang ada kutipan

# Cek Komponen startswith() endswith()

check = "Extraordinary Biased".startswith("Extraordinary")
print("start = " + str(check))
recheck = "Extraordinary Biased".endswith("Biased")
print("finish = " + str(recheck))

# Penggabungan Komponen join() split()

pisah = ['Koharu', 'love', 'Kosuki']
gabung = ','.join(pisah)
gabung1 = ''.join(pisah)
gabung2 = ' '.join(pisah)
gabung3 = ' cie '.join(pisah)
print(pisah), print(gabung), print(gabung1), print(gabung2), print(gabung3)

gabungan = 'imrizzgonnarizztouchrizzyourizz'
print(gabungan.split('rizz'))

# Alokasi Karakter rjust(), ljust(), center()

print(5 * '=' + 'data' + '=' * 5) # Cara Lama

right = 'liberal'.rjust(20, '>')
print('"' + right + '"')

left = 'communist'.ljust(20, 'L')
print('"' + left + '"')

center = 'Non-blok'.center(20, '^')
print('"' + center + '"')

# Kebalikan ===> strip()

center = center.strip('^')
print('"' + center + '"')
