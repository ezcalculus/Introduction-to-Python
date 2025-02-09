# Introduction to String

# -------- How to make str --------

data = "This is a string"
print (data, type(data))

# Single Quote ('...')
data = 'This is a single quote'
print(data)

# Double Quote
data = "This is a double quote"
print(data)

# Both single and double
data = "'Piye kabare toh, wenak jamanku tenan'"
print(data)

data = '"Piye kabare toh, wenak jamanku tenan"'
print(data)

# -------- Tanda \ --------

# Tanda \

# Membuat tanda ' menjadi str
print('Mari shalat jum\'at')
print('g\'day mate, how ya\' doin\'?, see ya')

# backslash
print("C:\\user\\JMS")

# tab
print("ucup\totong, jauhan")

# backspace
print('ucup \botong')

# New line
print('Alisa with Jody Cambridge in Oxford \nno offense') # --> (LF) line feed --> unix, macOS, linux
print('Alisa with Jody Cambridge in Oxford \rno offense') # --> (CR) carriage return --> commodore, acorn, lisp
print('Alisa with Jody Cambridge in Oxford \r\nno offense') # --> (CRLF) line feed carriage return --> dipakai oleh windows

# -------- str literal atau raw --------

# hati-hati
print('C:\new folder') # Path-nya akan salah

# menggunakan raw string
print(r'C:\new folder') # membuat str tanpa terhalang dengan sign-sign tertentu

# multiline literal str
print("""
Nama    : X=ABC
Class   : S
4chan   : XyzscizoR
Body    : 144
website : aphrodite.org
""")
