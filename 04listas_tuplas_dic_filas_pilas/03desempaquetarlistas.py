numeros = [1,2,3]
numeros2 = [1,2,3,4,5,6,7,8,9]
# primero = numeros[0]
# print(primero)  podriamos hacer esto para convertir un elemto de una lista a variable

primero,segundo,tercero = numeros
print(primero,segundo,tercero)

var1,var2, *otroselementos,penultimo,ultimo = numeros2
print(var1,var2,otroselementos,penultimo,ultimo)
