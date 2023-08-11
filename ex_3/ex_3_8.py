dia = int(input('Introduce un día de la semana (entre 1 y 7): '))
print('El día es ... ', end='')

if dia == 1:
    print('lunes')
elif dia == 2:
    print('martes')
elif dia == 3:
    print('miércoles')
elif dia == 4:
    print('jueves')
elif dia == 5:
    print('viernes')
elif dia == 6 or dia == 7:
    print('festivo')
else:
    print('incorrecto')
