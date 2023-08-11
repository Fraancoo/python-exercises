a, b, c = [int(x) for x in input('Dame tres valores enteros: ').split(' ')]
r = (a if a < c else c) if a < b else (b if b < c else c)
print('Resultado:', r)
