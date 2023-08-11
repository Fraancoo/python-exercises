from os import system


def fibonacci():
    try:
        system("cls")
        print("* * * * * * * * * Serie de Fibonacci * * * * * * * *")
        print("Ingrese el número de elementos que quiera visualizar")
        elems = int(input("#:"))
        ant2 = 0
        ant1 = 1

        if elems < 1:
            raise ValueError

        for e in range(elems):
            print("Fibonacci", e, "= ", end='')
            if e > 1:
                act = ant2 + ant1
                print(act)
                ant2 = ant1
                ant1 = act
            elif e == 0:
                print("0")
            elif e == 1:
                print("1")
    except ValueError:
        print("Debe ingresar un número mayor a 0")
        input("\033[0;31m Presione una tecla para continuar ..." + "\033[0;0m")
        fibonacci()


fibonacci()
