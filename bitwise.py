# Operator bitwise (Binary operation)

# syntax format(variable, '08b') untuk mengubah desimal ke binary 8 digit
a = 7
b = 4
print('a dalam biner --> ', format(a, '08b'))
print('b dalam biner --> ', format(b, '08b'))

print('\n=====OR (|)=====')
c = a | b
print('Desimal --> ', c, '\nBiner --> ', format(c, '08b'))

print('\n=====AND (&)=====')
c = a & b
print('Desimal --> ', c, '\nBiner --> ', format(c, '08b'))

print('\n=====XOR (^)=====')
c = a ^ b
print('Desimal --> ', c, '\nBiner --> ', format(c, '08b'))

print('\n=====NOT (~)=====')
x = ~a
y = ~b
z = (x | y)
print('Desimal --> ', x, '\nBiner --> ', format(x, '08b'), '\n')
print('Desimal --> ', y, '\nBiner --> ', format(y, '08b'), '\n')
print('Desimal --> ', z, '\nBiner --> ', format(z, '08b'), '\n')

print('\n=====Cara flip False ke True atau sebaliknya satu-satu=====')
d = 0b00000111 # syntax untuk mengubah Binary ke angka 7
e = 0b00000100 # syntax untuk mengubah Binary ke angka 4
f = 0b11111111 # Operator
print('nilai f = ', f)
print(format(f^d, '08b')) # XOR f dengan d untuk flip logika True dan False
print(format(f^e, '08b')) # XOR f dengan e untuk flip logika True dan False

# Shifting

print('\n=====Shifting right (>>)=====')
x = a >> 2
print('Desimal --> ', a, '\nBiner --> ', format(a, '08b'), '\n')
print('Desimal --> ', x, '\nBiner --> ', format(x, '08b'), '\n')
y = b >> 2
print('Desimal --> ', b, '\nBiner --> ', format(b, '08b'), '\n')
print('Desimal --> ', y, '\nBiner --> ', format(y, '08b'), '\n')

print('\n=====Shifting left (<<)=====')
x = a << 2
print('Desimal --> ', a, '\nBiner --> ', format(a, '08b'), '\n')
print('Desimal --> ', x, '\nBiner --> ', format(x, '08b'), '\n')
y = b << 2
print('Desimal --> ', b, '\nBiner --> ', format(b, '08b'), '\n')
print('Desimal --> ', y, '\nBiner --> ', format(y, '08b'), '\n')