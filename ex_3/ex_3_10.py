size = int(input("Escriba el tamaño del tornillo (cm): "))
print("El tornillo es ", end='')

if size >= 1 and size < 3:
    print("pequeño")
elif size >= 3 and size < 5:
    print("mediano")
elif size >= 5 and size < 6.5:
    print("grande")
elif size >= 6.5 and size < 8.5:
    print("muy grande")
