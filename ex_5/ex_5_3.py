from math import ceil
from os import system
from random import random

system("cls")

nums = []

for x in range(0, 15):
    nums.append(ceil(random() * 10))

print("Lista de números:")
print(nums)

print("")

for n in nums:
    print("Números pares: ", end='')
    if n % 2 == 0:
        print(n, " ")
    print("")
    print("Números impares: ", end='')
    if n % 2 != 0:
        print(n, " ")
