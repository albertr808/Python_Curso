###igual que las listas solo queno se pueden:modificar, agregar elementos o quitar###
numeros = (1,2,3,4,5,6)+(7,8,9,10)
print(numeros)

punto = tuple([1,2]) #funcion tuple recibe cualquier cosa que sea iterable
print(punto)

solo12345 = numeros[:5]  #podemos acceder a elementos de una tupla
print(solo12345)
primero, segundo, *otros = numeros #podewmos desempaquetar
print(primero,segundo,otros)

for numero in numeros:
    print(numero)

listaNumeros = list(numeros)
listaNumeros[0] = "hola"
print(listaNumeros)
print(numeros)