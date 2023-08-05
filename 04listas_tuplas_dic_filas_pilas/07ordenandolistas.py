numeros = [1,22,34,5,6,9,67,1,2,345,345,2,4,6,4,1,9,7,8,9,1234]
nombres = [[4,"raul"],[1,"hugo"],[3,"alejandro"]]
nombres2 = [["raul",2,3],["hugo",1,2],["alejandro",3,1]]

numeros.sort()  #ordena numeros
numeros.sort(reverse=True)  #ordena elementos de manera descendente
numeros2 = sorted(numeros)       #devuelve una nueva lista ordenados, puede ser asc y descendente
print(numeros)
print(numeros2)


nombres.sort()
print(nombres)

#ordena ahora con el indice en el segundo elemento
#funcion que retorna el segundo elemento
def ordena(elemento):
    return elemento[1]

nombres2.sort(key=ordena)
print(nombres2)

#con lambda

nombres2.sort(key= lambda elemento1: elemento1[1])
print(nombres2)