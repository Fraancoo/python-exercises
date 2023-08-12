from os import system


def triangulo():
    try:
        system("cls")
        print("")
        long = int(input("Ingrese la longitud del triángulo: "))

        if long < 1:
            raise ValueError

        for x in range(long):
            print(x * "*")

        for x in range(long):
            print((long - x) * "*")

    except ValueError:
        print("Ingrese un número entero positivo")
        input("\033[0;31mPresione una tecla para continuar ...\033[0;0m")
        triangulo()


triangulo()
