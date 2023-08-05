"""Enunciado:Tenemos un texto donde queremos encontrar palabras clave.
las palabras clave pueden ser hasta 5 y debermos pedirselos al usuario
y guardarlas en una lista
"""
#si el usuario requiere poner menos de 5 palabras clave, debera escrbir 
# "fin" para terminar de introdcuir los datos.Si el usuario introduce
#numeros o nada, deberemos eliminarlos de la lista antes de la busqueda.

#en otra lista ,deberemos guardar el numero de veces que aparecer cada
#palabra clave en nuestro texto.Por ejemplo, si las palabras clave son
#"ordenador " y "portatil" y aparecen 5 o 7 veces respectivamente, nuestra
#lista deberian ser asi
#       -Keywords = ["ordenador","portatil"]
#       -Ocurrencias = [5,7]

#podemos pasar de una cadena de texto a una lista de palabras mediante el metodo split()
#ejemplo : texto = "hola mundo"
#          print(texto.split())
#          texto = ["hola","mundo"]
#palabras a buscar "arte","tecnica","cientifica","investigacíon","tecnológica"

texto ="""El Estado del Arte/Estado de la técnica, hace referencia al estado último del conocimiento sobre la investigación y el desarrollo (I+D), es decir que es el límite de conocimiento generado sobre un tema o problema de investigación científica y/o tecnológica, estableciendo hasta donde ha avanzado el mismo, cual es la frontera en un 
tiempo y espacio determinado.
En el inicio del proceso de construcción y/o descubrimiento de conocimientos científicos mediante la investigación, sin duda alguna, los profesores se preguntan ¿El 
estado del arte/técnica, es una de esas ocurrencias de la gestión de la investigación 
(Gestores), para complicar el trabajo de los investigadores en la formulación de sus 
protocolos de I+D? ¿Es el afán de hacer más burocrático el acceso al financiamiento, 
especialmente si este, tiene como fuente el presupuesto universitario? De igual 
manera, los investigadores con escasa experiencia en investigación tienen la percepción que el estado del arte/técnica es lo mismo que Marco Teórico y como tal lo tratan. 
En aras de contribuir a un mejor discernimiento e internalización y la adecuada utilización de estos elementos fundamentales de todo proyecto de investigación científica 
y/o tecnológica hemos preparado una síntesis sobre el tema."""


keywords = []
ocurrencias = []

for x in range(5):
    keyword = input("introduce una palabra o fin para terminar")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword)
print(keywords)

posicion = 0
while(True):
    if posicion >= len(keywords):
        break
    if keywords[posicion] == '':
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric():
        keywords.pop(posicion)
    else:
        posicion = posicion+1

print("lista corregida")
print(keywords)

texto = texto.split()
for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            pos = keyword.index(keyword)
            ocurrencias[pos] += 1
            break
