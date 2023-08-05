"""metodos de las listas:
Añadir elementos
para ejecutar estos metodos:VariableTipoLista.metodo()
insert()
append()                                                                        """

lenguajes = ["C","Java","Python","JavaScript","Kotlin"]

#insert()

lenguajes.insert(0,"C++") #inserta un elemento en el indice selecciona
#esto no remplaza ninguno otro elemento,solo lo recorre
print(lenguajes)

#append() agrega el elemento al final de la lista

lenguajes.append("TypeScript")
print(lenguajes)

#unirlistas

lenguajes2 = ["Anaconda","R","Pascal"]
lenguajes2.extend(lenguajes)
print(lenguajes2)
