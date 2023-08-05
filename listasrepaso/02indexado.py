#indexado y sublistas

lista = ["hola","mundo",":)"]

#acceder a la ultima posicion
ultimaPosicion = lista[-1]
print(f"\nel elemento de la ultima posicion es: {ultimaPosicion}\n")

#sublistas o accerder a un rango de elementos
sublistas = lista[0:2]  #para regresar una lista al reves ponemos [::-1]
print(f"{sublistas}")

#saber si algo esta dentro de la lista
palabra = "hola"
if palabra in lista:
    print(f" \"{palabra}\" esta en la lista")
else:
    print(f" \"{palabra}\" no se encuentra en la lista")


