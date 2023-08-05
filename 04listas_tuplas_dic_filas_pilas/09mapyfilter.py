usuarios = [["raul",2],["hugo",1],["alejandro",3]]

#filter
nombres = list(map(lambda usuario: usuario[0],usuarios))
#map
menosUsuarios = list(filter(lambda usuario: usuario [1]>2,usuarios))
print(nombres)
print(menosUsuarios)
