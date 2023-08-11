class Producto:
    name = ""
    price = 0
    sells = 0


prodA = Producto()
prodA.name = "Sabritas"
prodA.price = 20
prodA.sells = 450

prodB = Producto()
prodB.name = "Dulce"
prodB.price = 5
prodB.sells = 225

prodC = Producto()
prodC.name = "Juguete"
prodC.price = 50
prodC.sells = 275

print("Las ventas del producto A son las más elevadas: " +
      str(prodA.sells > prodB.sells and prodA.sells > prodC.sells))
print("Ningún producto tiene ventas inferiores a 200: " +
      str(prodA.sells >= 200 and prodB.sells >= 200 and prodC.sells >= 200))
print("Algún producto tiene unas ventas superiores a 400: " +
      str(prodA.sells > 400 or prodB.sells > 400 or prodC.sells > 400))
print("La media de ventas es superior a 500: " +
      str(((prodA.price * prodA.sells) / prodA.sells) > 500 and ((prodB.price * prodB.sells) / prodB.sells) > 500 and ((prodC.price * prodC.sells) / prodC.sells) > 500))
print("El producto B no es el más vendido: " +
      str(prodB.sells < prodA.sells or prodB.sells < prodC.sells))
print("El total de ventas esta entre 500 y 1000: " +
      str((prodA.sells + prodB.sells + prodC.sells) >= 500 and (prodA.sells + prodB.sells + prodC.sells) <= 1000))


print("Media del producto " + prodA.name + " es " +
      str((prodA.price * prodA.sells) / prodA.sells))
print("Media del producto " + prodB.name + " es " +
      str((prodB.price * prodB.sells) / prodB.sells))
print("Media del producto " + prodC.name + " es " +
      str((prodC.price * prodC.sells) / prodC.sells))
