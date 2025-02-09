print("===PART 1===")

# angka satuan (integer)
data_integer = 1
print("data :", data_integer, ", bertipe", type(data_integer))

# desimal (float)
data_float = 1.5
print(type(data_float))

# kumpulan karakter (string)
data_string = "ucok"
print(type(data_string))

# The Ending is getting closer

# biner true/false (boolean)
data_biner = True
print(type(data_biner))

# bilangan kompleks
kompleks = complex(6,5)
print("data", kompleks, "bertipe",type(kompleks))

# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data", data_c_double, "bertipe",type(data_c_double))

print("")

print("===PART 2===")

# Casting : merubah dari satu tipe ke tipe lain

# Integer
print("===INTEGER===")
data_int = 6
# ---------------------
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # false jika nilai int = 0
print("data =", data_int, "bertipe", type(data_int))
print("data =", data_float, "bertipe", type(data_float))
print("data =", data_str, "bertipe", type(data_str))
print("data =", data_bool, "bertipe", type(data_bool))

# Float
print("===FLOAT===")
data_float = 6.7
# ---------------------
data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # false jika nilai float = 0
print("data =", data_int, "bertipe", type(data_int))
print("data =", data_float, "bertipe", type(data_float))
print("data =", data_str, "bertipe", type(data_str))
print("data =", data_bool, "bertipe", type(data_bool))

# Boolean
print("===BOOLEAN===")
data_bool = False 
# ---------------------
data_int = int(data_bool) 
data_float = float(data_bool)
data_str = str(data_bool)
print("data =", data_int, "bertipe", type(data_int))
print("data =", data_float, "bertipe", type(data_float))
print("data =", data_str, "bertipe", type(data_str))
print("data =", data_bool, "bertipe", type(data_bool))

# String
print("===STRING===")
data_str = "0"
# ---------------------
data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str) # false jika string kosong
print("data =", data_int, "bertipe", type(data_int))
print("data =", data_float, "bertipe", type(data_float))
print("data =", data_str, "bertipe", type(data_str))
print("data =", data_bool, "bertipe", type(data_bool))