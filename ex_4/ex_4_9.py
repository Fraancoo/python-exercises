from os import system


def multi():
    try:
        system("cls")
    except ValueError:
        print("Debe ingresar solo números enteros")
        input("\033[1;41m Presione una tecla para continuar ..." + "\033[0;0m")
        multi()


multi()
