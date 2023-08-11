try:
    print()
    aniosPerro = int(input("Edad del perro: "))
    aniosHumano = 0
    for x in range(aniosPerro):
        anio = x + 1
        if anio == 1 or anio == 2:
            aniosHumano += 10.5
        else:
            aniosHumano += 4
except ValueError:
    print("El valor debe ser numérico")
finally:
    print(str(aniosPerro) + " son " + str(aniosHumano) + " años humanos")
