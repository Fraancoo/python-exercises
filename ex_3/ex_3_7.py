num1 = int(input('Introduce el valor 1: '))
min = num1
max = num1

num2 = int(input('Introduce el valor 2: '))
if num2 < min:
    min = num2
else:
    max = num2

num3 = int(input('Introduce el valor 3: '))
if num3 < min:
    min = num3
elif num3 > max:
    max = num3

print('El mínimo es', min)
print('El máximo es', max)
