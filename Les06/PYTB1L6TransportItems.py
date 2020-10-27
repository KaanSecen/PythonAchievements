import os
import sys
import time

os.system('cls')

factory = []
distribution = []
shop = []

print("Factory:  []")
print("distribution:  []")
print("shop:  []")

factory.append("Shoes")

time.sleep(1)

factory2 = str(factory)

os.system('cls')

print("Factory:  " + factory2)
print("distribution:  []")
print("shop:  []")

factory.clear()

distribution.append("Shoes")

time.sleep(1)

distribution2 = str(distribution)

os.system('cls')

print("Factory:  []")
print("distribution:  " + distribution2)
print("shop:  []")

distribution.clear()

shop.append("Shoes")

time.sleep(1)

shop2 = str(shop)

os.system('cls')

print("Factory:  []")
print("distribution:  []")
print("shop:  " + shop2)

shop.clear()

time.sleep(1)

os.system('cls')

print("Factory:  []")
print("distribution:  []")
print("shop:  []")

time.sleep(1)

result=input("Opnieuw? Y/N\n>")
if result=='y' or result =='Y':
     os.system('python "PYTB1L6TransportItems.py"')
else:
     time.sleep(1)
     print("Gemaakt Door Kaan Secen.")