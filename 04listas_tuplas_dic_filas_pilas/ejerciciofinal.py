from pprint import pprint
"""eliminar los espacios en blanco de un string
y devolver una lista con los caracteres restantes

2.contar en un diccionario cuanto se repiten los caracteres de un string

3.ordenar las llaves de un diccionario por el valor que tienen y devolver una lista
que contiene las tuplas[("a",3),("b",2),("c",4),("d",4)]

4.de un listado de tuplas devolver las tuplas que tengan mayor valor
[("a",3),("b",2),("c",4),("d",4)] ---> [("c",4),("d",4)]
5. crear un mensaje que diga:
los caracteres que mas se repiten con 4 son
c y d

"""


cadena = "a b c d e a b f w c e d g d c ed"
def quitar_espacios(cadena):
    return [char for char in cadena if char != " "]

def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )
def mayor_tupla(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden [1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

def crea_mensaje(diccionario):
    mensaje = "los que mas se repiten son \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sinespacios = quitar_espacios(cadena)
contados = cuenta_caracteres(sinespacios)
ordenados = ordena(contados)
mayores = mayor_tupla(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)
