print("Ingrese la medida de los 3 lados de un triángulo")
lado1 = int(input("Medida del lado 1: "))
lado2 = int(input("Medida del lado 2: "))
lado3 = int(input("Medida del lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("Es un triángulo equilátero")
elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2):
    print("Es un triángulo isósceles")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Es un triángulo escaleno")
