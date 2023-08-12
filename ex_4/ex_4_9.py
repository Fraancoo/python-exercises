from os import system


def multi():
    try:
        system("cls")
        print("Multiplicación a x b")
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))

        if a == 0 or b == 0:
            raise ValueError

        rang = b
        sign = " + "
        if b < 0:
            rang = b * -1
            sign = " - "

        print("(" + str(a) + ") x (" + str(b) + ") = ", end="")
        for n in range(rang):
            print("(" + str(a) + ")", end="")
            if n < rang - 1:
                print(sign, end="")
        print(" =", a * b)

    except ValueError:
        print("Ingrese solo números enteros")
        input("\033[0;31m Presione una tecla para continuar ..." + "\033[0;0m")
        multi()


multi()
