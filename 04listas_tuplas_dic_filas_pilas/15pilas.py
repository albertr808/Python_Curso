#lifo last in first out ,el ultimo que ingresa es el primero en salir
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
ultimoElemento = pila.pop()

print(ultimoElemento)
print(pila)
print(pila[-1])
pila.pop()
print(pila)
if not pila:
    print("pila vacia")