# Width and Multiline

# Data
data_nama = "William Minerva"
data_umur = 44
data_tinggi = 186.7
data_sepatu = 42
data_body = 7

# String
data_str = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_sepatu}, bitch = {data_body})"
print(5 * "=" + "Data String" + 5 * "=")
print(data_str)

# String Multiline (Menggunakan enter, newline \n)
data_str = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_sepatu}, \nbitch = {data_body}"
print("\n" + 5 * "=" + "Data String" + 5 * "=")
print(data_str)

# String Multiline (kutip triplets)
data_str = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_sepatu}
bitch = {data_body}
"""
print("\n" + 5 * "=" + "Data String" + 5 * "=")
print(data_str)

# Mengatur lebar
data_str = f"""nama            = {data_nama}
umur            = {data_umur:>15}
tinggi          = {data_tinggi:>15}
nomor sepatu    = {data_sepatu:>15}
bitch           = {data_body:>15}
"""
print("\n" + 5 * "=" + "Data String" + 5 * "=")
print(data_str)
