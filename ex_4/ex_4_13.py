from os import system


def inp(msg):
    i = int(input(msg + ": "))
    if i < 1:
        raise ValueError
    return i


def rect():
    try:
        system("cls")
        print("Ingrese las dimensiones de una reja")
        col = inp("Columnas")
        row = inp("Filas")
        alt = inp("Altura")
        anch = inp("Anchura")

        print(col * ("+" + (anch * "-")), end="+\n")
        for c in range(col):
            for a in range(alt):
                for r in range(row):
                    print("|" + (anch * " "), end="")
                print("|")
            print(col * ("+" + (anch * "-")), end="+\n")

    except ValueError:
        print("Ingrese solo números enteros positivos")
        input("\033[0;31mPresione una tecla para continuar... \033[0;0m")
        rect()


rect()
