buscar = 1
for numero in range(1,11):
    print(numero)
    if numero == buscar:
        print("encontrado",buscar)
        break
else:
    print("no se encontro el numero")