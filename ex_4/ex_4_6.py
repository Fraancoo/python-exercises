from os import system
from time import sleep, time
from random import randint


secret_num = randint(1, 100)
count = 0
start = time()


def adivina():
    global count, start
    count = count + 1
    print(" - - - - - Intento:", count, " - - - - - ")
    num = int(input("Ingresa un número del 1 al 100: "))
    if num < 1 or num > 100:
        print("Ingrese un número del 1 al 100")
        adivina()
    elif num == secret_num:
        end = time()
        print("* / - \ * / - \ * / - \ * / - \ *")
        print("* \ - Le atinasteeee xdxdxd - / *")
        print("* / - Intentos:", count, "          - \ *")
        print("* \ - Tiempo:", "{:.1f}".format(end - start), "         - / *")
        print("* / - \ * / - \ * / - \ * / - \ *")
    elif num > secret_num:
        print("Intenta un número más pequeño •v•")
        adivina()
    elif num < secret_num:
        print("Intenta un número más grande e.e")
        adivina()


try:
    system("cls")
    print("* / - \ * / - \ * / - \ * / - \ *")
    print("* \ - / Adivina el número \ - / *")
    print("* / - \ * / - \ * / - \ * / - \ *")
    adivina()
except ValueError:
    print("Ingrese un valor numérico entero")
    sleep(3)
    system("cls")
    adivina()
