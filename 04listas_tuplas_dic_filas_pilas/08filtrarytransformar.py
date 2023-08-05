usuarios = [["raul",2],["hugo",1],["alejandro",3]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])  #esto extrae los nombres de la lista y los pasa a otra llamada "nombres"y quita los id
# print(nombres)

# nombres = [expresion for item in items]
nombres = [usuario[0] for usuario in usuarios]
print(nombres)
#filtrar
nombres = [usuario for usuario in usuarios if usuario [1]>2]
print(nombres)