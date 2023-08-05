# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John")
beatles.append("Paul")
beatles.append("George")
print("paso 2:",beatles)

# paso 3
for beatles2 in range (2):
    nIntegrantes = str(input( "ingrese nuevos integrantes"))
    beatles2 = nIntegrantes
    beatles.append(beatles2)
print("paso 3", beatles)

#paso 4

del beatles[4]
del beatles[3]
print("paso 4 :", beatles)

#paso5
beatles.insert(3,"Ringo")
print("paso 5 :", beatles)
