from os import system
from time import sleep


def apilar():
    system("cls")
    filas = 0
    latas = int(input("Ingrese el número de latas: "))

    while (latas > 0):
        filas += 1
        latas = latas - filas

    for f in range(filas):
        print(((filas - 1) * 2 - (f * 2)) * " ", end="")
        print((f + 1) * "  * ")

    if latas < 0:
        print("Latas restantes:", latas + filas)


try:
    apilar()
except ValueError:
    print("Debe ingresar un número entero")
    sleep(2)
    apilar()
