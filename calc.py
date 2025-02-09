def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Tidak bisa membagi dengan nol!"
    return x / y

print("Pilih Operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True:
    # Pilih operasi
    choice = input("Masukkan pilihan (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue

        if choice == '1':
            print("Hasil:", add(num1, num2))
        elif choice == '2':
            print("Hasil:", subtract(num1, num2))
        elif choice == '3':
            print("Hasil:", multiply(num1, num2))
        elif choice == '4':
            print("Hasil:", divide(num1, num2))

    else:
        print("Pilihan tidak valid.")

    # Tanya pengguna apakah ingin melakukan perhitungan lagi
    next_calculation = input("Ingin melakukan perhitungan lain? (ya/tidak): ")
    if next_calculation.lower() != 'ya':
        break

print("Terima kasih telah menggunakan kalkulator!")
