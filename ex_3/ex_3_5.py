try:
    num = int(input("Ingrese un número: "))
    if num > 0:
        print("El número es positivo")
    elif num < 0:
        print("El número es negativo")
    elif num == 0:
        print("El número es 0")
except ValueError:
    print("Debe ingresar un número")
