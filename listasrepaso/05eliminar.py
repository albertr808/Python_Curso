"""metodos elimnar elementos
pop()
remove()
del()
"""
lenguajes = ["C","Java","Python","JavaScript","Kotlin"]
print(lenguajes)

#pop()

lenguajes.pop() #por defecto eliminar el ultimo elemento
lenguajes.pop(0) #elimina el elemento del indice indicado
#si ponemos un indice fuera de rango nos dara un error
print(lenguajes)

#remove()

lenguajes.remove("Python")  #elimina por caracter especifico
#si ponemos algo que no esta en la lista dara un error
print(lenguajes)

#eliminar elemento con "del"

# del lenguajes[3]
# print(lenguajes)

#index , nos dice si este elemento existe o no en la lista y nos devuelve donde se encuentra
indice = lenguajes.index("JavaScript")
print(indice)