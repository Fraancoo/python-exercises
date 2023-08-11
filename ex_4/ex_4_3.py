from os import system
from time import sleep


def basilea():
    system("cls")
    print("Problema de Basilea")
    i = int(input("Ingresa el valor de I: "))

    for x in range(i):
        print("")
        print("  1   ")
        print(" --- +")
        print("  " + str(x + 1) + "   ")
        print("")


try:
    basilea()
except ValueError:
    print("Debe ingresar un valor numérico entero")
    sleep(3)
    basilea()
