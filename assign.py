# Operasi Assignment --> operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5 # adalah assignment
print('nilai a =', a)

a += 2
print('a = a + 2 dapat ditulis a += 2 sehingga hasilnya', a)

a -= 2
print('a = a - 2 dapat ditulis a -= 2 sehingga hasilnya', a)

a *= 2
print('a = a * 2 dapat ditulis a *= 2 sehingga hasilnya', a)

a /= 2
print('a = a / 2 dapat ditulis a /= 2 sehingga hasilnya', a)

a **= 2
print('a = a ** 2 dapat ditulis a **= 2 sehingga hasilnya', a)

# ==========================================================

b = 10
print('\nnilai b =', b)

b %= 4
print('b = b % 4 dapat ditulis b %= 4 sehingga hasilnya', b)

b //= 3
print('b = b // 3 dapat ditulis b //= 3 sehingga hasilnya', b)

# ==========================================================

# Operasi bitwise
c = True
print('\nnilai c =', c)

c |= False
print('c = c | False dapat ditulis c |= False sehingga hasilnya', c)

c &= True
print('c = c & True dapat ditulis c &= True sehingga hasilnya', c)

c ^= True
print('c = c ^ True dapat ditulis c ^= True sehingga hasilnya', c)

# geser geser
d = 0b0111
print('\n nilai d =', d, format(d,'04b'))

d >>= 2
print('d = d >> 2 dapat ditulis d >>= 2 sehingga hasilnya', d, format(d,'04b'))

d <<= 2
print('d = d << 2 dapat ditulis d <<= 2 sehingga hasilnya', d, format(d,'04b'))

# Note : Jika ada variable yang sama tapi memiliki nilai yang berbeda,
# komputer membaca dari variable yang paling akhir (terbaru)