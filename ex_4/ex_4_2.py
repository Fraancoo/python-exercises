count = 0

while count < 3:
    print("Intentos restantes (" + str(3 - count) + ")")
    pw = input("Ingrese la contraseña: ")
    if pw == 'iloveyou123':
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        count += 1
