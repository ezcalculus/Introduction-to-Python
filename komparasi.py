# setiap hasil adalah boolean

# >, <, >=, <=, ==, !=, is, is not

# Diketahui
a = 5
b = 3
c = a
d = b

# lebih dari > 
print("---lebih dari (>)---")
x = a > b
print(a, ">", b, "=", x)    

# kurang dari <
print("---kurang dari (<)---")
y = b < a
print(b, "<", a, "=", y) 

# lebih dari sama dengan >=
print("---lebih dari sama dengan (>=)---")
z = c >= a
print(c, ">=", a, "=", z)

# kurang dari sama dengan <=
print("---kurang dari sama dengan (<=)---")
v = d <= b
print(d, "<=", b, "=", v)

# sama dengan ==
print("---sama dengan (==)---")
w = a == 5
print(a, "==", 5, "=", w)

# tidak sama dengan !=
print("---tidak sama dengan (!=)---")
t = a != 25
print(a, "!=", 25, "=", t)

# is
print("---is---")
alpa = a is c
print("a is c =", alpa)

# is not
print("---is not---")
beta = a is not b
print("a is not b =", beta)

# ---------------------------------------

i = 5
j = 6
k = 6
print("nilai i =", i, "id =", hex(id(i)))
print("nilai j =", j, "id =", hex(id(j)))
print("nilai k =", k, "id =", hex(id(k)))
print(id(i))
print(id(j))
print(id(k))