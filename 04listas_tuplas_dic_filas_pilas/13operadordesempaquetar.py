lista = [1,2,3,4]
lista2 = (1,2,3,4,5)
print(lista)
print(*lista)
print(*lista2)

combinada = ["hola",*lista, *lista2]
print(combinada)

punto1 = {"x":19}
punto2 = {"y":20}

nuevoPunto = {**punto1,**punto2,"z":"holamundo"}
print(nuevoPunto)