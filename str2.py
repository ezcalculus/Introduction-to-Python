# ======================================================================== #

# Operation and Manipulation String

# -------- menyambung string (concatenate) --------
first_name = "Axel"
middle_name = "Jonas"
last_name = "Siahaan"

full_name = first_name + " " + middle_name + " " + last_name
print(full_name)

# -------- menghitung panjang string --------
length = len(full_name)
print('panjang dari' + " " + full_name + ' = ' + str(length))

# -------- operator untuk string --------

# mengecek apakah ada komponen char atau string di string

q = "x"
status = q in full_name
print('string' + " " + q + ' ada di' + " " + full_name + ' = ' + str(status))

q = "&"
status = q not in full_name
print('string' + " " + q + ' ada di' + " " + full_name + ' = ' + str(status))

# mengulang string
print('huwala humba '*3)
print(3*'huwala humba ')

# indexing
print('index ke-7 : ' + full_name[7]) # index pertama dimulai dari nol
print('index ke-2 : ' + full_name[2]) 
print('index ke-4 : ' + full_name[4]) 
print('index ke-(-11) : ' + full_name[-11]) # urutan mundur jika negative
print('index ke-[0:3] : ' + full_name[0:3]) # range (karakter terakhir (index 3 = l)) tidak diprint oleh python
print('index ke-[0:10:5] : ' + full_name[0:10:5]) # deret interval tertentu

# item paling kecil (character dengan nilai ASCII code terbesar)
print('paling kecil : ', min(full_name))
# item paling besar
print('paling besar : ', max(full_name))

ascii_code = ord('x')
print('ASCII code untuk x adalah' + ' ' + str(ascii_code))
data = 121
print('char untuk ASCII 121 adalah' + ' ' + chr(data))

# -------- operator dalam bentuk method --------

data = 'cahyadi daddy fatherless'
jumlah = data.count("d")
print('jumlah chara d pada', data, '=', str(jumlah))
# ======================================================================== #