from os import system
from time import sleep


def ecuacion():
    print("Calculadora de la ecuación ax + b = 0")
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))

    if a != 0:
        print("x = -b/a")
        print("x = -(" + str(b)+")/(" + str(a)+")")
        print("x =", -(b)/a)
    elif a == 0 and b != 0:
        print("La ecuación no tiene solución")
    elif a == 0 and b == 0:
        print("No sé, espero haberte ayudado")


try:
    ecuacion()
except ValueError:
    print("Los valores de a y b deben ser valores numéricos")
    sleep(3)
    system("cls")
    ecuacion()
