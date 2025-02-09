# Date and Time (Exercise)

import datetime as dt

today = dt.date.today()

print(today)

tanggal = dt.date(2004,2,7)
print(tanggal)
print(f"Hari lahir saya jatuh pada {tanggal:%A}")

# Contoh lain

input 