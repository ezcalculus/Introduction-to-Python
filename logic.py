# operasi logika atau boolean

# not, or, and, xor

a = True
b = False

print("---Operasi NOT---")
print("not a =", not a)
print("not b =", not b)

print("---Operasi OR---")
print(b, "OR", b, "=", b or b)
print(b, "OR", a, "=", b or a)
print(a, "OR", b, "=", a or b)
print(a, "OR", a, "=", a or a)

print("---Operasi AND---")
print(b, "AND", b, "=", b and b)
print(b, "AND", a, "=", b and a)
print(a, "AND", b, "=", a and b)
print(a, "AND", a, "=", a and a)

print("---Operasi XOR---")
print(b, "XOR", b, "=", b ^ b)
print(b, "XOR", a, "=", b ^ a)
print(a, "XOR", b, "=", a ^ b)
print(a, "XOR", a, "=", a ^ a)