try:
    print("Ingrese un número")
    num = int(input('Número: '))
    print("El número es:", num)
except ValueError:
    print("Debe ingresar un valor numérico")
finally:
    print("Adios")
