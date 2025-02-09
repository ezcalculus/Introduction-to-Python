# latihan komparasi dan boolean

print("Suatu bilangan memenuhi pada : \n~ interval <5 atau >=10 \n~ interval 6 sampai 10 \n~ hanya interval <5 \n~ hanya interval >= 10 ")
interval = float(input("Check any number --> "))

# +++5-------------
Example1 = (interval < 5)
print("Kurang dari <5 =", Example1)

# ------------10+++
Example2 = (interval >= 10)
print("Lebih dari sama dengan >=10 =", Example2)

# +++5--------10+++
Example3 = (Example1 or Example2)
print("Conclusion +++5--------10+++ =", Example3)

# ---5++++++++10---
Ex4 = (interval > 5)
Ex5 = (interval <=10)
print("Conclusion ---5++++++++10--- =", Ex5 and Ex4)
# Example4 = (5 < interval <= 10)
# print("Conclusion ---5++++++++10--- =", Example4)