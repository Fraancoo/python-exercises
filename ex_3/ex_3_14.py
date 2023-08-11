from os import system
from math import sqrt
from time import sleep


def ecuacion():
    print("Calculadora de la ecuación ax^2 + bx + c = 0")
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    c = int(input("Ingrese el valor de c: "))
    


try:
    ecuacion()
except ValueError:
    print("Los valores de a, b y c deben ser valores numéricos")
    sleep(3)
    system("cls")
    ecuacion()
