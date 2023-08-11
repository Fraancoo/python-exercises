def passwd():
    pw = input("Ingrese la contraseña: ")
    if pw == 'iloveyou123':
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
        passwd()

passwd()
