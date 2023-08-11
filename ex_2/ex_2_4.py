from os import system
from time import sleep
from math import floor


def equivalente():
    print("Calculadora de periodos de tiempo")
    total = int(input("Ingrese la cantidad de segundos: "))
    # Días
    day = floor(total / 60 / 60 / 24)
    if day > 0:
        total = total % (60 * 60 * 24)
    # Horas
    hour = floor(total / 60 / 60)
    if hour > 0:
        total = total % (60 * 60)
    # Minutos
    min = floor(total / 60)
    if min > 0:
        total = total % 60
    # Segundos
    seg = floor(total)

    print("Equivalente en ...")
    print("Días:", day)
    print("Horas:", hour)
    print("Minutos:", min)
    print("Segundos:", seg)


try:
    equivalente()
except ValueError:
    print("Los segundos deben ser un valor numérico entero")
    sleep(3)
    system("cls")
    equivalente()
