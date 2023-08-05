#los diccionarios son una coleccion de datos que se encuentran agrupados por una llave y un valor
#a la izquieda es string y a la derecha cualquier valor o tipo de datos
punto = {"x":25, "y":50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45  #agrgar elementos

if "w" in punto:
    print(punto["w"])

print(punto.get("x"))  #acceder a un valor del elemto con get
print(punto.get("w",100))
del punto["x"] #eliminar llave y su valor
print(punto)
del(punto ["y"])
print(punto)
punto ["x"] = 25

for valor in punto:
    print(valor,punto[valor])

for valor in punto.items():
    print(valor)

for llave,valor in punto.items():
    print(llave,valor)