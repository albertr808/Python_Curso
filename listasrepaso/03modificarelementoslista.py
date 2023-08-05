lenguajes = ["C","Java","Python","JavaScript","Kotlin"]
#asignar o remover elementos a una lista 
lenguajes[0] = lenguajes[0]+"++" #especificar la posicion del elemento a modificar y asignarle su nuevo valor
print(lenguajes)

#remplazar ciertos elementos de una lista
lenguajes[0:2] = ["TypeScript","C"]
"""se remplazan los elementos de 0,1 y se cambian por los nuevos""" 
print(lenguajes)

#ingresar nuevos elementos a una lista 
#es una de varias formas
lenguajes[5:6] = "R"
print(lenguajes)
