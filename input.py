# input user

# data yang dimasukkan pasti bersifat string
data = input("Input your ID :")
print("data =", data, "tipe =", type(data))

# menggunakan sifat data
data_int = int(input("Input your pin : "))
print("PIN anda adalah", data_int, "dan bertipe", type(data_int))

data_fl = float(input("Input your GPA : "))
print("GPA", data_fl, "You can take 24 SKS from your last GPA and the type is", type(data_fl))

data_str = str(input("Grade : "))
print("Your grade is", data_str, ", You can take Quantum Physics lecture because you have", data_str, "grade and the type is", type(data_str))

boolean = bool(float(input("Input any number from 1 to 10 : ")))
print("Your status are", boolean, ", you can go to next location and the type is", type(boolean))