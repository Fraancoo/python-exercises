print('Cálculo de la media de una serie de datos')
print('-----------------------------------------')
# Inicializamos las variables
suma = 0
num = 0
# Leemos datos y los procesamos hasta que introducen 0
x = float(input('Introduce un valor (0 para acabar) : '))
while x != 0:
    suma = suma + x
    num = num + 1
    x = float(input('Introduce un valor (0 para acabar) : '))
# Damos los resultados
print('La media de los elementos es', suma/num)
